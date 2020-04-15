from collections import Counter

import pandas as pd
import matplotlib.pyplot as plt


class Plots:

    @staticmethod
    def plot_data(train: pd.DataFrame, test: pd.DataFrame) -> None:
        Plots.plot_lengths(train, 'Lengths of tweets in train dataset unmodified data')
        Plots.plot_lengths(test, 'Lengths of tweets in test dataset unmodified data')
        Plots.plot_most_popular_words(train, "Most popular 30 words for train unmodified data")
        Plots.plot_most_popular_words(test, "Most popular 30 words for test unmodified data")


    @staticmethod
    def plot_lengths(data: pd.DataFrame, title: str) -> None:
        lenghts = data['text'].str.len().value_counts()
        plt.boxplot(lenghts)
        plt.title(title)
        plt.show()

    @staticmethod
    def plot_most_popular_words(data: pd.DataFrame, title: str) -> None:
        most_popular_words = data['text'].str.split(expand=True).stack().value_counts()[:30]
        most_popular_words.plot.bar(x=0, y=1)
        plt.title(title)
        plt.show()
