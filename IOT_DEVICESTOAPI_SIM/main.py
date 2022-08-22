'''
        Main IoT Simulation
        Description: It Simulates the devices pushing patient entries to the REST API
                     (that eventually will be used for feeding the prediction model)
'''
import pandas as pd

#custom
from devices import devicesSimulation
from http_utils import crequest as re


def iotSimulation():
    datalink = './dataset/dataset_patient_enties_raw.csv'
    df_full = pd.read_csv(datalink)

    #------test------
    # test.post_10(df_full)
    print(re.printtt())


    # ------device posting--------
    # devicesSimulation(10)






if __name__ == '__main__':
    print('|------------------------------|IoT Simulation|------------------------------|\n')
    iotSimulation()

