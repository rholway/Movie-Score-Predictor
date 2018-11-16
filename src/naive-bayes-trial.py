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
from itertools import cycle
from sklearn import svm, datasets
from sklearn.metrics import roc_curve, auc
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import label_binarize
from sklearn.multiclass import OneVsRestClassifier
from scipy import interp



def f(row):
    '''
    function to create two classes based on rotten tomatoes scores of above
    or below 75%
    '''
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

# def roc(algo_name_list, y_predict_list, algo_for_predict_proba_list, y_test, X_test):
#     plt.figure()
#     for name, y_pred, instantiation in zip(algo_name_list, y_predict_list, algo_for_predict_proba_list):
#         roc_auc = roc_auc_score(y_test, y_pred)
#         roc_auc = np.around(roc_auc,2)
#         fpr, tpr, thresolds = roc_curve(y_test, instantiation.predict_proba(X_test)[:, 1])
#         plt.plot(fpr, tpr, label='{} (area = {})'.format(name, roc_auc))
#     plt.plot([0,1],[0,1], 'r--')
#     plt.xlim([0,1])
#     plt.ylim([0,1.1])
#     plt.xlabel('False Positive Rate', weight='bold')
#     plt.ylabel('True Positive Rate', weight='bold')
#     plt.title('ROC Curvey for Model 3', weight='bold')
#     plt.legend(loc='lower right')
#     # plt.show()
#     plt.savefig('ROC_Model3')



if __name__ == '__main__':
    # trial with lem scripts
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



    ### ROC plot

    from sklearn.metrics import roc_curve, auc
    fpr, tpr, thresholds = roc_curve(sklearn_predictions, y_test)
    roc_auc = auc(fpr, tpr)

    plt.figure()
    plt.plot(fpr, tpr, color='darkorange', lw=1, label='ROC curve (area = %0.2f)' % roc_auc)
    plt.plot([0, 1], [0, 1], color='navy', lw=1, linestyle='--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate', fontsize=14)
    plt.ylabel('True Positive Rate', fontsize=14)
    plt.title('ROC Curve', fontsize=20)
    plt.legend(loc="lower right")
    # plt.show()
    plt.savefig('../images/ROCPLOT')
    plt.close()
