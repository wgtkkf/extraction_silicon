# Coded by Takuro TOKUNAGA
# Last modified: October 28 2020

import numpy as np
import time
import scipy.io
from numpy import linalg as LA

start = time.time()

# unit conversion
eV_J = 1.602176565*np.power(10.,-19)
A_m = 1.0*np.power(10.,-10)
Hz_THz = 1.0*np.power(10.,-12)
gmol_kg=1.0*np.power(10.,-3.0)/(6.02214129*np.power(10.,23.0));
scale=((eV_J/np.power(A_m,2.0))/gmol_kg)*np.power(Hz_THz,2.0)
#print(str(scale))

# parameters
size=48
threshold1 = 0.0001 #[]
threshold2 = 0.1 #[]

# scattering region
def enforceKC():

    for i in range(-1, 2, 1): # -1,0,+1
        for j in range(-1, 2, 1): # -1,0,+1
            kmatrix=np.zeros((size,size), dtype=np.complex)
            data = np.loadtxt("../abinit/total_mat_C/LAMMPS_unit/KC_"+str(i)+str(j)+".txt")
            kmatrix = data

            #K00
            if i==0 and j==0:
                diagonal = kmatrix[0][0]

                for k in range(0, size, 1): # 0,47,+1
                    for l in range(0, size, 1): # 0,47,+1
                        if k==l:
                            kmatrix[k][l] = diagonal

                            if k<size-1:
                                kmatrix[k][k+1] = 0
                                kmatrix[k+1][k] = 0
            # other
            #else:
            #    if abs(kmatrix[i][j]) < threshold1:
            #        kmatrix[i][j] = 0

            # output
            np.savetxt("../abinit/total_mat_C/LAMMPS_unit/KC_"+str(i)+str(j)+".txt", kmatrix, fmt="%0.12f", delimiter=" ")

    return 0

def enforceVCL():

    for i in range(-1, 2, 1): # -1,0,+1
        for j in range(-1, 2, 1): # -1,0,+1
            vlmatrix=np.zeros((size,size), dtype=np.complex)
            data = np.loadtxt("../abinit/total_mat_C/LAMMPS_unit/V_CL_"+str(i)+str(j)+".txt")
            vlmatrix = data

            #if abs(vlmatrix[i][j]) < threshold2:
            #    vlmatrix[i][j] = 0

            # output
            np.savetxt("../abinit/total_mat_C/LAMMPS_unit/V_CL_"+str(i)+str(j)+".txt", vlmatrix, fmt="%0.12f", delimiter=" ")

def enforceVCR():

    for i in range(-1, 2, 1): # -1,0,+1
        for j in range(-1, 2, 1): # -1,0,+1
            vrmatrix=np.zeros((size,size), dtype=np.complex)
            data = np.loadtxt("../abinit/total_mat_C/LAMMPS_unit/V_CR_"+str(i)+str(j)+".txt")
            vrmatrix = data

            #if abs(vrmatrix[i][j]) < threshold2:
            #    vrmatrix[i][j] = 0

            # output
            np.savetxt("../abinit/total_mat_C/LAMMPS_unit/V_CR_"+str(i)+str(j)+".txt", vrmatrix, fmt="%0.12f", delimiter=" ")

if __name__ == "__main__":
    enforceKC()
    enforceVCL()
    enforceVCR()

# time display
elapsed_time = time.time()-start
#print("elapsed_time:{:.2f}".format(elapsed_time) + "[sec]")
