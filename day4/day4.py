#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 22:55:44 2020

@author: rlmcclure

Passport data is validated in batch files (your puzzle input). Each passport is
 represented as a sequence of key:value pairs separated by spaces or newlines.
 Passports are separated by blank lines.
"""

import os
import numpy as np
import pandas as pd
import timeit
start = timeit.default_timer()

#%%
filen = 'day4/input.txt'
#%%
with open(filen) as f:
    print(help(f))
    lines = f.readlines()

nl = '\n'
'''
so I had '\n\n' instead of '\n \n' and then would have had it a lot earlier
'''
#%%
#%%
#byr #(Birth Year)
#iyr #(Issue Year)
#eyr #(Expiration Year)
#hgt #(Height)
#hcl #(Hair Color)
#ecl #(Eye Color)
#pid #(Passport ID)
#opt
#cid #(Country ID)

#rqd
mtch = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
#%% part 1
ppct = 0
validpct = 0
cutp = []
jj = 0
for ii in np.arange(np.shape(lines)[0]-1):
    jj+=1
    if lines [ii+1] == nl:
        curpp = ' '.join(lines[ii+1-jj:ii+1])
        if all(x in curpp for x in mtch):
            validpct +=1
        ppct += 1
        jj=-1
ii+=1
curpp = ' '.join(lines[ii-jj:ii+1])
if any(x in curpp for x in mtch):
    validpct +=1
ppct += 1

#%%
