import pandas as pd
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.preprocessing import LabelEncoder


def preprocess_dataframe(df):
    # drop Null / NaN
    df = df.dropna()

    categorical_cols = data_to_encode(df)

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


def create_dictionary_encoder(df, columns_to_encode, col):
    """
          Gets an array of specified columns to be a dictionary of encoders
    """
    dictionary_of_encoders = {}
    for col in columns_to_encode:
        dictionary_of_encoders[col] = LabelEncoder().fit(df[col])
    return dictionary_of_encoders


def label_encoding(df, dictionary_of_encoders, categorical_columns, save=False):
    for column in categorical_columns:
        df[column] = dictionary_of_encoders[column].transform(df[column])

    if save:
        save_url = 'api_dataset_encoded.csv'
        saving = df.to_csv(save_url, index=False)

