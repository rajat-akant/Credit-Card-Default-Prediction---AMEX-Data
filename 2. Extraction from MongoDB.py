
from pymongo import MongoClient
import pandas as pd
import csv
from time import process_time

client=MongoClient('localhost:27017') #Passing Local host and associated Port No. , Since the cluster is running on local machine.
print(client)
print("connection done")

db=client.Project #Connecting to the the Data Base in Mongo Cluster.

# =============================================================================
# Extracting the first 500k rows from Mongo Cluster
# =============================================================================
t1 = process_time()
df = pd.DataFrame(list(db.train.find().limit(500000)))                                               
t2 = process_time()
print('time required for extraction',t2-t1)

# Dropping the default ID column of MongoDB
df.drop('_id', axis=1, inplace=True)

# Saving the dataframe to feather file for easy of computation
import pyarrow.feather as feather
feather.write_feather(df, "C:/PC_Data/DBDA/Project/seq_train_data.ftr")


# =============================================================================
# Extracting the train labels from from Mongo Cluster
# =============================================================================
t1 = process_time()
df = pd.DataFrame(list(db.labels.find()))                                               
t2 = process_time()
print('time required for extraction',t2-t1)

# Dropping the default ID column of MongoDB
df.drop('_id', axis=1, inplace=True)

# Saving the dataframe to feather file for easy of computation
import pyarrow.feather as feather
feather.write_feather(df, "C:/PC_Data/DBDA/Project/labels_data.ftr")

client.close()
