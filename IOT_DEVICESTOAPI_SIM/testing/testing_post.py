'''Testing File'''

import pandas as pd
import requests
import json

# CUSTOM
import consts as cc


def post_10(df):
    print('working')
    pd.set_option('display.max_rows', None)
    # df = df.iloc[:10, :]

    df = df.iloc[[0, 96]]
    print(df)
    # r = requests.get(url=cc.URL_RAW,headers=cc.HEADERS_POST)

    # print(r.status_code)
    # json = r.json()
    # print(json)
    # if r.status_code == 200:
    #     for index, row in df.iterrows():
    #         print(f'{index=}')
    #         data_json_post = {
    #             "Gender": row['GENDER'],
    #             "Age":row['AGE'] ,
    #             "Race": row['RACE_ETHNICITY'],
    #             "Diagnosis": row['Diagnosis'],
    #             "MD": row['MD'],
    #             "Assignment": row['Assignment'],
    #             "EMR": row['EMR'],
    #             "LOS": row['LOS'] ,
    #             "RAR": row['RAR'],
    #             "A": row['A'],
    #             "B": row['B'],
    #             "C": row['C'],
    #             "D": row['D'],
    #             "E": row['E'],
    #             "F": row['F'],
    #             "G": row['G'],
    #             "H": row['H'],
    #             "I": row['I'],
    #             "J": row['J'],
    #             "K": row['K'],
    #             "L": row['L'],
    #             "M": row['M'],
    #             "N": row['N'],
    #             "O": row['O'],
    #             "P": row['P'],
    #             "Q": row['Q'],
    #             "R": row['R'],
    #             "S": row['S'],
    #             "T": row['T'],
    #             "U": row['U'],
    #             "V": row['V'],
    #             "W": row['W'],
    #             "X": row['X'],
    #             "Y": row['Y'],
    #             "Z": row['Z'],
    #             "AA": row['AA'],
    #             "AB": row['AB'],
    #             "AC": row['AC'],
    #             "AD": row['AD'],
    #             "PsychotropicMedications": row['PsychotropicMedications'],
    #             "Administrations": row['Administrations'],
    #             "TherapeuticGuidances": row['TherapeuticGuidances']
    #         }
    #         print(data_json_post)
    #         r = requests.post(cc.URL_RAW, data=json.dumps(data_json_post), headers=cc.HEADERS_POST)


