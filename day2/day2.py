#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 23:22:52 2020

@author: rlmcclure

Each line gives the password policy and then the password. The password policy
 indicates the lowest and highest number of times a given letter must appear
 for the password to be valid. For example, 1-3 a means that the password must
 contain a at least 1 time and at most 3 times.

How many passwords are valid according to their policies?
"""
#%%

import os
import numpy as np
import pandas as pd
import timeit
start = timeit.default_timer()

#%%
filen = 'input.txt'
#%%
pwds = pd.read_csv(filen,sep=' ',names=('Range','Letter'),index_col=2)
pwds['Letter']=pwds['Letter'].str.split(pat=':',expand=True)
pwds['Range']=pwds['Range'].str.split(pat='-')
#%% part 1
ii = 0
for pp,row in pwds.iterrows():
    let = row['Letter']
    lo = int(row['Range'][0])
    up = int(row['Range'][1])
    if pp.count(let) >= lo and pp.count(let) <= up:
        ii+=1
print(ii)
        
#%% part 2
jj = 0
for pp,row in pwds.iterrows():
    let = row['Letter']
    lo = int(row['Range'][0])
    up = int(row['Range'][1])
    if pp[lo-1] == let or pp[up-1] == let:
        if pp[lo-1] != pp[up-1]:
            jj+=1
print(jj)
#%%
end = timeit.default_timer()
print(end-start)