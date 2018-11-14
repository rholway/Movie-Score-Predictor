import pandas as pd
import numpy as np
from string import punctuation, printable
import matplotlib as mpl
import matplotlib.pyplot as plt
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
nlp = spacy.load('en_core_web_md')
nlp.Defaults.stop_words.add('pron')


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
    # if not stop_words:
    #     stop_words = []

    # stop_words = STOP_WORDS
    added_stops = set([word for word in doc if word[:].isupper()])
    stop_words = STOP_WORDS.union(added_stops)


        # .append([word for word in doc if word[0].isupper()])
    # stop_words = STOP_WORDS
    # added_stops = [word for word in doc if word[:].isupper()]
    # added_stops = set(added_stops)
    # stop_words = stop_words.update(added_stops)
    # STOP_WORDS.add({set([word for word in doc if word[:].isupper()])})
    # STOP_WORDS.update({'daa'})

    # for word in doc.split():
    #
    #     if word[:].isupper():
    #         stop_words.append(word)

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
    # for movie plots
    # plot_df = pd.read_csv('../data/movie_plot_df')
    # plot_df['rating'] = plot_df['rating'].str.replace('%','')
    # plot_df['rating'] = pd.to_numeric(plot_df['rating'], errors='coerce')
    # plot_df.dropna(inplace=True)
    # plot_df['plot'] = plot_df['plot'].apply(lemmatize_string)
    # lem_df = plot_df.filter(['title', 'plot', 'rating'], axis=1)
    # lem_df.to_csv('../data/lem_plot_df')
    # mean_len = plot_df['plot'].str.len().groupby(plot_df['plot']).mean()

    # for movie scripts
    # script_df = pd.read_csv('../data/scripts_df_II')
    # script_df['script'] = script_df['script'].apply(lemmatize_string)
    # script_df.to_csv('../data/lem_scripts_df')

    # trial caps df
    d = {'col1': [" here's movie SCRIPT with CHARACTERS available", "SCENE one is with youknowwho CUT"]
    , 'col2': [3, 4]}
    trial_df = pd.DataFrame(data=d)
    trial_df['col1'] = trial_df['col1'].apply(lemmatize_string)
