# So You Think You Can Write...A Movie

### Question/Project: Can we predict the Rotten Tomato score of a movie by running an algorithm on the movie script?

The idea of this project is to take a movie script, and before the script gets read, or put into production, try to predict what the Rotten Tomato Score of the movie will be.

Rather than starting with the entire script, plot summaries of movies were used at first, to make the process less computationally expensive.  Average plots were 628 characters long (minimum: 112, maximum: 2,826), so it would be very difficult to find signal from such a small character size.

Hopefully, once the algorithm is up and running, it can be used to train on full movie scripts, and be able to find signal.

### Data
A data frame was created of movie titles, plot summaries, and Rotten Tomato scores.  The OMDb API was used to gather data.

| Movie Title        | Plot Summary          | RT%  |
| ------------- |:-------------:| -----:|
| The Wolf of Wall Street     | Jordan Belfort is a Long Island penny stockbro... | 78.0 |

1,096 Movies

![Hist of Movies - Plots](images/hist-of-movie-ratings-plots.png)

### Tokenize Plot Summaries

Strip all punctuation and unicode from plot summaries, then use spaCy to lemmatize words to tokens.  Make all tokens lower case, and remove all stop words.

Before  | After
------------- | -------------
'Jordan Belfort is a Long Island penny stockbroker who served 22 months in prison for defrauding investors in a massive 1990s securities scam that involved widespread corruption on Wall Street and in the corporate banking world, including shoe designer Steve Madden.'  | 'jordan belfort long island penny stockbroker serve 22 month prison defraud investor massive 1990s security scam involve widespread corruption wall street corporate banking world include shoe designer steve madden'



### TF-IDF

Create a term frequency-inverse document frequency (tf-idf) of the full corpus, training corpus and test corpus. (Don't use the test set to build your training feature matrix, or you are using the test set to help build your model).  Only use tf-idf of training corpus and test corpus to build and evaluate model.

title  | token 0  | token 1  | token 2
-------- | ----| ----| -----
movie 1  | 0.0 | 0.4 | 0.1
movie 2  | 0.5 | 0.0 | 0.04

Use L2 norm to normalize term frequency.  This will account for different size documents.  Use idf to account for dominant terms across documents (if some terms are used frequently across multiple documents, the inverse will make the words less important, rather than more important).  The maximum features for these tf-idfs were 5,000, and ngram_range was (1,2)

### Naive Bayes

Created a binary classification model using Naive Bayes.  Scores greater than 75% classified as 1 (540 of 1096 movies), and scores 75% or lower classified as 0 (556 of 1096 movies).

Naive Bayes predicted the classification of a movie (whether it was greater than 75% or 75% or less based on Rotten Tomatoes scores) based on the tf-idf of the plot with 56% accuracy.  Not very good.  Difficult to find signal in only the plots.

### Non-Negative Matrix Factorization

Using NMF, we are able to reduce dimensions of the tf-idf based on how many 'topics' (k) we want to group our features into.  In an attempt to find a representative value for k, we create an elbow plot.

![NMF Elbow Plot - Plots](images/plots-elbow-plot.png)

There is no distinguishable 'elbow' here, so 10 was chosen arbitrarily.  This may be expected, because we did not expect to find much signal in the data from only reviewing plot summaries.

#### What are the tokens and movies in the topics in the full corpus?

topic number  | top 5 tokens  | top 5 titles
------------- | ------------- | -------------
0  | life, friend, good, woman, work  |  500 Days of Summer, The Family Man, Chasing Amy, Final Destination 2, The Back-up Plan
1  | world, war, evil, force, army  |  The Lord of the Rings: The Return of the King, Hellboy, Hellboy II: The Golden Army, Rise of the Guardians, Blade Trinity
2  | york, new york, new, city, york city  |  The Siege, A Most Violent Year, Taxi Driver, Phone Booth, New York Minute
3  | murder, killer, detective, police, kill  | Mr. Brooks, Jennifer 8, The Crow: Salvation, Insomnia, Manhunter
4  | town, small, small town, local, creature  |  Tremors, Mr. Deeds Goes to Town, I Am Number Four, Mumford, Super 8
5  | alien, earth, mission, ship, human  |  Alien: Resurrection, Star Trek: The Motion Picture, Alien 3, Independence Day, The Day the Earth Stood Still
6  | school, high, high school, student, teacher  | One Eight Seven, Cherry Falls, 17 Again, Easy A, Ferris Bueller's Day Off
7  | family, son, father, daughter, child  |  August: Osage County, Wanted, Blow, War of the Worlds, Magnolia
8  | story, true, true story, base tell  |  Grand Theft Parsons, Memento, The Elephant Man, Rush, Heavenly Creatures
9  | drug, agent, money, nick, gang  |  Sicario, Ocean's Twelve, Midnight Express, Deep Cover, Confidence
<!--
#### What are the tokens in training vs. testing data?

topic number  | Train - top 5 tokens  | Test - top 5 titles
------------- | --------------------- | --------------------
0  | life, friend, love, work, good  |  chris, death, rose, weekend, island
1  | alien, earth, ship, space, mission  |  earth, mission, alien, find, planet
2  | murder, kill, killer, drug, police  |  new york, york, new, york city, live
3  | new york, york, new, city, york city  | school, high school, high, scarlet, lose
4  | war, world, vampire, evil, join  |  think, marry, good, friend, good friend
5  | family, son, father, daughter, child  |  jenny, alien, matrix, husband, david
6  | town, small, boy, small town, young  | world, detective, crime, force, man
7  | school, high, high school, student, teacher |  Tremors, Mr. Deeds Goes to Town, Mumford, Super 8, Silver Bullet
8  | jack, casino, elizabeth, strike, capitan  |  vegas, las, las vegas, sex, ben
9  | story, time, true tell, true story  |  story, life, true, frank, meet -->

### Regression Models

Performed train-test split on data.  Then created train tfidf and test tfidf.  Used Rotten Tomato ratings as targets.  The following are 10-fold cross validation scores.

Model  | MSE  | R2
------ | ---- | -----
AdaBoost Regressor  | 682.33  |  -0.094
Gradient Boosting Regressor  | 658.51  |  -0.064
Random Forest Regressor  | 815.22  |  -0.299

Pretty bad scores of the models trying to predict Rotten Tomato scores based on movie plot tf-idfs

Best model was Gradient Boosting Regressor

#### Learning Rate 0.1
![Training vs Test data - GBR - Plots](images/plot_gdbr_lr0.1.png)

#### Learning Rate 1.0
![Training vs Test data - GBR - Plots](images/plot_gdbr_lr1.png)
