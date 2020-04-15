# from datasets_loader
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

from test.datasets_loader import DatasetsLoader

x_train, y_train, x_test, y_test, x_val, y_val = DatasetsLoader.load_data(
    '/home/lucjan/PycharmProjects/kaggle/tweet-sentimental-extraction/data/train.csv',
    '/home/lucjan/PycharmProjects/kaggle/tweet-sentimental-extraction/data/test.csv')


tokenization = TfidfVectorizer(max_features=3000)
tokenization.fit(x_train)



# vectorizer = CountVectorizer()

# classifier = XGBClassifier()
# vectorizer.set_params(max_features=500)
# pipeline = Pipeline([
# ('vectorizer', vectorizer),
# ('classifier', classifier)
# ])
# pipeline.fit(x_train, y_train)
# y_pred = cross_val_predict(pipeline, x_val, y_val, cv=3)
# conf_mat = confusion_matrix(y_val, y_pred)
#
#
# csv = 'term_freq_df.csv'
