"""Testing File"""
import matplotlib.pyplot as plt
import pandas as pd
import requests
import json

# CUSTOM
from IOT_DEVICESTOAPI_SIM import consts as cc


def post_10(df):
    print('working')
    pd.set_option('display.max_rows', None)
    # df = df.iloc[:10, :]

    df = df.iloc[[0, 96]]
    print(df)
    r = requests.get(url=cc.URL_RAW, headers=cc.HEADERS_POST)

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


def dataset_for_use(df):
    x = df['Diagnosis'].value_counts()
    diagnosis_list_clean = []
    diagnosis_list_all = []
    dict_diag = {}
    i = 1
    for diagnosis, value in x.items():
        diagnosis_list_all.append(diagnosis)
        if value >= 50:
            # keep diagnosis's with high frequency
            diagnosis_list_clean.append(diagnosis)
            dict_diag[f'{i}'] = {diagnosis: value}
        i = i + 1
    df = df[df['Diagnosis'].isin(diagnosis_list_clean)]
    df = df.replace('MDD, Recurrent, Severe Without Psychotic Features', 'MDD, Recurrent')
    # df = df.replace('Depressive Disorder NOS', )
    df = df.replace('MDD, Single Episode,Severe Without Psychotic Features', 'MDD, Single Episode')
    # df = df.replace('MDD', )
    df = df.replace('MDD, Single Episode, Severe With Psychotic Features', 'MDD, Single Episode')
    df = df.replace('MDD, Recurrent, Severe With Psychotic Features', 'MDD, Recurrent')
    df = df[df['Diagnosis'] != 'MDD']
    df = df[df['Diagnosis'] != 'Depressive Disorder NOS']

    # Save to file
    save_url = 'dataset/dataset_patient_entries_raw_2classes.csv'
    saving = df.to_csv(save_url, index=False)


    # return save_url

if __name__ == '__main__':
    df = pd.read_csv('C:/Users/Giannis/Desktop/bachelor-thesis/IOT_DEVICESTOAPI_SIM/dataset/dataset_patient_enties_raw.csv')
    x = df['Diagnosis'].value_counts()
    diagnosis_list_clean = []
    diagnosis_list_all = []
    dict_diag = {}
    dict_diag_all = {}
    i = 1
    for diagnosis, value in x.items():
        dict_diag_all[f'{i}'] = {diagnosis: value}
        if value >= 50:
            # keep diagnosis's with high frequency
            diagnosis_list_clean.append(diagnosis)
            dict_diag[f'{i}'] = {diagnosis: value}
        i = i + 1

    for k, v in dict_diag_all.items():
        print(str(k) + ': ' + str(v))
    fig = df['Diagnosis'].value_counts()[:20].plot(kind='bar')
    # plt.subplots_adjust(bottom=.87, )
    plt.savefig('myfile.png', bbox_inches="tight")

    plt.show()


