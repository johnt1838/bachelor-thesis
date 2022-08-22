import pandas as pd
import requests
import json

# CUSTOM IMPORT CONSTS
from IOT_DEVICESTOAPI_SIM import consts as cc


def code200(request):
    """Code 200 check"""
    return request.status_code == 200


def get_request(url):
    request = requests.get(url)
    return request


def number_objects(request):
    """
        Requesting  number of Json objects |
    """
    if code200(request):
        data = request.json()
        length = len(data)
        return length
    else:
        print('[STATUS CODE]:ERROR')


def delete_entries_specific(start, end, url):
    """
        It takes endpoints of specific deletion entry
    """

    request = get_request(url)
    for i in range(start, end):
        delete_url = f'{url}{i}'
        request.delete(delete_url)


def delete_entries_all(url):
    """
        [DELETE] All (raw patient entries)
    """
    # Gathering
    id_list = []
    request = get_request(url)
    json_ = request.json()
    for object_ in json_['results']:
        id_list.append(object_['id'])
    print(json_['next'])
    while json_['next'] != None:
        json_ = get_request(json_['next']).json()
        for object_ in json_['results']:
            id_list.append(object_['id'])

    # Deleting
    if len(id_list) == 0:
        print('[INFO]: No Entries in api.')
        return
    print(f'Deleting entries of URL: {url} | Number of entries: {len(id_list)}')
    for id_ in id_list:
        delete_url = f'{url}{id_}'
        r = requests.delete(delete_url)
        if r.status_code != 204:
            print(f'[ERROR-SC]: Status code:{r.status_code}')
