"""
    -Main Server it simulates a server getting data from an API.
    These Data will be processed and they will be fed in a model,
    for training purposes.

    -When the model will be ready. There will be an extra api endpoint for
    model testing purposes.
"""

from server import *
from test_model_api import *
import os


def ServerSimulation():


    print('[Server Simulation]')
    #---------Testing------------
    #
    server = init_server()
    #---------Actual-------------


    # x= os.path.exists('ensemble.pickle')
    # if x:
    #     loaded_model = pickle.load(open('ensemble.pickle', 'rb'))
    #     test_model(loaded_model)
    # else:
    #     server = init_server()

























if __name__ == '__main__':
    print('|------------------------------|Server Simulation|------------------------------|\n')
    ServerSimulation()