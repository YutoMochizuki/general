#!/bin/sh

#400個のディレクトリのftmergeするファイルのtxtを出力するプログラム


import os
import datetime
import math

from astropy.io import ascii
from astropy.io import fits
from astropy.table import Table
from astropy.time import Time
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.graph_objs as go

#s = "ftmerge "
#for i in range(1,401):
#    if i < 10:
#        s = str(s) + "00000"+str(i)+"/xout_spect1.fits,"
#    elif i < 100:
#        s = str(s) + "0000"+str(i)+"/xout_spect1.fits,"
#    elif i < 400:
#        s = str(s) + "000"+str(i)+"/xout_spect1.fits,"
#    else:
#        s = str(s) + "000"+str(i)+"/xout_spect1.fits"
#s =  str(s) + " xout_spect1.fits"
#print(s)

s = ""
for i in range(1,401):
    if i < 10:
        s = "00000"+str(i)+"/xout_spect1.fits"
    elif i < 100:
        s = "0000"+str(i)+"/xout_spect1.fits"
    else:
        s = "000"+str(i)+"/xout_spect1.fits"

ds = pd.DataFrame(s,header=None)

ds.to_csv('ftmerge.txt', sep='\t', index=False, header=None)
