# force constant matrix generation code from ABINIT output
# Coded by Takuro TOKUNAGA
# Last modified: August 15 2019

import numpy as np
import shutil
import os
import time

start = time.time()

def begin():
    print ("begin")

def comments():
    print ("copy & rename..")

def end():
    print ("end")

# comments
comments()

# main
begin()

# V

for i in range(-1, 2, 1): # zloop
    for j in range(-1, 2, 1): # xloop
        for k in range(-1, 2, 1): # yloop
            if i==-1:
                # copy V_CL for K01L, R
                shutil.copy("../abinit/total_mat_C/LAMMPS_unit/V_CL_"+str(j)+str(k)+".txt",\
                "../abinit/total_mat_L/LAMMPS_unit/K01L_"+str(j)+str(k)+".txt")   # from to
                
                shutil.copy("../abinit/total_mat_C/LAMMPS_unit/V_CL_"+str(j)+str(k)+".txt",\
                "../abinit/total_mat_R/LAMMPS_unit/K01R_"+str(j)+str(k)+".txt")   # from to
            elif i==0:
                # copy KC for K00L, R
                shutil.copy("../abinit/total_mat_C/LAMMPS_unit/KC_"+str(j)+str(k)+".txt",\
                "../abinit/total_mat_L/LAMMPS_unit/K00L_"+str(j)+str(k)+".txt")   # from to
                
                shutil.copy("../abinit/total_mat_C/LAMMPS_unit/KC_"+str(j)+str(k)+".txt",\
                "../abinit/total_mat_R/LAMMPS_unit/K00R_"+str(j)+str(k)+".txt")   # from to
            else:
                # copy V_CR for K10L, R
                shutil.copy("../abinit/total_mat_C/LAMMPS_unit/V_CR_"+str(j)+str(k)+".txt",\
                "../abinit/total_mat_L/LAMMPS_unit/K10L_"+str(j)+str(k)+".txt")   # from to
                
                shutil.copy("../abinit/total_mat_C/LAMMPS_unit/V_CR_"+str(j)+str(k)+".txt",\
                "../abinit/total_mat_R/LAMMPS_unit/K10R_"+str(j)+str(k)+".txt")   # from to

# end
end()

# time display
elapsed_time = time.time()-start
print("elapsed_time:{:.2f}".format(elapsed_time) + "[sec]")
