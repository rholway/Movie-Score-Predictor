import urllib
import json
# http://www.omdbapi.com/?apikey=OMD_API&
import omdb
import requests
from omdb import OMDBClient

API_KEY = "80ed70f5"
client = OMDBClient(apikey=API_KEY)
movie = omdb.get(title='True Grit', fullplot=True, tomatoes=True)
# print(movie['plot'], movie['ratings'][1]['value'])


movie2 = omdb.imdbid('tt0065126', fullplot=True)
movie2_data = movie2['plot'], movie2['ratings'][1]['value']
print(movie2_data[1])


# omdb.set_default('apikey', API_KEY)

# omdb.set_default('OMD_API', 'OMD_API')
# res = omdb.request(t='Get Out')
# data = omdb.get(title='True Grit')

# def website_search(query):
#     api_key = web_api
#     url = http://www.omdbapi.com/?apikey=OMD_API&
#     rating = query.replace(' ','%20')
#     final_url = url + '&rating' + rating + '&plot=full'
#     json_obj = urllib.urlopen(final_url)
#     data = json.load(json_obj)
#     for item in data['objects']:
#         print item['rating'], item['plot=full']

#!/usr/bin/env python3
# import requests
#
# URL = "http://www.omdbapi.com/"
# API_KEY = "80ed70f5"
#
# def get(params):
#     response = requests.get(URL, params)
#     if response.status_code != 200:
#         print ('WARNING', response.status_code)
#         return None
#     else:
#         return response.json()

# URL = "http://www.omdbapi.com/"

# res = omdb.request(t='True Grit')
# omdb.get(**params)

# def get(params):
#     response = requests.get(URL, params)
#     if response.status_code != 200:
#         print ('WARNING', response.status_code)
#         return None
#     else:
#         data = response.json()['Search']
#         return data[0]['Title']
#
#
# print(get({
#     'apikey': API_KEY,
#     's': 'Strange Wilderness'}))
# ======================================================================

# def get_plot_and_score(IMDbID):
#     m_info = omdb.imdbid(IMDbID, fullplot=True)
#     data = m_info['title'], m_info['plot'], m_info['ratings'][1]['value']
#     temp_df = pd.DataFrame([data], columns=['title', 'plot', 'rating'])
#     return temp_df
    # client = OMDBClient(apikey=API_KEY)
# print(get_plot_and_score('tt0065126'))
# df = pd.DataFrame(columns=['title', 'plot', 'rating'])
