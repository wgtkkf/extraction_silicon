 # split ABINIT output into each files of generic atoms
# Coded by Takuro TOKUNAGA
# Last modified: August 10 2020

# parameter info:
# file name of 'f1' and 'full_length '
# atom_num

import time
import os
import glob

start = time.time()

def begin():
    print ("begin")

def comments():
    print ("removing txt files..")

def end():
    print ("end")

path_abinit = "../abinit/"

# comments
comments()

# main
begin()

# remove txt files at
# small_mat
# small_mat_center
# total_mat_C, L, and R
# LAMMPS_unit of total_mat_C, L, and R
for file in glob.glob(path_abinit + 'small_mat/*.txt', recursive=True):
    os.remove(file)

for file in glob.glob(path_abinit + 'small_mat_center/general/*.txt', recursive=True):
    os.remove(file)

for file in glob.glob(path_abinit + 'total_mat_C/*.txt', recursive=True):
    os.remove(file)

for file in glob.glob(path_abinit + 'total_mat_L/*.txt', recursive=True):
    os.remove(file)

for file in glob.glob(path_abinit + 'total_mat_R/*.txt', recursive=True):
    os.remove(file)

# LAMMPS unit folder
for file in glob.glob(path_abinit + 'total_mat_C/LAMMPS_unit/*.txt', recursive=True):
    os.remove(file)

for file in glob.glob(path_abinit + 'total_mat_L/LAMMPS_unit/*.txt', recursive=True):
    os.remove(file)

for file in glob.glob(path_abinit + 'total_mat_R/LAMMPS_unit/*.txt', recursive=True):
    os.remove(file)

# end
end()

# time display
elapsed_time = time.time()-start
print("elapsed_time:{:.2f}".format(elapsed_time) + "[sec]")
