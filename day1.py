#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 23:29:05 2020

@author: rlmcclure
"""
#%%

import os
import numpy as np
from astropy.io import fits
import pandas as pd
#%%
er_filen = 'day1_input.txt'
#%%
filestr = er_filen
with open(filestr) as f:    
    # first we allocate memory
    siz = 0
    for l in f:
        siz+=1
    nList = np.empty(siz)
    
with open(filestr) as f:  
        ii = 0
        for l in f:
            nList[ii]=int(l)
            ii+=1
#%%
nList.sort()
nListFlip = np.flip(nList)
for ii,nn in enumerate(nList):
    for jj,ff in enumerate(nListFlip):
            for kk,tt in enumerate(nList):
                if nn+ff+tt == 2020:
                    print(nn*ff*tt)