import pandas as pd
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.preprocessing import LabelEncoder
from featurewiz import featurewiz


def preprocess_dataframe(df):
    print('[Debug] preprocess_dataframe')
    # drop Null / NaN
    df = df.dropna()
    df = df.drop('id', inplace=False, axis=1)

    categorical_cols = data_to_encode(df)
    dict_of_encoders = create_dictionary_encoder(df, categorical_cols)

    df_encoded = label_encoding(df, dict_of_encoders, categorical_cols, True)

    best_columns = feature_selection(df_encoded)
    best_columns.append('Diagnosis')
    all_features = df_encoded.columns.tolist()
    print(all_features)
    for column in all_features:
        print(column)
        if column not in best_columns:
            print(f'{column} dropped')
            df_encoded = df_encoded.drop(column, inplace=False, axis=1)

    # featurewiz
    # df_encoded = feature_selection_featurewiz(df_encoded)

    return df_encoded


def feature_selection(data):
    print('[DEBUG] feature_selection')
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
    x = featureScores.nlargest(20, 'Score')

    best_features = x['Feature'].unique().tolist()
    return best_features


def feature_selection_featurewiz(data):
    print('[DEBUG]- FEATURE WIZ')
    features = featurewiz(data, target='Diagnosis', corr_limit=0.70,
                          verbose=2)
    print(type(features))


# Encoding
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
