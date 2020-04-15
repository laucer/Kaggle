import pandas as pd
from typing import List, Tuple

from sklearn.model_selection import train_test_split

from test.data_cleaner import DataCleaner
from test.plots import Plots


class DatasetsLoader:

    @staticmethod
    def load_data(train_path, test_path) -> Tuple:
        train = pd.read_csv(train_path)
        test = pd.read_csv(test_path)
        train = train.dropna()  # TODO
        test = test.dropna()  # TODO

        Plots.plot_data(train, test)
        # DataCleaner.urls_to_url_text(train, test)
        datacleaner = DataCleaner()
        datacleaner.remove_not_important_words(train, test)


        x_train = train.selected_text
        y_train = train.sentiment
        y_train = y_train.apply(DatasetsLoader.map_to_values)

        x_test = test.text
        y_test = test.sentiment
        y_test = y_test.apply(DatasetsLoader.map_to_values)

        x_test, x_val, y_test, y_val = train_test_split(x_test, y_test, test_size=0.5, shuffle=True, stratify=y_test)

        return x_train, y_train, x_test, y_test, x_val, y_val

    @staticmethod
    def map_to_values(x: str) -> int:
        if x == 'positive':
            return 1
        if x == 'negative':
            return -1
        else:
            return 0
