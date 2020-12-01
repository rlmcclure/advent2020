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
import itertools
import timeit
start = timeit.default_timer()
go1 = 1
go2 = 1
#%%
er_filen = 'day1_input.txt'
#%%
filestr = er_filen
with open(filestr) as f:    
    # first we allocate memory
    siz = 0
    for l in f:
        siz+=1
    ns = np.empty(siz)
    
with open(filestr) as f:  
        ii = 0
        for l in f:
            ns[ii]=int(l)
            ii+=1

#%% part 1
for n in itertools.product(ns, ns):
    if go1 == 1:
        if sum(n) == 2020:
            print(np.product(n))
            go1 = 0
#%% part 2
for n in itertools.product(ns, ns, ns):
    if go2 == 1:
        if sum(n) == 2020:
            print(np.product(n))
            go2 = 0
    

end = timeit.default_timer()
print(end-start)
