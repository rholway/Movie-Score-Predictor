# So You Think You Can Write...A Movie

#### Question/Project: Can we predict the Rotten Tomato score of a movie by running an algorithm on the movie script?

The idea of this project is to take a movie script, and before the script gets read, or put into production, try to predict what the Rotten Tomato Score of the movie will be.

Rather than starting with the entire script, plot summaries of movies were used at first, to make the process less computationally expensive.  Average plots were 628 characters long (minimum: 112, maximum: 2,826), so it would be very difficult to find signal from such a small character size.

Hopefully, once the algorithm is up and running, it can be used to train on full movie scripts, and be able to find signal.

#### Data
A data frame was created of movie titles, plot summaries, and Rotten Tomato scores.  The OMDb API was used to gather data.

| Movie Title        | Plot Summary          | RT%  |
| ------------- |:-------------:| -----:|
| The Wolf of Wall Street     | Jordan Belfort is a Long Island penny stockbro... | 78.0 |

1,096 Movies

![Hist of Movies - Plots](images/hist-of-movie-ratings-plots.png)

#### Tokenize Plot Summaries

Strip all punctuation and unicode from plot summaries, then use spaCy to lemmatize words to tokens.  Make all tokens lower case, and remove all stop words.

| Movie Title        | Plot Summary          |
| ------------- |:-------------:| -----:|
| 'Jordan Belfort is a Long Island penny stockbroker who served 22 months in prison for defrauding investors in a massive 1990s securities scam that involved widespread corruption on Wall Street and in the corporate banking world, including shoe designer Steve Madden.'     | 'jordan belfort long island penny stockbroker serve 22 month prison defraud investor massive 1990s security scam involve widespread corruption wall street corporate banking world include shoe designer steve madden' | 

#### TF-IDF
