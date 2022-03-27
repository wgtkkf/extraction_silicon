# split ABINIT output into each files of generic atoms
# Coded by Takuro TOKUNAGA
# Last modified: August 10 2020

# parameter info:
# file name of 'f1' and 'full_length '
# atom_num

import numpy as np
import cmath
import pandas as pd
import time
#import scipy.io
import itertools
import os
import glob

start = time.time()

def begin():
    print ("begin")

def comments():
    print ("splitting..")

def comments_delete():
    print ("Input >> How many si_4c_general file exist? (0, 16, 32, 48, ..)")

def comments_input():
    print ("Input >> How many atoms in the supercell? (16, 32, 48, ..)")

def end():
    print ("end")

# remove "si_4c_general_##_.txt" files generated before
# path define
path_abinit = "../abinit/"

comments_delete()
file_num_keyboard = input()
file_num = int(file_num_keyboard)
if file_num!=0:
    for i in range(0, file_num):
        os.remove(path_abinit + "si_4c_general_"+str(i+1)+".txt")
elif file_num==0:
    exit

# generate new "si_4c_general_##_.txt" files for IFCs extraction
comments_input()
atom_num_keyboard = input()
atom_num = int(atom_num_keyboard)
#atom_num = 16 # number of atom's in the primitive cell

#
dof = 3       # degree of freedom, fixed
galine = np.zeros(atom_num,dtype=np.int64) # generic atom lines

# comments
comments()

# main
begin()

# change name here and delete this comment later
f1 = open('si_4c_d.out', 'r') # read mode, d: device's d

lines = [line for line in f1]
# full line length
full_length = len(open('si_4c_d.out').readlines())
#print(str(full_length))

counter = 1
# extract force constant matrices
for i in lines:
    if 'generic atom number   '+str(counter) in i:
        galine[counter-1] = lines.index(i)
        #print(lines.index(i))
        counter += 1
    elif 'generic atom number  '+str(counter) in i:
        galine[counter-1] = lines.index(i)
        counter += 1

#print(str(galine))

# generic atom number 1~atom_num
for i in range(0,atom_num):
    f2 = open("si_4c_general_"+str(i+1)+".txt","w")
    if i<atom_num-1:
        for line in itertools.islice(lines, int(galine[i]), int(galine[i+1])):
            f2.write(line)
    else:
        for line in itertools.islice(lines, int(galine[i]), int(full_length)):
            f2.write(line)

    f2.close()

# file close
f1.close()
f2.close()

# end
end()

# time display
elapsed_time = time.time()-start
print("elapsed_time:{:.2f}".format(elapsed_time) + "[sec]")
