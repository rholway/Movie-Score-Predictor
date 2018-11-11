import os
API_KEY = os.environ['NYT_API_KEY']
import bs4
import requests
import pymongo
import pandas as pd
from pprint import pprint

def init_mongo_client():
    client = pymongo.MongoClient()  # Initiate Mongo client
    db = client.nyt      # Access database
    coll = db.articles   # Access collection
    return db.articles   # return collection pointer

def make_request(n_pages=10):
    '''
    Recursively submit requests to API, paginating over most recent `n_pages`.
    By default, API returns 10 articles per page.
    '''
    endpoint = 'http://api.nytimes.com/svc/search/v2/articlesearch.json'
    document_list = []
    for page in range(0, n_pages):
        payload = {'api-key': API_KEY, 'page': page}
        response = requests.get(endpoint, params=payload)
        if _valid_response(response):
            new_documents = _parse_response(response)
            document_list.extend(new_documents)
        else:
            continue
    return document_list

def _valid_response(response):
    if response.status_code == 200:
        if 'response' in response.json().keys():
            print('SUCCESS: valid response')
            return True
        elif self._is_empty(json):
            print('WARNING: empty response')
            return False
        else:
            print('WARNING: unexpected response')
            return False
    else:
        print ('WARNING: request failed with status code {}'.format(response.status_code))

def _parse_response(response):
    return response.json()['response']['docs']

def _is_empty(any_structure):
    if any_structure:
        return False
    else:
        print('WARNING: Data structure is empty.')
        return True

def insert_documents_into_db(documents):
    collection = init_mongo_client()
    print('{} documents received'.format(len(documents)))
    print('inserting documents into mongodb...')
    document_count = 0
    for doc in documents:
        try:
            collection.insert(doc)
            print(doc['headline']['main'])
            document_count += 1
        except pymongo.errors.DuplicateKeyError:
            print("duplicate record found... skipping...")
            continue
    print('done. {} documents successfully inserted to MongoDB'.format(document_count))

def query_collection(WHERE, SELECT=None):
    collection = init_mongo_client()
    return collection.find(WHERE, SELECT)

def print_collection(cursor):
    '''
    This is a generator!
    Once you do it once, the cursor will be empty
    '''
    for doc in cursor:
        print('hi')
        pprint(doc)

def get_articles(table):
    links = table.find({'web_url': {'$exists': 'true'}},{'web_url': 1})
    import pdb; pdb.set_trace()
    counter = 0
    for uid_link in links:
        counter += 1
        if counter % 100 == 0:
            print ('Count: ', counter, ' ')
            print (uid)
        uid = uid_link['_id']
        link = uid_link['web_url']
        html = requests.get(link).content
        soup = bs4.BeautifulSoup(html, 'html.parser')

        article_content = '\n'.join([i.text for i in soup.select('p.story-body-text')])
        if not article_content:
            article_content = '\n'.join([i.text for i in soup.select('.caption-text')])
        if not article_content:
            article_content = '\n'.join([i.text for i in soup.select('[itemprop="description"]')])
        if not article_content:
            article_content = '\n'.join([i.text for i in soup.select('#nytDesignBody')])
        else:
            article_content = ''

        table.update({'_id': uid}, {'$set': {'raw_html': html}})
        table.update({'_id': uid}, {'$set': {'content_txt': article_content}})

def convert_collection_to_df(cursor):
    return  pd.DataFrame(list(cursor))

if __name__ == '__main__':
    new_documents = make_request(n_pages=10)
    insert_documents_into_db(new_documents)
    WHERE = {'type_of_material': 'Obituary', 'word_count' : {'$gt': 30}}
    SELECT = {'_id': 0, 'snippet': 1, 'source': 1, 'type_of_material': 1}
    cursor = query_collection(WHERE, SELECT)
    df = convert_collection_to_df(cursor)
    cursor.rewind()
    print_collection(cursor)
    WHERE = {'headline.main': {'$regex':  u"President.*"}}
    cursor = query_collection(WHERE, SELECT)
    df = convert_collection_to_df(cursor)
    cursor.rewind()
    print_collection(cursor)
    table = init_mongo_client()
    get_articles(table)
