# delete and change the files after splitting ABINIT outputs for each generic atoms
# Coded by Takuro TOKUNAGA
# Last modified: August 31 2020
# not completed yet. add if routine later for 114 and 116

import numpy as np
import cmath
import pandas as pd
import time
#import scipy.io
import itertools
import os

start = time.time()


def begin():
    print ("begin")

def end():
    print ("end")

# functions for comments
def comments_cell():
    print ("Input >> supercell size? (1x1x2, 4, 6..)")

def comments():
    print ("removing and renaming..")

dof = 3       # degree of freedom, fixed
atom_num = 8 # number of atom's in the conventional unit cell
galine = np.zeros(atom_num,dtype=np.int64) # generic atom lines

comments_cell()
cell_number = input()
n = int(cell_number)*0.5

#
comments()

# main
begin()

# unnecessary file delete
for i in range(0,int(cell_number)*atom_num):
    if n > 1:
        check = os.path.exists("si_4c_general_"+str(i+1)+".txt")
        if i+1 < (8*(n-1)+1) or i+1 > 8*(n+1):
            if check == 1:
                os.remove("si_4c_general_"+str(i+1)+".txt") # remove file
            elif check == 0:
                break
    elif n==1:
        break

# rename remaining files
for i in range(0,int(cell_number)*atom_num):
    check = os.path.exists("si_4c_general_"+str(i+1)+".txt")

    if check == 1:
        os.rename("si_4c_general_"+str(i+1)+".txt", "si_4c_general_"+str(i+1-8*(int(n)-1))+".txt") # rename file

    # maximum of i
    if i > int(cell_number)*atom_num:
        break

# end
end()

# time display
elapsed_time = time.time()-start
print("elapsed_time:{:.2f}".format(elapsed_time) + "[sec]")
