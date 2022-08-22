import pandas as pd
import requests
import json
import sys
import os
import inspect

# CUSTOM IMPORT
import sys
import os
sys.path.append('/THESIS/bachelor-thesis/IOT_DEVICESTOAPI_SIM')
from THESIS.bachelor-thesis.IOT_DEVICESTOAPI_SIM import consts
#-----------------












def code200(request):
    '''Code 200 check'''
    return request.status_code == 200

def getRequest(url):
    request = requests.get(url)
    return request

def numObjects(request):
    '''
        Requesting  number of Json objects |
    '''
    if code200(request):
        data = request.json()
        length = len(data)
        return length
    else:
        print('[STATUS CODE]:ERROR')




def delete_entries_XY(start,end,url):
    '''
        It takes endpoints of specific deletion entry
    '''

    request = getRequest(url)
    for i in range(start,end):
        delete_url = f'{url}{i}'
        request.delete(delete_url)

def delete_entries_ALL(url):
    '''
        [DELETE] All (raw patient entries)
    '''
    id_list = []
    request = getRequest(url)
    # last = numObjects(request)
    for object in request.json():
        id_list.append(object['id'])

    if len(id_list) == 0:
        print('[INFO]: No Entries in api.')
        return
    print(f'Deleting entries of URL: {url} | Number of entries: {len(id_list)}')
    for id in id_list:
        delete_url = f'{url}{id}'
        r = requests.delete(delete_url)
        if r.status_code != 204:
            print(f'[ERROR-SC]: Status code:{r.status_code}')

def printtt():
    print(URL_RAW)

