import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def get_len(str):
    return len(str)


if __name__ == '__main__':

    s_df = pd.read_csv('../../data/scripts_df_II')
    s_df.dropna(inplace=True)
    s_df.rename(columns={'Unnamed: 0':'len'}, inplace=True)
    s_df['len'] = s_df['script'].apply(get_len)
    s_df = s_df.query('len > 10000')



    lem_df = pd.read_csv('../../data/lem_scr_df_III')
    lem_df = lem_df.query('scrplen > 1000')
    lem_df.drop(lem_df.loc[lem_df['scrplen']==117849].index, inplace=True)
    lem_df.drop(lem_df.loc[lem_df['scrplen']==95413].index, inplace=True)
    lem_df.drop(lem_df.loc[lem_df['scrplen']==78897].index, inplace=True)
    lem_df.to_csv('../../data/lem_scripts_IV')




    # scrp_list = lem_df['scrplen'].tolist()


    # fig, ax = plt.subplots()
    # ax.hist(s_df['len'], bins=20)
    # ax.set_xlabel('Script Length (words)', fontsize=14)
    # ax.set_ylabel('Movies', fontsize=14)
    # ax.set_title('Histogram of Movie Script Length', fontsize=20)
    # # plt.show()
    # plt.savefig('../../images/SCRPLENHIST')
    # plt.close()

    # fig, ax = plt.subplots()
    # ax.hist(s_df['len'], bins=20)
    # ax.set_xlabel('Script Length (words)', fontsize=14)
    # ax.set_ylabel('Movies', fontsize=14)
    # ax.set_title('Histogram of Movie Script Length', fontsize=20)
    # # plt.show()
    # plt.savefig('../../images/SCRPLENHISTALT')
    # plt.close()

    # fig, ax = plt.subplots()
    # ax.hist(lem_df['scrplen'], bins=20, color='m')
    # ax.set_xlabel('Script Length (tokens)', fontsize=14)
    # ax.set_ylabel('Movies', fontsize=14)
    # ax.set_title('Movie Script Length - Tokenized', fontsize=20)
    # # plt.show()
    # plt.savefig('../../images/LEMTOKENSHISTLENG')
    # plt.close()

    # fig, ax = plt.subplots()
    # ax.scatter(lem_df['rating'], lem_df['scrplen'], c='m')
    # ax.set_xlabel('Movie Rating', fontsize=14)
    # ax.set_xlim(0,105)
    # ax.set_ylabel('Tokens in Script', fontsize=14)
    # # ax.set_ylim(0, 200000)
    # # ax.get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x/1000))))
    # ax.set_title('Scatter Plot of Ratings vs. # of Tokens', fontsize=20)
    # # plt.show()
    # plt.savefig('../../images/SCATTERRATINGVSLENGTHWTOKENS')
    # plt.close()










# stop_words = ['look', 'man', 'int', 'ext', 'hand', 'come', 'day', 'turn', 'night',
# 'head',
#
# 'jack', 'david', 'elizabeth', 'frank', 'danny', 'kate', 'look', 'stephen',
# 'tom', 'bill',
#
# 'sam', 'chris', 'annie', 'mike', 'continue', 'look', 'lucy', 'eric',
# 'carl', 'cut',
#
# 'contd', 'continue', 'int', 'look', 'day', 'ext', 'eye', 'continuous',
#  'like', 'head',
#
#  'look', 'know', 'int', 'like', 'think', 'want', 'day', 'come',
#  'room', 'car',
#
#  'nick', 'alex', 'beth', 'sarah', 'tom', 'tony', 'look', 'kelly',
#  'int', 'adam',
#
#   'script', 'window', 'free', 'notice', 'stay', 'use', 'mike', 'john',
#  'bobby', 'ed',
#
#  'paul', 'ben', 'anna', 'annie', 'jim', 'ted', 'tom', 'graham',
#  'rachel', 'know',
#
#  'max', 'julie', 'billy', 'kate', 'annie', 'jackie', 'henry',
#   'eddie', 'luke', 'clay',
#
#   'harry', 'linda', 'joe', 'helen', 'int', 'thomas',
#    'david', 'day', 'look', 'night'
# ]
#
#
# '''
# movies_topic_0
# 192          World-is-not-Enough,-The
# 485                        Mummy,-The
# 246         1492-Conquest-of-Paradise
# 300                         Entrapmen
# 1018                   Les-Miserables
# 20                          Gladiator
# 1093    X-Files-Fight-the-Future,-The
# 398                             Mulan
# 1006                    Jurassic-Park
# 216                   Wild-Bunch,-The
#
# movies_topic_1
# 128                                   Fight-Club
# 431                                American,-The
# 1053                                    Croupier
# 381              Nightmare-Before-Christmas,-The
# 951                                     Oblivion
# 202                                          Roo
# 643                        Rise-of-the-Guardians
# 556     Pirates-of-the-Caribbean-Dead-Man's-Ches
# 507                                       Legend
# 722                                      Newsies
#
# movies_topic_2
# 901                     Moon
# 325     Machine-Gun-Preacher
# 797                    Ronin
# 62                 Lone-Star
# 730             Benny-&-Joon
# 1028       Dear-White-People
# 215                     Ghos
# 845                        S
# 828          Moonrise-Kingdo
# 582                  I-am-Sa
#
# movies_topic_3
# 1113                     Hitchcock
# 208       How-to-Train-Your-Dragon
# 413            Slumdog-Millionaire
# 295     How-to-Train-Your-Dragon-2
# 780                      Happy-Fee
# 138                 Ninja-Assassin
# 657                  Kung-Fu-Panda
# 573                     Ex-Machina
# 510                      Saving-Mr
# 1015                 Wrestler,-The
#
# movies_topic_4
# 129         Good-Will-Hunting
# 1037              Ghost-World
# 388           American-Hustle
# 311              Storytelling
# 858               Chasing-Amy
# 43                     Extrac
# 131                      Kids
# 459                      Juno
# 920              Cedar-Rapids
# 721     Margot-at-the-Wedding
#
# movies_topic_5
# 483           Youth-in-Revo
# 171              Black-Rain
# 61      Law-Abiding-Citizen
# 502      Living-in-Oblivion
# 1056      Great-Gatsby,-The
# 788                Zootopia
# 317        Deer-Hunter,-The
# 1036        Horrible-Bosses
# 256           Basic-Instinc
# 384                Godzilla
#
# movies_topic_6
# 530                    Stepmo
# 93              Almost-Famous
# 201                 Toy-Story
# 988         Jurassic-Park-III
# 536            Broadcast-News
# 987          Independence-Day
# 195                        12
# 865    Neverending-Story,-The
# 481                 Omega-Man
# 115          Punch-Drunk-Love
#
# movies_topic_7
# 407                        Buried
# 59                   Hotel-Rwanda
# 846               Green-Mile,-The
# 744       Kids-Are-All-Right,-The
# 336           Last-Tango-in-Paris
# 921    Happy-Birthday,-Wanda-June
# 611                          Dune
# 671     Six-Degrees-of-Separation
# 134                       Beloved
# 588                Big-White,-The
#
# movies_topic_8
# 244                            Pi
# 438                      Rushmore
# 980                     Max-Payne
# 579                   City-of-Joy
# 12                      Collatera
# 368    Mad-Max-2-The-Road-Warrior
# 545                 Burning-Annie
# 167                     Liar-Liar
# 931                   Sunset-Blvd
# 647                  Strange-Days
#
# 508     Something's-Gotta-Give
# 17           Lord-of-Illusions
# 710            Dumb-and-Dumber
# 824        Papadopoulos-&-Sons
# 870                 Armageddon
# 1024               Man-Trouble
# 754                  True-Lies
# 833                    Frances
# 855            Broken-Embraces
# 648        To-Sleep-with-Anger
# '''

topic_0
'contd', 'contd contd', 'okay', 'contd okay', 'v0'
Last-Tango-in-Paris, Heis, Iron-Lady,-The, Get-Ou, Men-Who-Stare-at-Goats,-The

topic_1
'20', '30', '10', '40', '18'
Ordinary-People, Hills-Have-Eyes,-The, Crazy,-Stupid,-Love, Shame, In-the-Loop

topic_2
'smile', 'glance', 'thank', 'happen', 'reach'
Changeling, Titanic, White-Christmas, Lone-Star, Dogma

topic_3
'165', '153', '176', '155', 'alans'
Bonfire-of-the-Vanities, Catch-Me-If-You-Can, TRON, Star-Trek-First-Contac, Darkman

topic_4
'huh', 'clothe', 'cmon', 'hesitate', 'manage'
Frances, Kafka, Shipping-News,-The, Boondock-Saints,-The, Ed-Wood

topic_5
'int', 'sit', 'like', 'good', 'come'
Cinema-Paradiso, Warrior, Hellraiser-Hellseeker, Inventing-the-Abbotts, Big-Eyes

topic_6
'charlies', 'tonys', 'jerrys', 'sober', 'charlies 81899'
So-I-Married-an-Axe-Murderer, Perks-of-Being-a-Wallflower,-The, Smashed, Mean-Streets, Station-Wes

topic_7
'joes', 'joes joes', 'yeh', 'jills', 'intday'
Looper, Super-8, Midnight-Cowboy, Mighty-Joe-Young, Program,-The

topic_8
'okay', 'uh', 'okay okay', 'shrug', 'jr'
Big, Ghostbusters-2, Edward-Scissorhands, Casino, American-Psycho

topic_9
'pauls', 'jims', 'teds', 'pauls pauls', 'annas'
Misery, Kids-Are-All-Right,-The, Big-White,-The, Dune, Manhattan-Murder-Mystery
