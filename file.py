import json
import os
import csv
import pandas as pd

curdir=os.path.dirname(__file__)
inMap=os.path.join(curdir,'mapping.json')
inData=os.path.join(curdir,'dataset.csv')
outData=os.path.join(curdir,'dataset_out.csv')

# parse json into dic
fmap = open(inMap)
dmap = json.load(fmap)

#open dataset into dataframe
fdata = pd.read_csv(inData,delimiter=",", encoding="utf8")
idx_dic = {}
for col in fdata.columns:
    idx_dic[fdata.columns.get_loc(col)] = col

fdatanum = len(fdata)

frame = {}
for col in dmap:
    label = dmap[col]['label']
    colSource = dmap[col]['source']
    print(label, col, colSource)

    if colSource == "none":
        default = dmap[col]['default']
        print('check>>',dmap[col]['fx'])
        frame[label] = pd.Series(default, index=range(fdatanum))
    else:        
        frame[label] = pd.Series(fdata.iloc[:, int(colSource)])

#frame = { 'Author': auth_series, 'Article': article_series }
#Creating DataFrame by passing Dictionary
result = pd.DataFrame(frame)
print(result.columns)
    




#print(fdata.iloc[:, 3])










#


