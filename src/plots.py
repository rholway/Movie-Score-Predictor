import matplotlib.pyplot as plt
import numpy as np
import pandas as pd



plot_df = pd.read_csv('../data/movie_plot_df')
plot_df['rating'] = plot_df['rating'].str.replace('%','')
plot_df['rating'] = pd.to_numeric(plot_df['rating'], errors='coerce')
plot_df.dropna(inplace=True)


# Histogram of RT Scores
# fig, ax = plt.subplots()
# ax.hist(plot_df['rating'], bins=100)
# ax.set_xlabel('Rotten Tomato Score', fontsize=14)
# ax.set_ylabel('Movie Count', fontsize=14)
# ax.set_title('Histogram of Rotten Tomato Scores', fontsize=20)
# plt.savefig('../images/hist-of-movie-ratings-plots')
