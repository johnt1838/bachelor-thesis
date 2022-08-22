import logging
import threading
import pandas as pd

# Custom Libraries
from http_utils import crequest





class Device:
    '''
        Simulation IoT devices.These devices will have some characteristics and a small portion of data that will be used to
        simulate the data posting in the "middleman" REST-API.
    '''

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
    '''
        Taking a big dataset and splitting it to numDataframes.
        The return will be a list of smaller partitioned datasets
        numDataframes: numbers of dataframes to split
        numEntries: numbers of entries (rows) each small dataframe will have
        dataset: Big Dataset
    '''
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
    '''
        Creating X numbers of devices.
        Using Device class for multiple devices
        and dataFeeding function for Data input
    '''
    # creating devices
    listDevices = []
    listDatasets = dataFeeding(numberDevices, dataframe)
    for i in range(1, numberDevices + 1):
        listDevices.append(Device(i, listDatasets[i - 1]))
    return listDevices


def deviceThread(device):
    '''
            A thread for a device
    '''
    logging.info(f'[Thread {device.id}][Device{device.id}]: starting')

    logging.info(f'[Thread {device.id}][Device{device.id}]: finishing')


def devicesSimulation(numDevices, debug=False):
    '''
    Simulating Devices"
            1. Set big dataset\n
            2. Create devices\n
            3. Make the devices send data to api\n
            4.
    '''
    df = pd.read_csv('./dataset/dataset_clean_preprocessed_2classes_v1.csv')

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
        x = threading.Thread(target=deviceThread(device), args=(device.id,))
        x.start()
        threads.append(x)
    for thread in threads:
        thread.join()
