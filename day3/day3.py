#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 22:15:13 2020
@author: rlmcclure

Due to the local geology, trees in this area only grow on exact integer
 coordinates in a grid. You make a map (your puzzle input) of the open squares
 (.) and trees (#) you can see. For example:

The toboggan can only follow a few specific slopes (you opted for a cheaper
 model that prefers rational numbers); start by counting all the trees you
 would encounter for the slope right 3, down 1:From your starting position
 at the top-left, check the position that is right 3 and down 1. Then, check
 the position that is right 3 and down 1 from there, and so on until you go
 past the bottom of the map.

The locations you'd check in the above example are marked here with O where
 there was an open square and X where there was a tree:


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
with open(filen) as f:
        lines = f.readlines()
        
tree = '#'
s = '.'
nl = '\n'
#%% part 1
tct = 0
r,d = [3,1]
y,x = [0,0]
for ii in np.arange(np.shape(lines)[0]-1):
    y += d
    x += r
    if x > (len(lines[y])-2):
        x = x - (len(lines[y])-1)
    if lines[y][x] == tree:
        tct += 1
print(tct)
    
#%% part 2
tctList = []
r = [1,3,5,7,1]
d = [1,1,1,1,2]
for jj in np.arange(len(r)):
    tct = 0
    y,x = [0,0]
    for ii in np.arange(np.shape(lines)[0]-1):
        y += d[jj]
        x += r[jj]
        if y > (np.shape(lines)[0]-1):
            break
        if x > (len(lines[y])-2):
            x = x - (len(lines[y])-1)
        if lines[y][x] == tree:
            tct += 1
    tctList.append(tct)
print(np.prod(tctList))
#%%
end = timeit.default_timer()
print(end-start)
