# force constant matrix generation code from ABINIT output
# Coded by Takuro TOKUNAGA
# Last modified: August 31 2020

import numpy as np
import pandas as pd
import time
#import scipy.io
#import itertools

start = time.time()

def comments():
    print ("merging..")

def begin():
    print ("begin")

def end():
    print ("end")

# main
begin()
comments()

dof = 3
atom_num = 16 # number of atom's in the primitive cell
size= atom_num*dof
matrix1=np.zeros((dof,dof), dtype=np.float64) # 3 3
matrix2=np.zeros((dof,dof), dtype=np.float64) # 3 3
matrix3=np.zeros((dof,dof), dtype=np.float64) # 3 3
matrix4=np.zeros((dof,dof), dtype=np.float64) # 3 3
matrix5=np.zeros((dof,dof), dtype=np.float64) # 3 3
matrix6=np.zeros((dof,dof), dtype=np.float64) # 3 3
matrix7=np.zeros((dof,dof), dtype=np.float64) # 3 3
matrix8=np.zeros((dof,dof), dtype=np.float64) # 3 3
matrix9=np.zeros((dof,dof), dtype=np.float64) # 3 3
matrix10=np.zeros((dof,dof), dtype=np.float64) # 3 3
matrix11=np.zeros((dof,dof), dtype=np.float64) # 3 3
matrix12=np.zeros((dof,dof), dtype=np.float64) # 3 3
matrix13=np.zeros((dof,dof), dtype=np.float64) # 3 3
matrix14=np.zeros((dof,dof), dtype=np.float64) # 3 3
matrix15=np.zeros((dof,dof), dtype=np.float64) # 3 3
matrix16=np.zeros((dof,dof), dtype=np.float64) # 3 3
mat_tot=np.zeros((size,size), dtype=np.float64) # 48 48

# read files
for n in range(-1, 2, 1): # zloop
    for o in range(-1, 2, 1): # xloop
        for p in range(-1, 2, 1): # yloop
            # open file for output
            if n==-1:
                f1 = open("../abinit/total_mat_C/V_CL_"+str(o)+str(p)+".txt", 'w') # write mode
            elif n==0:
                f1 = open("../abinit/total_mat_C/KC_"+str(o)+str(p)+".txt", 'w') # write mode
            else: # n==1
                f1 = open("../abinit/total_mat_C/V_CR_"+str(o)+str(p)+".txt", 'w') # write mode

            for i in range(0, atom_num): # 0~15
                if n==1: # flipped for some reason, originally -1
                    mat1 = pd.read_csv("../abinit/small_mat_center/general/si_4_Generic"+str(i+1)+"_Generic1_K10_"+str(o)+str(p)+".txt", sep='\s+', header=None)
                    mat1.columns = ["x", "y", "z", "x1", "y1", "z1", "x2", "y2", "z2"]
                    mat2 = pd.read_csv("../abinit/small_mat_center/general/si_4_Generic"+str(i+1)+"_Generic2_K10_"+str(o)+str(p)+".txt", sep='\s+', header=None)
                    mat2.columns = ["x", "y", "z", "x1", "y1", "z1", "x2", "y2", "z2"]
                    mat3 = pd.read_csv("../abinit/small_mat_center/general/si_4_Generic"+str(i+1)+"_Generic3_K10_"+str(o)+str(p)+".txt", sep='\s+', header=None)
                    mat3.columns = ["x", "y", "z", "x1", "y1", "z1", "x2", "y2", "z2"]
                    mat4 = pd.read_csv("../abinit/small_mat_center/general/si_4_Generic"+str(i+1)+"_Generic4_K10_"+str(o)+str(p)+".txt", sep='\s+', header=None)
                    mat4.columns = ["x", "y", "z", "x1", "y1", "z1", "x2", "y2", "z2"]
                    mat5 = pd.read_csv("../abinit/small_mat_center/general/si_4_Generic"+str(i+1)+"_Generic5_K10_"+str(o)+str(p)+".txt", sep='\s+', header=None)
                    mat5.columns = ["x", "y", "z", "x1", "y1", "z1", "x2", "y2", "z2"]
                    mat6 = pd.read_csv("../abinit/small_mat_center/general/si_4_Generic"+str(i+1)+"_Generic6_K10_"+str(o)+str(p)+".txt", sep='\s+', header=None)
                    mat6.columns = ["x", "y", "z", "x1", "y1", "z1", "x2", "y2", "z2"]
                    mat7 = pd.read_csv("../abinit/small_mat_center/general/si_4_Generic"+str(i+1)+"_Generic7_K10_"+str(o)+str(p)+".txt", sep='\s+', header=None)
                    mat7.columns = ["x", "y", "z", "x1", "y1", "z1", "x2", "y2", "z2"]
                    mat8 = pd.read_csv("../abinit/small_mat_center/general/si_4_Generic"+str(i+1)+"_Generic8_K10_"+str(o)+str(p)+".txt", sep='\s+', header=None)
                    mat8.columns = ["x", "y", "z", "x1", "y1", "z1", "x2", "y2", "z2"]

                    mat9 = pd.read_csv("../abinit/small_mat_center/general/si_4_Generic"+str(i+1)+"_Generic9_K10_"+str(o)+str(p)+".txt", sep='\s+', header=None)
                    mat9.columns = ["x", "y", "z", "x1", "y1", "z1", "x2", "y2", "z2"]
                    mat10 = pd.read_csv("../abinit/small_mat_center/general/si_4_Generic"+str(i+1)+"_Generic10_K10_"+str(o)+str(p)+".txt", sep='\s+', header=None)
                    mat10.columns = ["x", "y", "z", "x1", "y1", "z1", "x2", "y2", "z2"]
                    mat11 = pd.read_csv("../abinit/small_mat_center/general/si_4_Generic"+str(i+1)+"_Generic11_K10_"+str(o)+str(p)+".txt", sep='\s+', header=None)
                    mat11.columns = ["x", "y", "z", "x1", "y1", "z1", "x2", "y2", "z2"]
                    mat12 = pd.read_csv("../abinit/small_mat_center/general/si_4_Generic"+str(i+1)+"_Generic12_K10_"+str(o)+str(p)+".txt", sep='\s+', header=None)
                    mat12.columns = ["x", "y", "z", "x1", "y1", "z1", "x2", "y2", "z2"]
                    mat13 = pd.read_csv("../abinit/small_mat_center/general/si_4_Generic"+str(i+1)+"_Generic13_K10_"+str(o)+str(p)+".txt", sep='\s+', header=None)
                    mat13.columns = ["x", "y", "z", "x1", "y1", "z1", "x2", "y2", "z2"]
                    mat14 = pd.read_csv("../abinit/small_mat_center/general/si_4_Generic"+str(i+1)+"_Generic14_K10_"+str(o)+str(p)+".txt", sep='\s+', header=None)
                    mat14.columns = ["x", "y", "z", "x1", "y1", "z1", "x2", "y2", "z2"]
                    mat15 = pd.read_csv("../abinit/small_mat_center/general/si_4_Generic"+str(i+1)+"_Generic15_K10_"+str(o)+str(p)+".txt", sep='\s+', header=None)
                    mat15.columns = ["x", "y", "z", "x1", "y1", "z1", "x2", "y2", "z2"]
                    mat16 = pd.read_csv("../abinit/small_mat_center/general/si_4_Generic"+str(i+1)+"_Generic16_K10_"+str(o)+str(p)+".txt", sep='\s+', header=None)
                    mat16.columns = ["x", "y", "z", "x1", "y1", "z1", "x2", "y2", "z2"]

                elif n==0:
                    mat1 = pd.read_csv("../abinit/small_mat_center/general/si_4_Generic"+str(i+1)+"_Generic1_K00_"+str(o)+str(p)+".txt", sep='\s+', header=None)
                    mat1.columns = ["x", "y", "z", "x1", "y1", "z1", "x2", "y2", "z2"]
                    mat2 = pd.read_csv("../abinit/small_mat_center/general/si_4_Generic"+str(i+1)+"_Generic2_K00_"+str(o)+str(p)+".txt", sep='\s+', header=None)
                    mat2.columns = ["x", "y", "z", "x1", "y1", "z1", "x2", "y2", "z2"]
                    mat3 = pd.read_csv("../abinit/small_mat_center/general/si_4_Generic"+str(i+1)+"_Generic3_K00_"+str(o)+str(p)+".txt", sep='\s+', header=None)
                    mat3.columns = ["x", "y", "z", "x1", "y1", "z1", "x2", "y2", "z2"]
                    mat4 = pd.read_csv("../abinit/small_mat_center/general/si_4_Generic"+str(i+1)+"_Generic4_K00_"+str(o)+str(p)+".txt", sep='\s+', header=None)
                    mat4.columns = ["x", "y", "z", "x1", "y1", "z1", "x2", "y2", "z2"]
                    mat5 = pd.read_csv("../abinit/small_mat_center/general/si_4_Generic"+str(i+1)+"_Generic5_K00_"+str(o)+str(p)+".txt", sep='\s+', header=None)
                    mat5.columns = ["x", "y", "z", "x1", "y1", "z1", "x2", "y2", "z2"]
                    mat6 = pd.read_csv("../abinit/small_mat_center/general/si_4_Generic"+str(i+1)+"_Generic6_K00_"+str(o)+str(p)+".txt", sep='\s+', header=None)
                    mat6.columns = ["x", "y", "z", "x1", "y1", "z1", "x2", "y2", "z2"]
                    mat7 = pd.read_csv("../abinit/small_mat_center/general/si_4_Generic"+str(i+1)+"_Generic7_K00_"+str(o)+str(p)+".txt", sep='\s+', header=None)
                    mat7.columns = ["x", "y", "z", "x1", "y1", "z1", "x2", "y2", "z2"]
                    mat8 = pd.read_csv("../abinit/small_mat_center/general/si_4_Generic"+str(i+1)+"_Generic8_K00_"+str(o)+str(p)+".txt", sep='\s+', header=None)
                    mat8.columns = ["x", "y", "z", "x1", "y1", "z1", "x2", "y2", "z2"]

                    mat9 = pd.read_csv("../abinit/small_mat_center/general/si_4_Generic"+str(i+1)+"_Generic9_K00_"+str(o)+str(p)+".txt", sep='\s+', header=None)
                    mat9.columns = ["x", "y", "z", "x1", "y1", "z1", "x2", "y2", "z2"]
                    mat10 = pd.read_csv("../abinit/small_mat_center/general/si_4_Generic"+str(i+1)+"_Generic10_K00_"+str(o)+str(p)+".txt", sep='\s+', header=None)
                    mat10.columns = ["x", "y", "z", "x1", "y1", "z1", "x2", "y2", "z2"]
                    mat11 = pd.read_csv("../abinit/small_mat_center/general/si_4_Generic"+str(i+1)+"_Generic11_K00_"+str(o)+str(p)+".txt", sep='\s+', header=None)
                    mat11.columns = ["x", "y", "z", "x1", "y1", "z1", "x2", "y2", "z2"]
                    mat12 = pd.read_csv("../abinit/small_mat_center/general/si_4_Generic"+str(i+1)+"_Generic12_K00_"+str(o)+str(p)+".txt", sep='\s+', header=None)
                    mat12.columns = ["x", "y", "z", "x1", "y1", "z1", "x2", "y2", "z2"]
                    mat13 = pd.read_csv("../abinit/small_mat_center/general/si_4_Generic"+str(i+1)+"_Generic13_K00_"+str(o)+str(p)+".txt", sep='\s+', header=None)
                    mat13.columns = ["x", "y", "z", "x1", "y1", "z1", "x2", "y2", "z2"]
                    mat14 = pd.read_csv("../abinit/small_mat_center/general/si_4_Generic"+str(i+1)+"_Generic14_K00_"+str(o)+str(p)+".txt", sep='\s+', header=None)
                    mat14.columns = ["x", "y", "z", "x1", "y1", "z1", "x2", "y2", "z2"]
                    mat15 = pd.read_csv("../abinit/small_mat_center/general/si_4_Generic"+str(i+1)+"_Generic15_K00_"+str(o)+str(p)+".txt", sep='\s+', header=None)
                    mat15.columns = ["x", "y", "z", "x1", "y1", "z1", "x2", "y2", "z2"]
                    mat16 = pd.read_csv("../abinit/small_mat_center/general/si_4_Generic"+str(i+1)+"_Generic16_K00_"+str(o)+str(p)+".txt", sep='\s+', header=None)
                    mat16.columns = ["x", "y", "z", "x1", "y1", "z1", "x2", "y2", "z2"]
                else: # n==-1
                    mat1 = pd.read_csv("../abinit/small_mat_center/general/si_4_Generic"+str(i+1)+"_Generic1_K01_"+str(o)+str(p)+".txt", sep='\s+', header=None)
                    mat1.columns = ["x", "y", "z", "x1", "y1", "z1", "x2", "y2", "z2"]
                    mat2 = pd.read_csv("../abinit/small_mat_center/general/si_4_Generic"+str(i+1)+"_Generic2_K01_"+str(o)+str(p)+".txt", sep='\s+', header=None)
                    mat2.columns = ["x", "y", "z", "x1", "y1", "z1", "x2", "y2", "z2"]
                    mat3 = pd.read_csv("../abinit/small_mat_center/general/si_4_Generic"+str(i+1)+"_Generic3_K01_"+str(o)+str(p)+".txt", sep='\s+', header=None)
                    mat3.columns = ["x", "y", "z", "x1", "y1", "z1", "x2", "y2", "z2"]
                    mat4 = pd.read_csv("../abinit/small_mat_center/general/si_4_Generic"+str(i+1)+"_Generic4_K01_"+str(o)+str(p)+".txt", sep='\s+', header=None)
                    mat4.columns = ["x", "y", "z", "x1", "y1", "z1", "x2", "y2", "z2"]
                    mat5 = pd.read_csv("../abinit/small_mat_center/general/si_4_Generic"+str(i+1)+"_Generic5_K01_"+str(o)+str(p)+".txt", sep='\s+', header=None)
                    mat5.columns = ["x", "y", "z", "x1", "y1", "z1", "x2", "y2", "z2"]
                    mat6 = pd.read_csv("../abinit/small_mat_center/general/si_4_Generic"+str(i+1)+"_Generic6_K01_"+str(o)+str(p)+".txt", sep='\s+', header=None)
                    mat6.columns = ["x", "y", "z", "x1", "y1", "z1", "x2", "y2", "z2"]
                    mat7 = pd.read_csv("../abinit/small_mat_center/general/si_4_Generic"+str(i+1)+"_Generic7_K01_"+str(o)+str(p)+".txt", sep='\s+', header=None)
                    mat7.columns = ["x", "y", "z", "x1", "y1", "z1", "x2", "y2", "z2"]
                    mat8 = pd.read_csv("../abinit/small_mat_center/general/si_4_Generic"+str(i+1)+"_Generic8_K01_"+str(o)+str(p)+".txt", sep='\s+', header=None)
                    mat8.columns = ["x", "y", "z", "x1", "y1", "z1", "x2", "y2", "z2"]

                    mat9 = pd.read_csv("../abinit/small_mat_center/general/si_4_Generic"+str(i+1)+"_Generic9_K01_"+str(o)+str(p)+".txt", sep='\s+', header=None)
                    mat9.columns = ["x", "y", "z", "x1", "y1", "z1", "x2", "y2", "z2"]
                    mat10 = pd.read_csv("../abinit/small_mat_center/general/si_4_Generic"+str(i+1)+"_Generic10_K01_"+str(o)+str(p)+".txt", sep='\s+', header=None)
                    mat10.columns = ["x", "y", "z", "x1", "y1", "z1", "x2", "y2", "z2"]
                    mat11 = pd.read_csv("../abinit/small_mat_center/general/si_4_Generic"+str(i+1)+"_Generic11_K01_"+str(o)+str(p)+".txt", sep='\s+', header=None)
                    mat11.columns = ["x", "y", "z", "x1", "y1", "z1", "x2", "y2", "z2"]
                    mat12 = pd.read_csv("../abinit/small_mat_center/general/si_4_Generic"+str(i+1)+"_Generic12_K01_"+str(o)+str(p)+".txt", sep='\s+', header=None)
                    mat12.columns = ["x", "y", "z", "x1", "y1", "z1", "x2", "y2", "z2"]
                    mat13 = pd.read_csv("../abinit/small_mat_center/general/si_4_Generic"+str(i+1)+"_Generic13_K01_"+str(o)+str(p)+".txt", sep='\s+', header=None)
                    mat13.columns = ["x", "y", "z", "x1", "y1", "z1", "x2", "y2", "z2"]
                    mat14 = pd.read_csv("../abinit/small_mat_center/general/si_4_Generic"+str(i+1)+"_Generic14_K01_"+str(o)+str(p)+".txt", sep='\s+', header=None)
                    mat14.columns = ["x", "y", "z", "x1", "y1", "z1", "x2", "y2", "z2"]
                    mat15 = pd.read_csv("../abinit/small_mat_center/general/si_4_Generic"+str(i+1)+"_Generic15_K01_"+str(o)+str(p)+".txt", sep='\s+', header=None)
                    mat15.columns = ["x", "y", "z", "x1", "y1", "z1", "x2", "y2", "z2"]
                    mat16 = pd.read_csv("../abinit/small_mat_center/general/si_4_Generic"+str(i+1)+"_Generic16_K01_"+str(o)+str(p)+".txt", sep='\s+', header=None)
                    mat16.columns = ["x", "y", "z", "x1", "y1", "z1", "x2", "y2", "z2"]

                row,col = mat1.shape # row (3) & column (9) of matorix

                for j in range(0, row):
                    for k in range(0, row):
                        matrix1[j][k] = mat1.iat[j,k]
                        matrix2[j][k] = mat2.iat[j,k]
                        matrix3[j][k] = mat3.iat[j,k]
                        matrix4[j][k] = mat4.iat[j,k]
                        matrix5[j][k] = mat5.iat[j,k]
                        matrix6[j][k] = mat6.iat[j,k]
                        matrix7[j][k] = mat7.iat[j,k]
                        matrix8[j][k] = mat8.iat[j,k]

                        matrix9[j][k] = mat9.iat[j,k]
                        matrix10[j][k] = mat10.iat[j,k]
                        matrix11[j][k] = mat11.iat[j,k]
                        matrix12[j][k] = mat12.iat[j,k]
                        matrix13[j][k] = mat13.iat[j,k]
                        matrix14[j][k] = mat14.iat[j,k]
                        matrix15[j][k] = mat15.iat[j,k]
                        matrix16[j][k] = mat16.iat[j,k]

                #print(matrix2)
                mat_tot_temp = np.concatenate([matrix1, matrix2, matrix3, matrix4,matrix5, matrix6, matrix7, matrix8\
                ,matrix9, matrix10, matrix11, matrix12,matrix13, matrix14, matrix15, matrix16], axis=1)
                #print(mat_tot)

                row,col = mat_tot_temp.shape # row (3) & column (24) of matorix
                #print(str(row))
                #print(str(col))

                # mat_tot: 48*24 matrix
                for l in range(0, dof): # 3
                    for m in range(0, size): # 48
                        mat_tot[dof*i+l][m] = mat_tot_temp[l][m] # 48*3

            # mat_tot: 48*48 matrix
            for l in range(0, size): # 48
                for m in range(0, size): # 48
                    f1.write(str(mat_tot[l][m]))
                    f1.write(str(' '))
                f1.write('\n')

        # close
        f1.close

# end
end()

# time display
elapsed_time = time.time()-start
print("elapsed_time:{:.2f}".format(elapsed_time) + "[sec]")
