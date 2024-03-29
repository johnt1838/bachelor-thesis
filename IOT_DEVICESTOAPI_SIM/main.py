"""
        Main IoT Simulation
        Description: It Simulates the devices pushing patient entries to the REST API
                     (that eventually will be used for feeding the prediction model)
"""
import pandas as pd

# custom
from devices import devicesSimulation
from http_utils import crequest as re
from testing import testing_post as test
from IOT_DEVICESTOAPI_SIM import consts as cc


def iotSimulation():
    data_link = './dataset/dataset_patient_entries_raw_2classes.csv'
    df_full = pd.read_csv(data_link)

    # ------test------
    # test.post_10(df_full)
    # test.dataset_for_use(df_full)
    # re.delete_entries_all(cc.URL_RAW)
    # re.delete_entries_all(cc.URL_RAW_DATA_TEST)

    # ------Actual--------
    devicesSimulation(10, debug=True)


if __name__ == '__main__':
    print('|------------------------------|IoT Simulation|------------------------------|\n')
    iotSimulation()
