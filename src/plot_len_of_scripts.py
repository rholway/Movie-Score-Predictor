import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def find_len_of_script(str):
    return len(str)



if __name__ == '__main__':
    df = pd.read_csv('../data/scripts_df_II')
    df['script'] = df['script'].apply(find_len_of_script)
    df = df.query('script > 10000')

    # fig, ax = plt.subplots()
    # ax.hist(df['script'], bins=20)
    # ax.set_xlabel('Script Length (words)', fontsize=14)
    # ax.set_ylabel('Movies', fontsize=14)
    # ax.set_title('Histogram of Movie Script Length', fontsize=20)
    # # plt.show()
    # plt.savefig('../images/HISTSCRPLEN')
    # plt.close()

    # fig, ax = plt.subplots()
    # ax.hist(df['rating'], bins=100)
    # ax.set_xlabel('Movie Rating', fontsize=14)
    # ax.set_xlim(0,100)
    # ax.set_ylabel('Movies', fontsize=14)
    # ax.set_title('Histogram of Movie Ratings', fontsize=20)
    # # plt.show()
    # plt.savefig('../images/hist-of-movie-script-ratings')
    # plt.close()

    fig, ax = plt.subplots()
    ax.scatter(df['rating'], df['script'], c='g')
    ax.set_xlabel('Movie Rating', fontsize=14)
    ax.set_xlim(0,105)
    ax.set_ylabel('Words in Script (thousands)', fontsize=14)
    # ax.set_ylim(0, 200000)
    ax.get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x/1000))))
    ax.set_title('Scatter Plot of Ratings vs. # of Words', fontsize=20)
    # plt.show()
    plt.savefig('../images/scatterSCATTER')
    plt.close()
