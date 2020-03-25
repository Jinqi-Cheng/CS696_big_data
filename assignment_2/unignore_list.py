"""
Create Date , 
@author: 
"""


# def should_ignore(file):
#     with open(file, 'r') as file:
#         first_line = file.readline()
#         _ = file.readline()
#         third = file.readline()
#         if first_line.count(",") != third.count(","):
#             return True
#         return False




import h5py
f=h5py.File("./data_output/green_tripdata_2015-07.hdf5","r")
print(f.keys())