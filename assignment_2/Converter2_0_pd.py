import os
import glob
from zipfile import ZipFile

import numpy as np

import pandas as pd
import vaex

def should_ignore(file):
    with open(file, 'r') as file:
        first_line = file.readline()
        _ = file.readline()
        third = file.readline()
        if first_line.count(",") != third.count(","):
            return True
        return False

dtype={
    'ehail_fee':np.float32,
    'trip_distance':np.float32,
    'dropoff_latitude':np.float32,
    'dropoff_longitude':np.float32,
    'passenger_count':np.float32,  # int32
    'tip_amount':np.float32,
    'pulocationid':np.float32,  # int32
    'improvement_surcharge':np.float32,
    'trip_type':np.float32,  # int32
    'pickup_latitude':np.float32,
    'fare_amount':np.float32,
    'congestion_surcharge':np.float32,
    'extra':np.float32,
    'ratecodeid':np.float32,  # int32
    'lpep_dropoff_datetime':np.object,
    'vendorid':np.float32,  # int32
    'lpep_pickup_datetime':np.object,
    'trip_type ':np.float32,  # int32
    'store_and_fwd_flag':str,
    'mta_tax':np.float32,
    'dolocationid':np.float32,  # int32
    'pickup_longitude':np.float32,
    'payment_type':np.float32,  # int32
    'tolls_amount':np.float32,
    'total_amount':np.float32
}

pd.set_option('display.max_columns', 500)
g = os.walk("./data/")
p = "./data/"
file_lst = ['green_tripdata_2013-08.csv','green_tripdata_2015-01.csv','green_tripdata_2016-07.csv','green_tripdata_2019-01.csv']
dic = dict()
lower_dic = dict()
all_cols = set()
def get_col_set(df):
    cols = set(list(df.columns))
for file_name in file_lst:
    df = pd.read_csv(os.path.join(p, file_name))
    cols = list(df.columns)
    for item in cols:
        if item not in lower_dic:
            lower_dic[item] = item.lower()
    cols = [item.lower() for item in cols]
    cols = set(cols)
    all_cols|=cols
print(all_cols)
is_first = False
for path,dir_list,file_list in g:
    for file_name in file_list:
        full_name = os.path.join(path, file_name)
        print(full_name)
        if should_ignore(full_name):
            continue
        df = pd.read_csv(full_name)
        df.rename(columns=lower_dic,inplace=True)
        difference = all_cols - set(df.columns)
        for col in difference:
            df[str(col)] = None
        for col in all_cols:
            df[col] = df[col].astype(dtype[col])

        # df.to_hdf(os.path.join("./data_output_pd/", file_name[:-3]+"hdf5"),'table',mode='w',format='table')
        if is_first:
            df.to_hdf("./green_tripdata_pd.hdf5", 'table', mode='w', format='table')
            is_first = False
        else:
            df.to_hdf("./green_tripdata_pd.hdf5",'table', append=True)