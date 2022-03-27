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
    print ("extracting coordinate..")

def begin():
    print ("begin")

def end():
    print ("end")

# main
comments()
begin()

h_atom = 0   # number of hydrogen atoms
si_atom = 8  # number of si atoms in the conventional unit cell, fixed
cell_num = 2 # cell number
atom_num = h_atom + cell_num*si_atom # total number of atoms in the suprecell, fixed as 16

# read files
s = 'with coordinates     '
f2 = open("ABINIT_generic_atoms_coordinates_output.txt", 'w') # write mode
for i in range(0, atom_num):
    f1 = open("si_4c_general_"+str(i+1)+".txt", 'r')       # read mode
    target_line = linecache.getline("si_4c_general_"+str(i+1)+".txt", 8)

    #print(target_line)
    target_line = target_line.replace('   ',' ')
    target_line = target_line.replace('    ',' ')
    target_line = target_line.replace('  ',' ')
    f2.write(target_line.strip(s))

# close
f1.close
f2.close

# end
end()

# time display
elapsed_time = time.time()-start
print("elapsed_time:{:.2f}".format(elapsed_time) + "[sec]")
