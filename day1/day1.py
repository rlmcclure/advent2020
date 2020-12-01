#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 23:29:05 2020

@author: rlmcclure
"""
#%%

import os
import numpy as np
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
            
#%% sort so it's more efficient? this takes it from .05s to .001s wtf
ns.sort()
#%% part 1
for nn in ns:
    if go1 == 1:
        for ff in ns:
                if go1 == 1 and nn+ff == 2020:
                    print(nn*ff)
                    go1 = 0

#%% part 2
for nn in ns:
    if go2 == 1:
        for ff in ns:
            if go2 == 1 and 2020-nn-ff >= min(ns):
                for tt in ns:
                    if nn+ff+tt == 2020:
                        print(nn*ff*tt)
                        go2 = 0
                        
end = timeit.default_timer()
print(end-start)
