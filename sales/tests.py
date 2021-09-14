from django.test import TestCase
import json
import pandas as pd
import csv

def TestApiResponse():
    with open('response.json', 'r') as f:
        data = json.load(f)

    data_frame = pd.json_normalize(data['items'])

    print(data_frame.head())

    # for item in data['items']:
    #     try:
    #         print(item['productId'], item['title'], item['primaryOffer']['offerPrice'])
    #     except:
    #         pass


TestApiResponse()


def OpenCsv():
    # with open('walmart-products.csv', 'r') as csv_file:
    #     csvFile = csv.reader(csv_file, delimiter=',')
    
    #     for row in csvFile:
    #         print(row)


    csvFile = pd.read_csv('walmart-products.csv')

    print(csvFile)

OpenCsv()