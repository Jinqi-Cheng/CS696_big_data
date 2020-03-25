"""
Create Date , 
@author: 
"""
import re
import glob
import vaex
import numpy as np

def tryint(s):
    try:
        return int(s)
    except:
        return s

def alphanum_key(s):
    """ Turn a string into a list of string and number chunks.
        "z23a" -> ["z", 23, "a"]
    """
    return [ tryint(c) for c in re.split('([0-9]+)', s) ]
# print(dic)
hdf5_list = glob.glob('./data_output/*.hdf5')
hdf5_list.sort(key=alphanum_key)
hdf5_list = np.array(hdf5_list)
print(hdf5_list)

# df = vaex.open(hdf5_list[0])
# print(df)


# This is an important step
master_df = vaex.open_many(hdf5_list)

# exporting
master_df.export_hdf5(path='./green_tripdata.hdf5')
#
df = vaex.open('./green_tripdata.hdf5')
print(df)