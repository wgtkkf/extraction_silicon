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
import scipy.io
import itertools

start = time.time()

def begin():
    print ("begin")

def comments():
    print ("splitting..")

def comments_input():
    print ("Input >> how many atoms in the supercell? (16,32,48,..)")

def end():
    print ("end")

comments_input()
atom_num_keyboard = input()

dof = 3       # degree of freedom, fixed
atom_num = int(atom_num_keyboard) # number of atom's in the primitive cell
galine = np.zeros(atom_num,dtype=np.int64) # generic atom lines

# comments
comments()

# main
begin()

# change name here and delete this comment later
f1 = open('si_4c.out', 'r') # read mode

lines = [line for line in f1]
# full line length
full_length = len(open('si_4c.out').readlines())
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
