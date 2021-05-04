#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 14:49:10 2021

@author: durack1
"""

import datetime
import json
import pdb
import shlex
import subprocess
import sys
from esgfQueryModels import get_dataset_time_data

#%% Get time
timeNow = datetime.datetime.now()
timeFormat = timeNow.strftime('%Y-%m-%d')
timeFormatDir = timeNow.strftime('%y%m%d')
print(timeFormatDir)

#%% Define MIPs and iterate
keys = ['C4MIP', 'CMIP', 'DAMIP', 'FAFMIP', 'HighResMIP', 'OMIP', 'PMIP',
        'ScenarioMIP']
for key in keys:
    print(key)

    # Call function
    js = get_dataset_time_data(project='CMIP6', activity_id=key,
                               variable_id='tos')

    # Write output
    outFile = '_'.join([timeFormat, key, 'esgf_dataset.json'])
    print('outFile:', outFile)
    print('JSON response numFound:', js['response']['numFound'])
    with open(outFile, 'w', encoding='utf-8') as f:
        json.dump(js, f, ensure_ascii=False, indent=4)

#%%

#3982
#https://esgf-node.llnl.gov/solr/datasets/select?q=*:*&wt=json&facet=true&rows=4000&fq=type:Dataset&fq=mip_era:CMIP6&fq=activity_id:CMIP&fq=experiment_id:historical&fq=variable_id:tos&shards=localhost:8983/solr/datasets,localhost:8985/solr/datasets,localhost:8987/solr/datasets,localhost:8988/solr/datasets,localhost:8990/solr/datasets,localhost:8993/solr/datasets,localhost:8994/solr/datasets,localhost:8995/solr/datasets,localhost:8996/solr/datasets,localhost:8997/solr/datasets
#2204
#https://esgf-node.llnl.gov/solr/datasets/select?q=*:*&wt=json&facet=true&rows=2161&fq=type:Dataset&fq=mip_era:CMIP6&fq=activity_id:CMIP&fq=experiment_id:historical&fq=variable_id:tos
#Shards
#https://esgf-node.llnl.gov/esg-search/search/?limit=0&format=application%2Fsolr%2Bjson