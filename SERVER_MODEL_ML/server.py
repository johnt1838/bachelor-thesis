import pickle

import numpy as np
import pandas as pd
import requests
from matplotlib.pyplot import subplot
from sklearn import metrics
from scipy.special import expit
# Custom
import sklearn
from matplotlib.colors import ListedColormap
from matplotlib import pyplot as plt
from sklearn.compose import make_column_transformer
from sklearn.ensemble import VotingClassifier
from sklearn.inspection import DecisionBoundaryDisplay
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler, MinMaxScaler
import seaborn as sns

import constants as cc
import preprocessing as pp


def init_server():
    print("[DEBUG]: INIT SERVER\n")

    json_data = get_data()
    link = json_to_csv(json_data)
    df = pd.read_csv(link)
    df_preprocessed, num_columns = pp.preprocess_dataframe(df)
    num_columns.remove('Diagnosis')  # target pop
    model = create_model(df_preprocessed, num_columns)
    pickle.dump(model, open('final_model.pickle', 'wb'))


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


def optimal_k(data, num_columns):
    X = data.drop('Diagnosis', axis=1)
    y = data['Diagnosis']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=0)

    ct = make_column_transformer(
        # (MinMaxScaler(), num_columns),
        (StandardScaler(), num_columns),
        remainder='passthrough'
    )
    acc = []
    k_range = range(1, 100)

    for i in k_range:
        neigh = KNeighborsClassifier(n_neighbors=i, p=1).fit(X_train, y_train)
        yhat = neigh.predict(X_test)
        acc.append(metrics.accuracy_score(y_test, yhat))

    # plt.plot(k_range, acc)
    # plt.xlabel('Value of K for KNN')
    # plt.ylabel('Testing Accuracy')
    # plt.show()
    print('THIS IS THE BEST max', max(acc))
    print(acc)
    return acc.index(max(acc))


def create_model(data, num_columns):
    print('Running KNN')
    X = data.drop('Diagnosis', axis=1)
    y = data['Diagnosis']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=0)  # 42

    ct = make_column_transformer(
        # (MinMaxScaler(), num_columns),
        (StandardScaler(), num_columns),
        remainder='passthrough'
    )

    X_train = ct.fit_transform(X_train)
    X_test = ct.transform(X_test)


    k_s = optimal_k(data, num_columns)
    print('THIS IS K_S', k_s)
    knn = KNeighborsClassifier(n_neighbors=k_s, p=1)
    knn.fit(X_train, y_train)
    ypred = knn.predict(X_test)
    # ----------------------------------------------------------------------------
    print('KNN: {:.2f}%'.format(accuracy_score(y_test, ypred)))


    ## visualize
    print(X)
    # plt.figure()
    # plot_decision_boundaries(X_train, y_train, KNeighborsClassifier)
    # plt.show()

    ##------------------------------------------------

    # print('Running DecisionTreeClassifier')
    # decision_tree = DecisionTreeClassifier(criterion='entropy', min_samples_leaf=7)
    # decision_tree.fit(X_train, y_train)
    # print('Decision Tree: {:.2f}%'.format(cross_val_score(decision_tree, X, y, cv=50).mean() * 100))

    # ---------------------------------------------------------------------------------------

    print('Logistic Regression Model')
    X = data.drop('Diagnosis', axis=1)
    y = data['Diagnosis']

    print(X.columns)



    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=0)

    ln = LogisticRegression(solver='liblinear', penalty='l2')
    ln.fit(X_train, y_train)
    ypred = ln.predict(X_test)
    ###--------------------
    for count,column in enumerate(X.columns):
        sns.set(rc={"figure.figsize": (16, 10)})
        subplot(4, 5, count + 1)
        sns.regplot(x=column,
                    y='Diagnosis',
                    data=data)
        plt.title(f'Logistic Regression curve - {column}')

    plt.tight_layout()
    plt.savefig(cc.URL_IMAGES + f'all_curves_regression_model.png')
    plt.show()


    ###--------------------
    print('Logistic Regression: {:.2f}%'.format(accuracy_score(y_test, ypred)))

    # ---------------------------------------------------------------------------------------

    print('Ensenble Model')
    voting_ens = VotingClassifier(estimators=[('knn', knn), ('ln', ln)], voting='soft')

    # Fit and predict with the models and ensemble
    for clf in (knn, ln, voting_ens):
        clf.fit(X_train, y_train)
        pickle.dump(clf, open('ensemble.pickle', 'wb'))
        y_pred = clf.predict(X_test)

        print(clf.__class__.__name__, accuracy_score(y_test, y_pred))
        # print(clf.__class__.__name__, cross_val_score(clf, X, y, cv=5).mean()*100)

    return voting_ens


def plot_decision_boundaries(X, y, model_class, **model_params):
    """
    Function to plot the decision boundaries of a classification model.
    This uses just the first two columns of the data for fitting
    the model as we need to find the predicted value for every point in
    scatter plot.
    Arguments:
            X: Feature data as a NumPy-type array.
            y: Label data as a NumPy-type array.
            model_class: A Scikit-learn ML estimator class
            e.g. GaussianNB (imported from sklearn.naive_bayes) or
            LogisticRegression (imported from sklearn.linear_model)
            **model_params: Model parameters to be passed on to the ML estimator

    Typical code example:
            plt.figure()
            plt.title("KNN decision boundary with neighbros: 5",fontsize=16)
            plot_decision_boundaries(X_train,y_train,KNeighborsClassifier,n_neighbors=5)
            plt.show()
    """
    try:
        X = np.array(X)
        y = np.array(y).flatten()
    except:
        print("Coercing input data to NumPy arrays failed")
    # Reduces to the first two columns of data
    # reduced_data = X[:, :2]
    reduced_data = X[:, (0,2)]
    print(reduced_data)
    # Instantiate the model object
    model = model_class(**model_params)
    # Fits the model with the reduced data
    model.fit(reduced_data, y)

    # Step size of the mesh. Decrease to increase the quality of the VQ.
    h = .02  # point in the mesh [x_min, m_max]x[y_min, y_max].

    # Plot the decision boundary. For that, we will assign a color to each
    x_min, x_max = reduced_data[:, 0].min() - 1, reduced_data[:, 0].max() + 1
    y_min, y_max = reduced_data[:, ].min() - 1, reduced_data[:, 1].max() + 1
    # Meshgrid creation
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))

    # Obtain labels for each point in mesh using the model.
    Z = model.predict(np.c_[xx.ravel(), yy.ravel()])

    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 2].min() - 1, X[:, 2].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.1),
                         np.arange(y_min, y_max, 0.1))

    # Predictions to obtain the classification results
    Z = model.predict(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)

    # Plotting
    plt.contourf(xx, yy, Z, alpha=0.4)
    plt.scatter(X[:, 0], X[:, 2], c=y, alpha=1)
    plt.xlabel("Feature-1", fontsize=18)
    plt.ylabel("Feature-2", fontsize=18)
    plt.xticks(fontsize=17)
    plt.yticks(fontsize=17)
    return plt


