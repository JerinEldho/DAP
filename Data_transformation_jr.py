# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 14:14:04 2022

@author: jerin
"""

import pymongo
import pandas as pd
import json
import xml.etree.ElementTree as ETree

xmldata2="D:\\NCI Modules\\Sem 1\\DAP\\CARRIER_DECODE.xml"

client = pymongo.MongoClient("mongodb://localhost:27017")

prstree2 = ETree.parse(xmldata2)
root2 = prstree2.getroot()


careerlist = []

all_data2 = []

for y in root2.iter('row'):
        airlineid = y.find('AIRLINE_ID').text
        opunique = y.find('OP_UNIQUE_CARRIER').text
        carrier = y.find('CARRIER_NAME').text
        careerlist = [airlineid,opunique,carrier]
        all_data2.append(careerlist)


df24 = pd.DataFrame(all_data2, columns =['AIRLINE_ID', 'OP_UNIQUE_CARRIER','CARRIER_NAME'])


data24 = df24.to_dict(orient="records")

db = client["AirlineData"]

db.CARRIER_DECODE.insert_many(data24)