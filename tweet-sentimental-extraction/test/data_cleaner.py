from typing import Tuple

import pandas as pd
from nltk import word_tokenize
from nltk.corpus import stopwords


class DataCleaner:

    def __init__(self) -> None:
        self.stopwords = set(stopwords.words('english'))

        # TODO

    def urls_to_url_text(train: pd.DataFrame, test: pd.DataFrame) -> Tuple:
        urls_number = train['text'].str.count('http|www.').sum()
        print(f'Number of urls before cleaning in train: {urls_number}')

        urls_number = test['text'].str.count('http|www.').sum()
        print(f'Number of urls before cleaning in test: {urls_number}')

        train = train['text'].replace('http|www', 'url', regex=True)
        test = test['text'].replace('http|www', 'url', regex=True)

        urls_number = train['text'].str.count('http|www.').sum()
        print(f'Number of urls after cleaning in train: {urls_number}')

        urls_number = test['text'].str.count('http|www.').sum()
        print(f'Number of urls after cleaning in test: {urls_number}')

    def remove_not_important_words(self, train: pd.DataFrame, test: pd.DataFrame) -> Tuple:
        test['text'].apply(self.remove_not_important_words_from_tweet)

    def remove_not_important_words_from_tweet(self, tweet: str):
        tweet = tweet.lower()
        tweet = word_tokenize(tweet)
        return 'a'
        # return [word for word in tweet if word not in self.stopwords]

