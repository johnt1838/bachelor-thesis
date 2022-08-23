import pandas as pd
import requests
# Custom
import constants as cc



def init_server():
    print("[DEBUG]: INIT SERVER\n")

    json_data = get_data()
    link = json_to_csv(json_data)
    df = pd.read_csv(link)
    model = create_model(df)


def get_data():
    """
        Getting data from raw api in JSON format.
    """

    links = [cc.URL_RAW_DATA]
    request = requests.get(cc.URL_RAW_DATA,
                           headers=cc.HEADERS)
    json_ = request.json()
    while json_['next'] is not None:
        links.append(json_['next'])
        json_ = requests.get(json_['next']).json()

    bigJson = {'results': []}
    for link in links:
        request = requests.get(link,
                               headers=cc.HEADERS)
        json_data = request.json()
        for data_line in json_data['results']:
            # print(data_line)
            # bigJson.update(data_line)
            bigJson['results'].append(data_line)

    return bigJson


def json_to_csv(json_data):
    link = "api_dataset.csv"
    columns = list(json_data['results'][0].keys())
    f = open(link, "w")
    # 1st line columns
    i = 1
    for column in columns:
        if i != len(columns):
            f.write(',')
            i+=1
        else:
            f.write('\n')

    for line in json_data['results']:
        for index_,col in enumerate(columns):
            f.write(str(line[f'{col}']))
            if index_ != len(columns)-1:
                f.write(',')

        f.write('\n')
    return link

def create_model(df):
    pass