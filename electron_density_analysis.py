# Coded by Takuro TOKUNAGA
# Last modified: April 27 2021

import numpy as np
import time
import sys
import pandas as pd

start = time.time()

# function: begin
def begin():
    print ("begin")

# function: end
def end():
    print ("end")

# read brillouin zone points
data = pd.read_csv("../../shared_win/5angs_volume_analysis.txt", sep=" ", header=None)
data.columns = ["x", "y", "z", "density"]
row, col = data.shape # row & column of matorix

x = np.zeros(row, dtype='float64')
y = np.zeros(row, dtype='float64')
z = np.zeros(row, dtype='float64')
d = np.zeros(row, dtype='float64')
density = np.zeros(row, dtype='float64')
total = 0

for i in range(0, row):
    x[i] = data.iat[i,0] # x line
    y[i] = data.iat[i,1] # y line
    z[i] = data.iat[i,2] # z line
    d[i] = data.iat[i,3] # density line

# main start
begin()

z1_criteria = 45.731 # bohr
z2_criteria = 53.971 # bohr

# 42.405 / 45.958
# 43.464 / 48.679
# 44.598 / 51.325
# 45.731 / 53.971

f1 = open('electron_density_sum.txt', 'w')

for i in range(0,row):
    if z[i] > z1_criteria and z[i] < z2_criteria:
        print(str(z[i]))
        total += d[i]

# file output
f1.write(str(total))

# file close
f1.close()

# end
end()

# time display
elapsed_time = time.time()-start
print("elapsed_time:{:.2f}".format(elapsed_time) + "[sec]")
