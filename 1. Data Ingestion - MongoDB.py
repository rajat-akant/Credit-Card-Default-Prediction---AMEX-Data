from pymongo import MongoClient
import pandas as pd
import csv
from time import process_time

client=MongoClient('localhost:27017') #Passing Local host and associated Port No. , Since the cluster is running on local machine.
print(client)
print("connection done")

db=client.Project #Connecting to relevant data base in your Mongo Cluster

# =============================================================================
# # Loading the dataset by every 5,00,000 rows
# =============================================================================
chunk_size=500000
#num=1
t1_start = process_time()
for chunk in pd.read_csv(r"C:/PC_Data/DBDA/Project/train_data.csv",chunksize=chunk_size):
    
    #below commented section was for trail only.
    # This is to break the loop after 02 iteration to avoid memory error
    # below condition is not required, since we are uploading complete dataset
    #if num > 02:
        #break
    db.train.insert_many(chunk.to_dict('record')) #ingesting the data in "train" collection
    #num+=1
t1_stop = process_time()
print("Elapsed time for Loading Data in seconds:",t1_stop-t1_start)

import gc
gc.collect()

# =============================================================================
# # Loading the training labels
# =============================================================================
chunk_size=500000
t1_start = process_time()
for chunk in pd.read_csv(r"C:/PC_Data/DBDA/Project/train_labels.csv",chunksize=chunk_size):
    
    db.labels.insert_many(chunk.to_dict('record')) #ingesting the data in "labels" collection

t1_stop = process_time()
print("Elapsed time for Loading Data in seconds:",t1_stop-t1_start)

import gc
gc.collect()


client.close()
# =============================================================================
# 1) The Above code shall be used for ingesting Data Set and Associated Labels
#    into MongoDB with each data set having a separate collection respectively.
# 2) The Database name could be anything. For our convinience I have kept it as Project.
# =============================================================================
