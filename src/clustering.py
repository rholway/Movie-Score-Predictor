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
from mpl_toolkits.mplot3d import Axes3D


def get_len(str):
    return len(str)

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
    return new_sc_df['title'][top_movies]

# elbow plot in plots.py script

if __name__ == '__main__':
    # plot summaries
    # df = pd.read_csv('../data/lem_plot_df')
    # y = df.pop('rating')
    # X = df['plot']
    # X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
    #
    # # create tfidf vector on plots lem df
    # tfidf_vectorizer = TfidfVectorizer(max_features=5000,
    #                                 stop_words=STOP_WORDS,
    #                                 ngram_range=(1,2))
    # k = 10 # number of topics
    # topics = ['latent_topic_{}'.format(i) for i in range(k)]
    # nmf = NMF(n_components = k)

    # full tfidf plots
    # full_tfidf = tfidf_vectorizer.fit_transform(X).todense()
    # full_tfidf_feature_names = tfidf_vectorizer.get_feature_names()
    # full_titles = X.index
    # nmf.fit(full_tfidf)
    # W_f = nmf.transform(full_tfidf)
    # H_f = nmf.components_
    # W_f = pd.DataFrame(W_f, index = full_titles, columns = topics)
    # H_f = pd.DataFrame(H_f, index = topics, columns = full_tfidf_feature_names)
    # W_f,H_f = (np.around(x,2) for x in (W_f, H_f))


    # # train tfidf plots
    # train_tfidf = tfidf_vectorizer.fit_transform(X_train).todense()
    # train_tfidf_feature_names = tfidf_vectorizer.get_feature_names()
    # train_titles = X_train.index
    # nmf.fit(train_tfidf)
    # W_tr = nmf.transform(train_tfidf)
    # H_tr = nmf.components_
    # W_tr = pd.DataFrame(W_tr, index = train_titles, columns = topics)
    # H_tr = pd.DataFrame(H_tr, index = topics, columns = train_tfidf_feature_names)
    # W_tr,H_tr = (np.around(x,2) for x in (W_tr, H_tr))


    # # test tfidf plots
    # test_tfidf = tfidf_vectorizer.transform(X_test).todense()
    # test_tfidf_feature_names = tfidf_vectorizer.get_feature_names()
    # test_titles = X_test.index
    # # nmf.fit(test_tfidf)
    # W_te = nmf.transform(test_tfidf)
    # H_te = nmf.components_
    # W_te = pd.DataFrame(W_te, index = test_titles, columns = topics)
    # H_te = pd.DataFrame(H_te, index = topics, columns = test_tfidf_feature_names)
    # W_te,H_te = (np.around(x,2) for x in (W_te, H_te))

    # first lem df scipts
    # sc_df = pd.read_csv('../data/lem_scripts_df')
    # y = sc_df.pop('rating')
    # X = sc_df['script']

    # updated lemmatized df of scripts
    # new_sc_df = pd.read_csv('../data/lem_scripts_IV')
    # y = new_sc_df.pop('rating')
    # X = new_sc_df['script']

    # once again, updated lemmatized df of scripts with more stop words
    new_sc_df = pd.read_csv('../data/lem_scripts_df_NEW')
    new_sc_df.dropna(inplace=True)
    new_sc_df.drop('Unnamed: 0.1', axis=1, inplace=True)
    new_sc_df.rename(columns={'Unnamed: 0':'len'}, inplace=True)
    new_sc_df['len'] = new_sc_df['script'].apply(get_len)
    new_sc_df = new_sc_df.query('len > 1000')
    # it doesn't look like these three scripts were lemmatized  - i think foreign language
    new_sc_df.drop(new_sc_df.loc[new_sc_df['len']==117849].index, inplace=True)
    new_sc_df.drop(new_sc_df.loc[new_sc_df['len']==95413].index, inplace=True)
    new_sc_df.drop(new_sc_df.loc[new_sc_df['len']==78897].index, inplace=True)
    y = new_sc_df.pop('rating')
    X = new_sc_df['script']

    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

    tfidf_vectorizer = TfidfVectorizer(max_features=5000,
                                    stop_words=STOP_WORDS,
                                    ngram_range=(1,2))
    k = 3 # number of topics
    topics = ['latent_topic_{}'.format(i) for i in range(k)]
    nmf = NMF(n_components = k)

    # full tfidf scripts
    full_tfidf = tfidf_vectorizer.fit_transform(X).todense()
    full_tfidf_feature_names = tfidf_vectorizer.get_feature_names()
    full_titles = X.index
    nmf.fit(full_tfidf)
    W_f = nmf.transform(full_tfidf)
    H_f = nmf.components_
    W_f = pd.DataFrame(W_f, index = full_titles, columns = topics)
    H_f = pd.DataFrame(H_f, index = topics, columns = full_tfidf_feature_names)
    W_f,H_f = (np.around(x,2) for x in (W_f, H_f))

    x = W_f.iloc[:,0]
    y = W_f.iloc[:,1]
    z = W_f.iloc[:,2]

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.scatter(x, y, z, color='b')

    ax.set_xlabel('Topic 0')
    ax.set_ylabel('Topic 1')
    ax.set_zlabel('Topic 2')

    plt.show()


    # # train tfidf plots
    # train_tfidf = tfidf_vectorizer.fit_transform(X_train).todense()
    # train_tfidf_feature_names = tfidf_vectorizer.get_feature_names()
    # train_titles = X_train.index
    # nmf.fit(train_tfidf)
    # W_tr = nmf.transform(train_tfidf)
    # H_tr = nmf.components_
    # W_tr = pd.DataFrame(W_tr, index = train_titles, columns = topics)
    # H_tr = pd.DataFrame(H_tr, index = topics, columns = train_tfidf_feature_names)
    # W_tr,H_tr = (np.around(x,2) for x in (W_tr, H_tr))
    #
    # # test tfidf plots
    # test_tfidf = tfidf_vectorizer.transform(X_test).todense()
    # test_tfidf_feature_names = tfidf_vectorizer.get_feature_names()
    # test_titles = X_test.index
    # # nmf.fit(test_tfidf)
    # W_te = nmf.transform(test_tfidf)
    # H_te = nmf.components_
    # W_te = pd.DataFrame(W_te, index = test_titles, columns = topics)
    # H_te = pd.DataFrame(H_te, index = topics, columns = test_tfidf_feature_names)
    # W_te,H_te = (np.around(x,2) for x in (W_te, H_te))
