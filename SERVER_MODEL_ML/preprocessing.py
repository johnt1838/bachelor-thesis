import pickle

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.pyplot import subplot
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.linear_model import RidgeCV
from sklearn.preprocessing import LabelEncoder
import constants as cc
import seaborn as sns

import os


def preprocess_dataframe(df, ):
    print('[Debug] preprocess_dataframe')
    # plt.figure(figsize=(10, 6))

    # drop Null / NaN
    df = df.dropna()
    # plt.figure(figsize=(10, 6))
    # sns.heatmap(df.isna().transpose(),
    #             cmap="YlGnBu",
    #             cbar_kws={'label': 'Missing Data'})
    # plt.savefig("visualizing_missing_data_before_fix.png", dpi=100)
    df = df.drop('id', inplace=False, axis=1)

    '''
        Encoding
    '''
    categorical_cols = data_to_encode(df)
    dict_of_encoders = create_dictionary_encoder(df, categorical_cols)
    df_encoded = label_encoding(df, dict_of_encoders, categorical_cols, True)
    '''----------------------------------------------------------------------------------'''



    # best_columns = feature_selection2(df_encoded)
    best_columns = feature_selection(df_encoded)
    best_columns.append('Diagnosis')
    all_features = df_encoded.columns.tolist()

    ''' drop bad features (columns) '''
    print(best_columns)
    for column in all_features:
        if column not in best_columns:
            df_encoded = df_encoded.drop(column, inplace=False, axis=1)


    # visualize
    # for count,column in enumerate(df_encoded.columns):
    #     sns.set(rc={"figure.figsize": (16, 10)})
    #     subplot(4, 5, count+1)
    #     ax = sns.boxplot(df_encoded[column])
    #
    #     plt.title(f'Distribution plot - {column}')
    #     sns.despine()
    # plt.tight_layout()
    # plt.savefig(cc.URL_IMAGES + f'boxplot_all_with_outliers.png')
    # plt.show()


    #-------------------------------------OUTLIERS---------------------------------------------------

    cols_todo = ['LOS', 'PsychotropicMedications' ]
    for column in cols_todo:
        qua10 = df_encoded[column].quantile(0.25)
        qua90 = df_encoded[column].quantile(0.75)
        df_encoded[column] = np.where(df_encoded[column] < qua10, qua10, df_encoded[column])
        df_encoded[column] = np.where(df_encoded[column] > qua90, qua90, df_encoded[column])
        print(df_encoded[column].skew())










    #-------------------------------------OUTLIERS---------------------------------------------------
    # visualize
    # for count, column in enumerate(df_encoded.columns):
    #     sns.set(rc={"figure.figsize": (16, 10)})
    #     subplot(4, 5, count + 1)
    #     ax = sns.boxplot(df_encoded[column])
    #
    #     plt.title(f'Distribution plot - {column}')
    #     sns.despine()
    # plt.tight_layout()
    # plt.savefig(cc.URL_IMAGES + f'boxplot_all_without_outliers.png')
    # plt.show()


    # trimming meds one by one


    #-------------------------

    with pd.option_context('display.max_rows', None,
                           'display.max_columns', None,
                           'display.precision', 3,
                           ):
        print(df_encoded.describe())
    #

    with pd.option_context('display.max_rows', None,
                           'display.max_columns', None,
                           'display.precision', 3,
                           ):
        print(df_encoded.describe())
    return df_encoded,best_columns


def feature_selection(data):
    features_best = []
    categorical_columns = []
    num_features_max = 35
    numerics = ['int8', 'int16', 'int32',
                'int64', 'float16', 'float32',
                'float64']
    features = data.columns.values.tolist()
    for col in features:
        if data[col].dtype in numerics: continue
        categorical_columns.append(col)

    train = data.drop(['Diagnosis'], axis=1)
    target = data['Diagnosis']

    bestfeatures = SelectKBest(score_func=chi2, k='all')
    fit = bestfeatures.fit(train, target)
    dfscores = pd.DataFrame(fit.scores_)
    dfcolumns = pd.DataFrame(train.columns)

    # concat two dataframes for better visualization
    featureScores = pd.concat([dfcolumns, dfscores], axis=1)
    featureScores.columns = ['Feature', 'Score']  # naming the dataframe columns
    features_best.append(featureScores.nlargest(num_features_max, 'Score')['Feature'].tolist())
    x = featureScores.nlargest(18, 'Score')
    print(x)
    # ####
    # indices = np.argsort(bestfeatures.scores_)[::-1]
    # features = []
    # for i in range(18):
    #     features.append(train.columns[indices[i]])
    #
    # fig, ax = plt.subplots(figsize=(20,10))
    #
    # sns.barplot(x=features, y=bestfeatures.scores_[indices[range(18)]],\
    # label="Importtant Categorical Features", palette=("Blues_d"),ax=ax).\
    # set_title('Categorical Features Importance')
    #
    # ax.set(xlabel="Columns", ylabel = "Importance")
    # plt.show()
    #
    # ####


    best_features = x['Feature'].unique().tolist()
    return best_features


# Encoding
def data_to_encode(df):
    """
            Takes a dataframe and return the columns that are non numeric (categorical)
    """

    categorical_columns = []
    numerics = ['int8', 'int16', 'int32', 'int64', 'float16', 'float32', 'float64']
    features = df.columns.values.tolist()
    for col in features:
        if df[col].dtype in numerics: continue
        categorical_columns.append(col)

    return categorical_columns


def create_dictionary_encoder(df, columns_to_encode):
    """
          Gets an array of specified columns to be a dictionary of encoders
    """
    dictionary_of_encoders = {}
    for col in columns_to_encode:
        dictionary_of_encoders[col] = LabelEncoder().fit(df[col])

    with open('encoder_dict.pickle', 'wb') as handle:
        pickle.dump(dictionary_of_encoders, handle, protocol=pickle.HIGHEST_PROTOCOL)
    return dictionary_of_encoders


def label_encoding(df, dictionary_of_encoders, categorical_columns, save=False):
    """
            Dataset non numerics classes to numerics
    """
    for column in categorical_columns:
        df[column] = dictionary_of_encoders[column].transform(df[column])
    if save:
        save_url = 'api_dataset_encoded.csv'
        saving = df.to_csv(save_url, index=False)
    return df


def label_decoding(df, dictionary_of_encoders, categorical_columns):
    """
         Dataset's column class numeric back to non numeric
    """
    for col in categorical_columns:
        df[col] = dictionary_of_encoders[col].inverse_transform(df[col])

    return df
