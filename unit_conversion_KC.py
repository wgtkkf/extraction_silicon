# force constant matrix generation code from ABINIT output
# Coded by Takuro TOKUNAGA
# Last modified: September 03 2020

import numpy as np
import pandas as pd
import time
#import itertools

start = time.time()

# Unit conversion: atomic unit
hartree = 27.2113961 # [eV]
bohr = 0.529177249 # [angs]

# ABINIT to LAMMPS
ABINIT_LAMMPS = hartree/np.power(bohr,2.0) # eV/Angs

def comments():
    print ("unit converting..")

def begin():
    print ("begin")

def end():
    print ("end")

comments()

# main
begin()

# KC
for i in range(-1, 2, 1): # xloop
    for j in range(-1, 2, 1): # yloop

        KC = pd.read_csv("../abinit/total_mat_C/KC_"+str(i)+str(j)+".txt", sep='\s+', header=None)
        KC = KC*ABINIT_LAMMPS # unit conversion
        row,col = KC.shape # get row & column of matorix

        f1 = open("../abinit/total_mat_C/LAMMPS_unit/KC_"+str(i)+str(j)+".txt", 'w') # write mode
        for k in range(0, row): # 48
            for l in range(0, col): # 48
                f1.write(str(KC[l][k])) # l & k are flipped maybe due to pd.read specification
                f1.write(str(' '))
            f1.write('\n')

# end
f1.close
end()

# time display
elapsed_time = time.time()-start
print("elapsed_time:{:.2f}".format(elapsed_time) + "[sec]")
