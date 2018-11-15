import pandas as pd
import numpy as np
from string import punctuation, printable
import matplotlib as mpl
import matplotlib.pyplot as plt
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
nlp = spacy.load('en_core_web_md')
from spacy.lang.en.stop_words import STOP_WORDS
nlp.Defaults.stop_words.add('pron')
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB



def f(row):
    if row['rating'] > 75:
        val = 1
    else:
        val = 0
    return val

def top_n(vectorizer, vectors, data, n):
    '''
    Print out the top 10 words by total tf-idf score
    '''
    words = vectorizer.get_feature_names()

    # Top 10 words by total tfidf
    total = np.sum(vectors, axis=0)
    return (get_top_values(total, n, words))

def get_top_values(lst, n, labels):
    '''
    INPUT: LIST, INTEGER, LIST
    OUTPUT: LIST

    Given a list of values, find the indices with the highest n values. Return
    the labels for each of these indices.
    '''
    return [labels[i] for i in np.argsort(lst)[-1:-n-1:-1]]



if __name__ == '__main__':
    # trial with lem
    df = pd.read_csv('../data/lem_scripts_IV')
    df['r>75'] = df.apply(f, axis=1)
    df.drop(['title', 'rating'], axis=1, inplace=True)
    y = df.pop('r>75')
    X = df['script']
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

    # DO TFIDF TRANSFORMATION
    vectorizer = TfidfVectorizer(max_features=5000,
                                 stop_words=STOP_WORDS,
                                 ngram_range=(1,2))
    vectors = vectorizer.fit_transform(X_train).toarray()
    test_vectors = vectorizer.transform(X_test).toarray()

    mnb = MultinomialNB()
    mnb.fit(vectors, y_train)
    print('Accuracy:', mnb.score(test_vectors, y_test))
    sklearn_predictions = mnb.predict(test_vectors)

    # mnb = MultinomialNB()
    # mnb.fit(X_train, y_train)
    # print('Accuracy:', mnb.score(X_test, y_test))
    # sklearn_predictions = mnb.predict(y_test)
