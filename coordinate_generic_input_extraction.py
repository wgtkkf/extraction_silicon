# Extraction of coordinates by ABINIT
# Coded by Takuro TOKUNAGA
# Last modified: May 10 2020

import numpy as np
import pandas as pd
import time
#import scipy.io
import linecache

start = time.time()

def comments():
    print ("extracting input coordinates..")

def comments_input():
    print ("Input >> gap distance [angstrom]?")

def begin():
    print ("begin")

def end():
    print ("end")

# main
comments()
begin()

df1 = pd.read_csv('normalized_coordinate.txt', encoding = 'UTF8', sep=' ', header=0)
row, col = df1.shape

comments_input()
num_keyboard = input()              # [angstrom]
gap = np.float64(num_keyboard) # [angstrom]

cell_num = 8                             # [-]
lc_si = 5.480                            # [angstrom]
angs_to_bohr = 1.889725989               # [bohr/angstrom]
lx = lc_si*angs_to_bohr                  # [bohr]
ly = lx                                  # [bohr]
lz = ((lc_si*cell_num)+gap)*angs_to_bohr # [bohr]

# specific cell number
cell2 = 2 # left
cell3 = 3 # left
cell4 = 4 # center
cell5 = 5 # center
cell6 = 6 # right
cell7 = 7 # right

# normalized coordinates
norm_x = np.zeros(row, dtype='float64')
norm_y = np.zeros(row, dtype='float64')
norm_z = np.zeros(row, dtype='float64')

f1 = open('ABINIT_generic_atoms_coordinates_input_L.txt', 'w')
f2 = open('ABINIT_generic_atoms_coordinates_input.txt', 'w')
f3 = open('ABINIT_generic_atoms_coordinates_input_R.txt', 'w')

for i in range(0, row):
    norm_x[i] = df1.iat[i,0] # x line
    norm_y[i] = df1.iat[i,1] # y line
    norm_z[i] = df1.iat[i,2] # z line

for i in range(0, row):
    # left
    if i >= cell_num*(cell2-1) and i < cell_num*cell3:
       f1.write(str("{:.4f}".format(norm_x[i]*lx)))
       f1.write(str(' '))
       f1.write(str("{:.4f}".format(norm_y[i]*ly)))
       f1.write(str(' '))
       f1.write(str("{:.4f}".format(norm_z[i]*lz)))
       f1.write('\n')

    # center
    if i >= cell_num*(cell4-1) and i< cell_num*cell5:
       f2.write(str("{:.4f}".format(norm_x[i]*lx)))
       f2.write(str(' '))
       f2.write(str("{:.4f}".format(norm_y[i]*ly)))
       f2.write(str(' '))
       f2.write(str("{:.4f}".format(norm_z[i]*lz)))
       f2.write('\n')

    # right
    if i >= cell_num*(cell6-1) and i< cell_num*cell7:
       f3.write(str("{:.4f}".format(norm_x[i]*lx)))
       f3.write(str(' '))
       f3.write(str("{:.4f}".format(norm_y[i]*ly)))
       f3.write(str(' '))
       f3.write(str("{:.4f}".format(norm_z[i]*lz)))
       f3.write('\n')

# file close
f1.close()
f2.close()
f3.close()

# end
end()

# time display
elapsed_time = time.time()-start
print("elapsed_time:{:.2f}".format(elapsed_time) + "[sec]")
