from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
import pandas as pd
import numpy as np
import spacy
nlp = spacy.load('en_core_web_md')
nlp.Defaults.stop_words.add('pron')
from spacy.lang.en.stop_words import STOP_WORDS
from sklearn.decomposition import NMF
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

def fit_nmf(k):
    nmf = NMF(n_components=k)
    nmf.fit(tfidf)
    W = nmf.transform(tfidf);
    H = nmf.components_;
    return nmf.reconstruction_err_

def top_tokens_in_topic(topic_n, n_tokens, H):
    '''
    input: topic to explore (int), how many tokens to return (int)
    output: top tokens for topic_n
    '''
    top_movies = H.iloc[topic_n].sort_values(ascending=False).index[:n_tokens]
    return top_movies

def top_movies_in_topic(topic_n, n_movies, W):
    top_movies = W.iloc[:,topic_n].sort_values(ascending=False).index[:n_movies]
    return df['title'][top_movies]

# elbow plot in plots.py script

if __name__ == '__main__':
    df = pd.read_csv('../data/lem_plot_df')
    y = df.pop('rating')
    X = df['plot']
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

    # create tfidf vector on plots lem df
    tfidf_vectorizer = TfidfVectorizer(max_features=5000,
                                    stop_words=STOP_WORDS,
                                    ngram_range=(1,2))
    k = 10 # number of topics
    topics = ['latent_topic_{}'.format(i) for i in range(k)]
    nmf = NMF(n_components = k)


    # train tfidf
    train_tfidf = tfidf_vectorizer.fit_transform(X_train).todense()
    train_tfidf_feature_names = tfidf_vectorizer.get_feature_names()
    train_titles = X_train.index
    nmf.fit(train_tfidf)
    W_tr = nmf.transform(train_tfidf)
    H_tr = nmf.components_
    W_tr = pd.DataFrame(W_tr, index = train_titles, columns = topics)
    H_tr = pd.DataFrame(H_tr, index = topics, columns = train_tfidf_feature_names)
    W_tr,H_tr = (np.around(x,2) for x in (W_tr, H_tr))


    # test tfidf
    test_tfidf = tfidf_vectorizer.fit_transform(X_test).todense()
    test_tfidf_feature_names = tfidf_vectorizer.get_feature_names()
    test_titles = X_test.index
    nmf.fit(test_tfidf)
    W_te = nmf.transform(test_tfidf)
    H_te = nmf.components_
    W_te = pd.DataFrame(W_te, index = test_titles, columns = topics)
    H_te = pd.DataFrame(H_te, index = topics, columns = test_tfidf_feature_names)
    W_te,H_te = (np.around(x,2) for x in (W_te, H_te))
