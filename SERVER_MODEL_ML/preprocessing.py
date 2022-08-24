import pandas as pd
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.preprocessing import LabelEncoder
from featurewiz import featurewiz


def preprocess_dataframe(df):
    # drop Null / NaN
    df = df.dropna()

    categorical_cols = data_to_encode(df)
    dict_of_encoders = create_dictionary_encoder(df, categorical_cols)

    df_encoded = label_encoding(df, dict_of_encoders, categorical_cols, True)
    print('\n\n\n THis is it \n\n')
    print(df_encoded)
    feature_selection(df_encoded)

    # feature_selection(df)


def feature_selection(data):
    features_best = []
    categorical_columns = []
    num_features_max = 35
    numerics = ['int8', 'int16', 'int32', 'int64', 'float16', 'float32', 'float64']
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
    print(featureScores.nlargest(len(dfcolumns), 'Score'))


def feature_selection_featurewiz(data):
    target = 'Diagnosis'
    features, train = featurewiz(data, target, corr_limit=0.7, verbose=2, sep=',', header=0, test_data="",
                                 feature_engg="", category_encoders="")

def data_to_encode(df):
    """
            Takes a dataframe and return the columns that are non numeric (categorical)
    """
    print("[data_to_be_encoded]\n")

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
