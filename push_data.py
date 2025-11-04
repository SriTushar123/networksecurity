import os 
import json
import sys
from networksecurity.exception.exception import NetworkSecurityException
import certifi
import pymongo
import pandas as pd
from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv
load_dotenv()

MONGO_DB_URL=os.getenv("MONGO_DB_URL")
print(MONGO_DB_URL)

ca=certifi.where()

class NetworkDataExtract:
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def json_to_csv_converter(self,file_path):
        try:
            data=pd.read_csv(file_path)
            data.reset_index(drop=True,inplace=True)
            records=list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise NetworkSecurityException(e,sys)
 
    def data_insert_mongodb(self,records,collection,database):
        try:
            self.database=database
            self.collection=collection
            self.records=records

            self.mongo_client=MongoClient(MONGO_DB_URL,tlsCAFile=ca)
            self.database=self.mongo_client[self.database]
            self.collection=self.database[self.collection]
            self.collection.insert_many(self.records)
            return(len(self.records))
        except Exception as e:
            raise NetworkSecurityException(e,sys)

if (__name__=="__main__"):
    FILE_PATH="Network_Data/phisingData.csv"
    COLLECTION="NetworkData"
    DATABASE="TusharAI"
    networksecurityobj=NetworkDataExtract()
    records=networksecurityobj.json_to_csv_converter(file_path=FILE_PATH)
    print(records)
    no_of_records=networksecurityobj.data_insert_mongodb(records=records,database=DATABASE,collection=COLLECTION)
    print(no_of_records)


