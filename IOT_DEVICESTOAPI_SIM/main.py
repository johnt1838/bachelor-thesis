'''
Main IoT Simulation
Description: It Simulates the devices pushing patient entries to the REST API
             (that eventually will be used for feeding the prediction model)
'''
import pandas as pd

#custom
from testing import testing_post as test
from http_utils import crequest
import consts as cc
from devices import devicesSimulation

def iotSimulation():
    datalink = './dataset/dataset_patient_enties_raw.csv'
    df_full = pd.read_csv(datalink)

    #------test------
    # test.post_10(df_full)


    # ------device posting--------
    # devicesSimulation()
    devicesSimulation(10)






if __name__ == '__main__':
    print('|------------------------------|IoT Simulation|------------------------------|\n')
    iotSimulation()

