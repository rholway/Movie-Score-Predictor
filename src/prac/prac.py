import pandas as pd
import numpy as np

df = pd.read_csv('../../data/lem_scripts_df')

stop_words = ['look', 'man', 'int', 'ext', 'hand', 'come', 'day', 'turn', 'night',
'head', 'jack', 'david', 'elizabeth', 'frank', 'danny', 'kate', 'look', 'stephen',
'tom', 'bill', 'sam', 'chris', 'annie', 'mike', 'continue', 'look', 'lucy', 'eric',
'carl', 'cut', 'contd', 'continue', 'int', 'look', 'day', 'ext', 'eye', 'continuous',
 'like', 'head', 'look', 'know', 'int', 'like', 'think', 'want', 'day', 'come',
 'room', 'car', 'nick', 'alex', 'beth', 'sarah', 'tom', 'tony', 'look', 'kelly',
 'int', 'adam', 'script', 'window', 'free', 'notice', 'stay', 'use', 'mike', 'john',
 'bobby', 'ed', 'paul', 'ben', 'anna', 'annie', 'jim', 'ted', 'tom', 'graham',
 'rachel', 'know', 'max', 'julie', 'billy', 'kate', 'annie', 'jackie', 'henry',
  'eddie', 'luke', 'clay', 'harry', 'linda', 'joe', 'helen', 'int', 'thomas',
   'david', 'day', 'look', 'night'

]
'''
movies_topic_0
192          World-is-not-Enough,-The
485                        Mummy,-The
246         1492-Conquest-of-Paradise
300                         Entrapmen
1018                   Les-Miserables
20                          Gladiator
1093    X-Files-Fight-the-Future,-The
398                             Mulan
1006                    Jurassic-Park
216                   Wild-Bunch,-The

movies_topic_1
128                                   Fight-Club
431                                American,-The
1053                                    Croupier
381              Nightmare-Before-Christmas,-The
951                                     Oblivion
202                                          Roo
643                        Rise-of-the-Guardians
556     Pirates-of-the-Caribbean-Dead-Man's-Ches
507                                       Legend
722                                      Newsies

movies_topic_2
901                     Moon
325     Machine-Gun-Preacher
797                    Ronin
62                 Lone-Star
730             Benny-&-Joon
1028       Dear-White-People
215                     Ghos
845                        S
828          Moonrise-Kingdo
582                  I-am-Sa

movies_topic_3
1113                     Hitchcock
208       How-to-Train-Your-Dragon
413            Slumdog-Millionaire
295     How-to-Train-Your-Dragon-2
780                      Happy-Fee
138                 Ninja-Assassin
657                  Kung-Fu-Panda
573                     Ex-Machina
510                      Saving-Mr
1015                 Wrestler,-The

movies_topic_4
129         Good-Will-Hunting
1037              Ghost-World
388           American-Hustle
311              Storytelling
858               Chasing-Amy
43                     Extrac
131                      Kids
459                      Juno
920              Cedar-Rapids
721     Margot-at-the-Wedding

movies_topic_5
483           Youth-in-Revo
171              Black-Rain
61      Law-Abiding-Citizen
502      Living-in-Oblivion
1056      Great-Gatsby,-The
788                Zootopia
317        Deer-Hunter,-The
1036        Horrible-Bosses
256           Basic-Instinc
384                Godzilla

movies_topic_6
530                    Stepmo
93              Almost-Famous
201                 Toy-Story
988         Jurassic-Park-III
536            Broadcast-News
987          Independence-Day
195                        12
865    Neverending-Story,-The
481                 Omega-Man
115          Punch-Drunk-Love

movies_topic_7
407                        Buried
59                   Hotel-Rwanda
846               Green-Mile,-The
744       Kids-Are-All-Right,-The
336           Last-Tango-in-Paris
921    Happy-Birthday,-Wanda-June
611                          Dune
671     Six-Degrees-of-Separation
134                       Beloved
588                Big-White,-The

movies_topic_8
244                            Pi
438                      Rushmore
980                     Max-Payne
579                   City-of-Joy
12                      Collatera
368    Mad-Max-2-The-Road-Warrior
545                 Burning-Annie
167                     Liar-Liar
931                   Sunset-Blvd
647                  Strange-Days

508     Something's-Gotta-Give
17           Lord-of-Illusions
710            Dumb-and-Dumber
824        Papadopoulos-&-Sons
870                 Armageddon
1024               Man-Trouble
754                  True-Lies
833                    Frances
855            Broken-Embraces
648        To-Sleep-with-Anger
'''
