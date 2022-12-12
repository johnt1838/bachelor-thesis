import os
import pickle

from sklearn.compose import make_column_transformer
from sklearn.preprocessing import StandardScaler

from preprocessing import label_encoding
import time
import pandas as pd
import requests
import constants as cc

columns_ = ['MD', 'EMR', 'LOS', 'A', 'C', 'D', 'F', 'G', 'K', 'L', 'M', 'O', 'P',
          'R', 'Y', 'Z', 'AA', 'PsychotropicMedications']
def test_model(model):
    '''
        Test created Model, for new data set
        Endpoint: http://127.0.0.1:8000/data/patient_entries_test/
    '''

    print('Running Model')

    # using ecoder
    with open('encoder_dict.pickle', 'rb') as handle:
        encode_dict = pickle.load(handle)

    req = requests.get(cc.URL_RAW_DATA_TEST, headers= cc.HEADERS)
    json_ = req.json()
    # print(json_['results'])

    datat = pd.DataFrame.from_records(json_['results'])
    # print(datat)

    for column in datat.columns:
        # print(column)
        if column == 'Diagnosis':
            continue
        if column not in columns_:
            datat = datat.drop(column, axis=1)

    # print(datat.columns)



    categorical_columns = []
    numerics = ['int8', 'int16', 'int32', 'int64', 'float16', 'float32', 'float64']
    features = datat.columns.values.tolist()
    for col in features:
        if datat[col].dtype in numerics: continue
        categorical_columns.append(col)

    dict_of_encoders = pickle.load(open('encoder_dict.pickle', 'rb'))
    data_encoded = label_encoding(datat, dict_of_encoders, categorical_columns, True)

    # print(data_encoded)



    X_test = data_encoded.drop('Diagnosis', axis=1)
    Y_test = data_encoded['Diagnosis']



    # load the model from disk
    ensemble_model = pickle.load(open('ensemble.pickle', 'rb'))
    ensemble_model.fit(X_test, Y_test)
    y_pred = model.predict_proba(X_test)
    # print(y_pred)

    from datetime import datetime

    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")



    for id, entry in enumerate(y_pred):
        if entry[0] > entry[1]:
            print(f'[{current_time}]-Patient with ID:{id} has {entry[0]*100:.2f}% Probability of occurrence of symptoms (MDD, Recurrent) ')
        else:
            print(f'[{current_time}]-Patient with ID:{id} has {entry[1]*100:.2f}% Probability of occurrence of symptoms (MDD, Single Episode) ')
        time.sleep(3)


















