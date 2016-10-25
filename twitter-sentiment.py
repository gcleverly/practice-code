# Classifies tweets on whether they are negative or positive

import pandas as pd

get_ipython().magic('matplotlib inline')

tweets_df = pd.read_csv('../datasets/tweet_data.csv', sep=';',
                        index_col=0)
tweets_df.head()

tweets_df['is_positive'] = tweets_df['polarity'].replace(4, 1)

tweets_df[tweets_df['polarity'] > 0]
tweets_df['is_positive'].unique()

from sklearn.feature_extraction.text import CountVectorizer

train_tweets = tweets_df['tweet'].values

# initializes the vectorizer:
#    English stop words & convert words to lowercase
vectorizer = CountVectorizer(stop_words='english',
                             ngram_range=(1, 1),  # Unigrams+Bigrams
                             lowercase=True)

# create list of unique words (ie the vocabulary)
vectorizer.fit(train_tweets)

# for each string of text,
#   counts how many of each word in the vocab there is
X_train = vectorizer.transform(train_tweets)

print(train_tweets[186])
print(X_train[186])
print(vectorizer.vocabulary_.get('phone'))
X_train.shape

from sklearn.feature_extraction.text import TfidfTransformer

transformer = TfidfTransformer()
transformer.fit(X_train)

X_train_tfidf = transformer.transform(X_train)

print(train_tweets[36])
print(X_train_tfidf[36])
print(vectorizer.vocabulary_.get('ugh'))

y = tweets_df['polarity'].values

[tweet for tweet in train_tweets if '!!!' in tweet.lower()]
print(set(y))

X = X_train_tfidf.toarray()  # converts sparse matrix -> ndarray
y = tweets_df['is_positive'].values
print(X.shape, y.shape)
print(X)

from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.cross_validation import cross_val_score

logreg = LogisticRegression(C=1000)
logreg.fit(X, y)

print(cross_val_score(logreg, X, y, cv=3))
print(logreg.coef_.min(), logreg.coef_.max())
print(logreg.coef_[0][5087])  # woo - should have pos sentiment
print(logreg.coef_[0][4809])  # ugh - should have neg sentiment

nb = MultinomialNB()
nb.fit(X, y)

cross_val_score(nb, X, y, cv=3)

sentence = ["I'm crying because it's gloomy out."]  # only 'crying' is in our model
sentence = ["My homework is done!"]
sentence_counts = vectorizer.transform(sentence)
sentence_tfidf = transformer.transform(sentence_counts)
logreg.predict(sentence_tfidf.toarray())
print(logreg.predict_proba(sentence_tfidf.toarray()))

print(vectorizer.vocabulary_.get('homework'))
print(logreg.coef_[0][2242])
print(vectorizer.vocabulary_)
