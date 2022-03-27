# Mass matrices (ML/MC/MR)
# Coded by Takuro TOKUNAGA
# Last modified: February 20 2020

import numpy as np
import pandas as pd
import time
import scipy.io
#import itertools

start = time.time()

def comments():
    print ("mass matrices..")

def begin():
    print ("begin")

def end():
    print ("end")

comments()

# main
begin()

dof = 3 # [-]
atom_num = 8 # number of atom's in the primitive cell
size= atom_num*dof # [-]
atom_num2 = 16 # number of atom's in the primitive cell
size2= atom_num2*dof # [-]
silicon_mass = 28.0855 # [amu]
germanium_mass = 72.6400 # [amu]

mass1=np.zeros((size,size), dtype=np.float64) # 24 24
mass2=np.zeros((size2,size2), dtype=np.float64) # 48 48

f1 = open("../abinit/ML.txt", 'w') # write mode
f2 = open("../abinit/MR.txt", 'w') # write mode
f3 = open("../abinit/MC.txt", 'w') # write mode

# initialization
# ML, MR & MC
# Si/Si symmetric system
for i in range(0, size2):
    for j in range(0, size2):
        if i==j:
            mass2[i][j] = silicon_mass

# output (ML, MR & MC)
for i in range(0, size2): # 48
    for j in range(0, size2): # 48
        f1.write(str(mass2[i][j]))
        f1.write(str(' '))

        f2.write(str(mass2[i][j]))
        f2.write(str(' '))

        f3.write(str(mass2[i][j]))
        f3.write(str(' '))
    f1.write('\n')
    f2.write('\n')
    f3.write('\n')

# close
f1.close
f2.close
f3.close

# end
end()

# time display
elapsed_time = time.time()-start
print("elapsed_time:{:.2f}".format(elapsed_time) + "[sec]")
