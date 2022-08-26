import pickle
import copy

import pandas as pd
import requests
# Custom
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

import constants as cc
import preprocessing as pp


def init_server():
    print("[DEBUG]: INIT SERVER\n")

    json_data = get_data()
    link = json_to_csv(json_data)
    df = pd.read_csv(link)
    df_preprocessed = pp.preprocess_dataframe(df)

    model = create_model(df_preprocessed)


def get_data():
    """
        Getting data from raw api in JSON format.
    """

    links = [cc.URL_RAW_DATA]
    request = requests.get(cc.URL_RAW_DATA,
                           headers=cc.HEADERS)
    json_ = request.json()
    while json_['next'] is not None:
        links.append(json_['next'])
        json_ = requests.get(json_['next']).json()

    bigJson = {'results': []}
    for link in links:
        request = requests.get(link,
                               headers=cc.HEADERS)
        json_data = request.json()
        for data_line in json_data['results']:
            # print(data_line)
            # bigJson.update(data_line)
            bigJson['results'].append(data_line)
    return bigJson


def json_to_csv(json_data):
    link = "api_dataset.csv"
    columns = list(json_data['results'][0].keys())

    f = open(link, "w")
    # 1st line columns
    i = 1
    for column in columns:
        if i != len(columns):
            f.write(column)
            f.write(',')
            i += 1
        else:
            f.write(column)
            f.write('\n')

    for line in json_data['results']:
        for index_, col in enumerate(columns):
            if col == 'Diagnosis':
                f.write('\"{}\"'.format(str(line[f'{col}'])))
            else:
                f.write(str(line[f'{col}']))
            if index_ != len(columns) - 1:
                f.write(',')
        f.write('\n')
    return link


def create_model(data):
    print('\n Model Logistic regression - Output probability')
    print(data.columns.values)

    X = data.drop(['Diagnosis'], axis=1)
    y = data['Diagnosis']
    scaler = StandardScaler()
    X = scaler.fit_transform(X)
    # X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1)
    max_ = 0.3
    best_ln = LogisticRegression()
    for iter in range(1, 100):
        for random in range(1, 10):
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1)  # 70% training and 30% test
            ln = LogisticRegression(penalty='l1', solver='liblinear', random_state=random)
            ln.fit(X, y)
            y_pred = ln.predict(X_test)

            if accuracy_score(y_test, y_pred) >= max_:
                print('Accuracy', accuracy_score(y_test, y_pred))
                max_ = accuracy_score(y_test, y_pred)
                best_ln = ln
                best_ln.fit(X,y)



    y_pred = best_ln.predict(X_test)
    print(accuracy_score(y_test, y_pred))
    #
    # train_yhat = best_ln.predict(X_train)
    # train_acc = accuracy_score(y_train, train_yhat)
    #
    # # evaluate on the test dataset
    # test_yhat = best_ln.predict(X_test)
    # test_acc = accuracy_score(y_test, test_yhat)
    #
    #
    # # summarize progress
    # print(train_acc, test_acc)

    return best_ln
