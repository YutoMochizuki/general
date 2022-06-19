#!/bin/sh
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

#%matplotlib inline

r_dir = "./../evt/"
r_file = "xa097081400rsl_p0px1010_cl.evt"

#image_fileの中にeventfiileを代入
image_file = os.path.join(r_dir, r_file)

#fitsのヘッダーを代入
hdu_list = fits.open(image_file)
print(hdu_list.info())

#header = hdu_list['EVENTS'].header
#print(header)



