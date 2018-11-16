from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from yellowbrick.text import FreqDistVisualizer
from yellowbrick.features.pca import PCADecomposition
from sklearn.decomposition import NMF, PCA, TruncatedSVD
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d



import pandas as pd
import numpy as np


if __name__ == '__main__':
    df = pd.read_csv('../data/lem_scripts_df_NEW')
    # scripts =
    df.dropna(inplace=True)
    X = df['script']
    y = df.pop('rating')

    cv = CountVectorizer()
    docs = cv.fit_transform(X)
    features = cv.get_feature_names()

    # visualizer = FreqDistVisualizer(features=features, n=10)
    # visualizer.fit(docs)
    # visualizer.poof()

    # visualizerPCA = PCADecomposition(scale=True, color='orange', proj_dim=3)
    # visualizerPCA.fit_transform(docs, y)
    # visualizerPCA.poof()

    # NORMALIZERS = {'l1': Normalizer(copy=True, norm='l1'), 'l2':
    # Normalizer(copy=True, norm='l2'), 'maxabs': MaxAbsScaler(copy=True),
    # 'minmax': MinMaxScaler(copy=True, feature_range=(0, 1)), 'standard':
    # StandardScaler(copy=True, with_mean=False, with_std=True)}

    tsvd = TruncatedSVD(n_components=3)
    X_tsvd = tsvd.fit_transform(docs)



    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    x = X_tsvd[:,0]
    y = X_tsvd[:,1]
    z = X_tsvd[:,2]

    ax.scatter(x, y, z, color='b')

    ax.set_xlabel('Topic 0')
    ax.set_ylabel('Topic 1')
    ax.set_zlabel('Topic 2')



    plt.show()
