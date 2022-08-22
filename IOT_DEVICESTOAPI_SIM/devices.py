import logging
import threading
import time
from random import randrange

import pandas as pd
import json

# Custom Libraries
import requests

from http_utils import crequest
from IOT_DEVICESTOAPI_SIM import consts as cc






class Device:
    """
        Simulation IoT devices.These devices will have some characteristics and a small portion of data that will be used to
        simulate the data posting in the "middleman" REST-API.
    """

    def __init__(self, id, data):
        self.id = id
        self.name = f'Patient{id}'
        self.data = data
        self.entries = data.shape[0]

    def __str__(self):
        return f'Device:{self.id} | Name:{self.name} | Entries:{self.entries}'

    def showData(self):
        print(self.data)


def dataFeeding(numDataframes, dataset):
    """
        Taking a big dataset and splitting it to numDataframes.
        The return will be a list of smaller partitioned datasets
        numDataframes: numbers of dataframes to split
        numEntries: numbers of entries (rows) each small dataframe will have
        dataset: Big Dataset
    """
    list_of_datasets = []
    # ---(97)------------------(970)---------/---(10)
    numEntries = int(len(dataset.index) / numDataframes)
    start = 0
    end = numEntries

    df = dataset.iloc[start:end]
    list_of_datasets.append(df)
    if numDataframes > 1:
        for i in range(1, numDataframes + 1):
            start = i * numEntries
            df = dataset.iloc[start:start + numEntries]
            list_of_datasets.append(df)
    return list_of_datasets


def createDevices(numberDevices, dataframe):
    """
        Creating X numbers of devices.
        Using Device class for multiple devices
        and dataFeeding function for Data input
    """
    # creating devices
    listDevices = []
    listDatasets = dataFeeding(numberDevices, dataframe)
    for i in range(1, numberDevices + 1):
        listDevices.append(Device(i, listDatasets[i - 1]))
    return listDevices


def deviceThread(device):
    """
            A thread for a device
            This function will get the device instance and will
            push on api endpoint its data.
    """
    logging.info(f'[Thread {device.id}][Device{device.id}]: starting')
    r = requests.get(url=cc.URL_RAW, headers=cc.HEADERS_POST)
    print(r.status_code)
    json_ = r.json()
    print(json_)
    if r.status_code == 200:
        for index, row in device.data.iterrows():
            print(f'{index=}')
            data_json_post = {
                "Gender": row['GENDER'],
                "Age":row['AGE'] ,
                "Race": row['RACE_ETHNICITY'],
                "Diagnosis": row['Diagnosis'],
                "MD": row['MD'],
                "Assignment": row['Assignment'],
                "EMR": row['EMR'],
                "LOS": row['LOS'] ,
                "RAR": row['RAR'],
                "A": row['A'],
                "B": row['B'],
                "C": row['C'],
                "D": row['D'],
                "E": row['E'],
                "F": row['F'],
                "G": row['G'],
                "H": row['H'],
                "I": row['I'],
                "J": row['J'],
                "K": row['K'],
                "L": row['L'],
                "M": row['M'],
                "N": row['N'],
                "O": row['O'],
                "P": row['P'],
                "Q": row['Q'],
                "R": row['R'],
                "S": row['S'],
                "T": row['T'],
                "U": row['U'],
                "V": row['V'],
                "W": row['W'],
                "X": row['X'],
                "Y": row['Y'],
                "Z": row['Z'],
                "AA": row['AA'],
                "AB": row['AB'],
                "AC": row['AC'],
                "AD": row['AD'],
                "PsychotropicMedications": row['PsychotropicMedications'],
                "Administrations": row['Administrations'],
                "TherapeuticGuidances": row['TherapeuticGuidances']
            }
            print(data_json_post)
            r = requests.post(cc.URL_RAW, data=json.dumps(data_json_post), headers=cc.HEADERS_POST)



    logging.info(f'[Thread {device.id}][Device{device.id}]: finishing')


def devicesSimulation(numDevices, debug=False):
    """
    Simulating Devices:
            1. Set big dataset\n
            2. Create devices\n
            3. Make the devices send data to api\n
            4.
    """
    df = pd.read_csv('./dataset/dataset_patient_entries_raw_2classes.csv')

    devices = createDevices(numberDevices=numDevices, dataframe=df)
    if len(devices) < 1:
        print('[DEBUG]: Error number of devices is less than 1')

    if debug:
        for device in devices:
            print(f'[DEVICE{device.id}]: {device}\n')
            device.showData()

    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")
    threads = list()
    for device in devices:
        logging.info(f'[MAIN]: create and start thread {device.id}')
        x = threading.Thread(target=deviceThread, args=(device, ))
        threads.append(x)
        x.start()
    for thread in threads:
        thread.join()
