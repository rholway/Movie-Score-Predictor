import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from clustering import *



plot_df = pd.read_csv('../data/movie_plot_df')
plot_df['rating'] = plot_df['rating'].str.replace('%','')
plot_df['rating'] = pd.to_numeric(plot_df['rating'], errors='coerce')
plot_df.dropna(inplace=True)


# Histogram of RT Scores
# fig, ax = plt.subplots()
# ax.hist(plot_df['rating'], bins=5)
# ax.set_xlabel('Rotten Tomato Score', fontsize=14)
# ax.set_ylabel('Movie Count', fontsize=14)
# ax.set_title('Histogram of Rotten Tomato Scores', fontsize=20)
# plt.show()
# plt.savefig('../images/hist-of-movie-ratings-plots')

# elbow plot of NMF from plots
# error = [fit_nmf(i) for i in range(1,10)]
# plt.plot(range(1,10), error)
# plt.xlabel('k')
# plt.ylabel('Reconstruction Error')
# plt.show()
