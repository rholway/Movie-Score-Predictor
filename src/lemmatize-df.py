import pandas as pd
import numpy as np
from string import punctuation, printable
import matplotlib as mpl
import matplotlib.pyplot as plt
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
nlp = spacy.load('en_core_web_md')
from spacy.lang.en.stop_words import STOP_WORDS
import os,re,pickle
# plt.style.use('bmh')

# import scipy.stats as stats
# from sklearn import manifold
# from mylib import *

## lemmatize string function
def lemmatize_string(doc, stop_words=STOP_WORDS):
    """
    takes a list of strings where each string is a document
    returns a list of strings
    """

    if not stop_words:
        stop_words = []

    # First remove punctuation form string
    PUNCT_DICT = {ord(punc): None for punc in punctuation}
    doc = doc.translate(PUNCT_DICT)

    # remove unicode
    clean_doc = "".join([char for char in doc if char in printable])

    # Run the doc through spaCy
    doc = nlp(clean_doc)

    # Lemmatize and lower text
    tokens = [re.sub("\W+","",token.lemma_.lower()) for token in doc ]
    tokens = [t for t in tokens if len(t) > 1]

    return ' '.join(w for w in tokens if w not in stop_words)

if __name__ == '__main__':
    plot_df = pd.read_csv('../data/movie_plot_df')
    plot_df['rating'] = plot_df['rating'].str.replace('%','')
    plot_df['rating'] = pd.to_numeric(plot_df['rating'], errors='coerce')
    plot_df.dropna(inplace=True)
    plot_df['plot'] = plot_df['plot'].apply(lemmatize_string)
    lem_df = plot_df.filter(['plot', 'rating'], axis=1)
    lem_df.to_csv('lem_plot_df')

    # mean_len = plot_df['plot'].str.len().groupby(plot_df['plot']).mean()
