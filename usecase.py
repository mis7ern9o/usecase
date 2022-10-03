import json
import os
import pandas as pd
import time

# generic and simple mapping script
# https://www.onlinedatagenerator.com/

# TODO Add  formulas to destination file
# TODO Add more rows to dataset.csv

tic = time.perf_counter()
curdir = os.path.dirname(__file__)
inMap = os.path.join(curdir, 'mapping.json')
inData = os.path.join(curdir, 'dataset200k.csv')
outData = os.path.join(curdir, 'dataset_out.csv')

# parse json into dic
fmap = open(inMap)
dmap = json.load(fmap)

# open dataset into dataframe
fdata = pd.read_csv(inData, delimiter=",", encoding="utf8")
idx_dic = {}
for col in fdata.columns:
    idx_dic[fdata.columns.get_loc(col)] = col

fdatanum = len(fdata)

# map dataset
frame = {}
for col in dmap:
    label = dmap[col]['label']
    colSource = dmap[col]['source']
    if colSource == "none":
        default = dmap[col]['default']
        frame[label] = pd.Series(default, index=range(fdatanum))
    else:        
        frame[label] = pd.Series(fdata.iloc[:, int(colSource)])

result = pd.DataFrame(frame)
result.to_csv(outData, sep=';', index=False)
toc = time.perf_counter()
print(f"Speed {toc - tic:0.4f} seconds")

