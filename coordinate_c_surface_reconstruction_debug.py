# Coded by Takuro TOKUNAGA
# Force constant matrices only for central region
# Last modified: October 01, 2020
# Updated: November 09, 2020

import numpy as np
import time
import sys
import copy
sys.path.append('../abinit/')
from fcmat_c_general_GA1_function  import GA1  # import function
from fcmat_c_general_GA2_function  import GA2  # import function
from fcmat_c_general_GA3_function  import GA3  # import function
from fcmat_c_general_GA4_function  import GA4  # import function
from fcmat_c_general_GA5_function  import GA5  # import function
from fcmat_c_general_GA6_function  import GA6  # import function
from fcmat_c_general_GA7_function  import GA7  # import function
from fcmat_c_general_GA8_function  import GA8  # import function
from fcmat_c_general_GA9_function  import GA9  # import function
from fcmat_c_general_GA10_function import GA10 # import function
from fcmat_c_general_GA11_function import GA11 # import function
from fcmat_c_general_GA12_function import GA12 # import function
from fcmat_c_general_GA13_function import GA13 # import function
from fcmat_c_general_GA14_function import GA14 # import function
from fcmat_c_general_GA15_function import GA15 # import function
from fcmat_c_general_GA16_function import GA16 # import function
from coordinate_adjustment_general import adjustment # import function

start = time.time()

def begin():
    print ("begin")

def comments():
    print ("extracting..")

def end():
    print ("end")

def debug():
    print ("debugging..")

# comments
comments()

# main
begin()

# unit conversion
ucangs = 1.0*np.power(10.,-10) # [m]
ucbohr = 0.529177249*ucangs    # [m]

# lattice constant of Si
dof = 3                        # [-], dgree of freedom
lcsi = 5.480*ucangs            # [m], don't change
lcsi_bohr = lcsi/ucbohr        # [bohr] 4/4

# read generic coordinates from ABINIT output
generic_coordinates_output=[list(map(np.float64,line.rstrip().split(" "))) for line in open("ABINIT_generic_atoms_coordinates_output.txt").readlines()]
generic_coordinates_L_output=[list(map(np.float64,line.rstrip().split(" "))) for line in open("ABINIT_generic_atoms_coordinates_output_L.txt").readlines()]
generic_coordinates_R_output=[list(map(np.float64,line.rstrip().split(" "))) for line in open("ABINIT_generic_atoms_coordinates_output_R.txt").readlines()]

# primitive cell atom's coordinates, left cells (cell #2, #3)
ab_coordinate_L1 = np.zeros(dof, dtype='float64')
ab_coordinate_L2 = np.zeros(dof, dtype='float64')
ab_coordinate_L3 = np.zeros(dof, dtype='float64')
ab_coordinate_L4 = np.zeros(dof, dtype='float64')
ab_coordinate_L5 = np.zeros(dof, dtype='float64')
ab_coordinate_L6 = np.zeros(dof, dtype='float64')
ab_coordinate_L7 = np.zeros(dof, dtype='float64')
ab_coordinate_L8 = np.zeros(dof, dtype='float64')
ab_coordinate_L9 = np.zeros(dof, dtype='float64')
ab_coordinate_L10 = np.zeros(dof, dtype='float64')
ab_coordinate_L11 = np.zeros(dof, dtype='float64')
ab_coordinate_L12 = np.zeros(dof, dtype='float64')
ab_coordinate_L13 = np.zeros(dof, dtype='float64')
ab_coordinate_L14 = np.zeros(dof, dtype='float64')
ab_coordinate_L15 = np.zeros(dof, dtype='float64')
ab_coordinate_L16 = np.zeros(dof, dtype='float64')

# primitive cell atom's coordinates, right cells (cell #6, #7)
ab_coordinate_R1 = np.zeros(dof, dtype='float64')
ab_coordinate_R2 = np.zeros(dof, dtype='float64')
ab_coordinate_R3 = np.zeros(dof, dtype='float64')
ab_coordinate_R4 = np.zeros(dof, dtype='float64')
ab_coordinate_R5 = np.zeros(dof, dtype='float64')
ab_coordinate_R6 = np.zeros(dof, dtype='float64')
ab_coordinate_R7 = np.zeros(dof, dtype='float64')
ab_coordinate_R8 = np.zeros(dof, dtype='float64')
ab_coordinate_R9 = np.zeros(dof, dtype='float64')
ab_coordinate_R10 = np.zeros(dof, dtype='float64')
ab_coordinate_R11 = np.zeros(dof, dtype='float64')
ab_coordinate_R12 = np.zeros(dof, dtype='float64')
ab_coordinate_R13 = np.zeros(dof, dtype='float64')
ab_coordinate_R14 = np.zeros(dof, dtype='float64')
ab_coordinate_R15 = np.zeros(dof, dtype='float64')
ab_coordinate_R16 = np.zeros(dof, dtype='float64')

# primitive cell atom's coordinates by ABNINIT output, centrale cells (cell #4, #5)
ab_coordinate1 = np.zeros(dof, dtype='float64')
ab_coordinate2 = np.zeros(dof, dtype='float64')
ab_coordinate3 = np.zeros(dof, dtype='float64')
ab_coordinate4 = np.zeros(dof, dtype='float64')
ab_coordinate5 = np.zeros(dof, dtype='float64')
ab_coordinate6 = np.zeros(dof, dtype='float64')
ab_coordinate7 = np.zeros(dof, dtype='float64')
ab_coordinate8 = np.zeros(dof, dtype='float64')
ab_coordinate9 = np.zeros(dof, dtype='float64')
ab_coordinate10 = np.zeros(dof, dtype='float64')
ab_coordinate11 = np.zeros(dof, dtype='float64')
ab_coordinate12 = np.zeros(dof, dtype='float64')
ab_coordinate13 = np.zeros(dof, dtype='float64')
ab_coordinate14 = np.zeros(dof, dtype='float64')
ab_coordinate15 = np.zeros(dof, dtype='float64')
ab_coordinate16 = np.zeros(dof, dtype='float64')

# initialization of generic coordinates
# this part will be used for shift factor calculation
for i in range(0, dof):
    ###
    # output by ABINIT (left region, cell #2 & #3)
    # left side
    ab_coordinate_L1[i] = generic_coordinates_L_output[0][i] # 1
    ab_coordinate_L2[i] = generic_coordinates_L_output[1][i] # 2
    ab_coordinate_L3[i] = generic_coordinates_L_output[2][i] # 3
    ab_coordinate_L4[i] = generic_coordinates_L_output[3][i] # 4
    ab_coordinate_L5[i] = generic_coordinates_L_output[4][i] # 5
    ab_coordinate_L6[i] = generic_coordinates_L_output[5][i] # 6
    ab_coordinate_L7[i] = generic_coordinates_L_output[6][i] # 7
    ab_coordinate_L8[i] = generic_coordinates_L_output[7][i] # 8

    # right side
    ab_coordinate_L9[i]  = generic_coordinates_L_output[8][i]  # 9
    ab_coordinate_L10[i] = generic_coordinates_L_output[9][i]  # 10
    ab_coordinate_L11[i] = generic_coordinates_L_output[10][i] # 11
    ab_coordinate_L12[i] = generic_coordinates_L_output[11][i] # 12
    ab_coordinate_L13[i] = generic_coordinates_L_output[12][i] # 13
    ab_coordinate_L14[i] = generic_coordinates_L_output[13][i] # 14
    ab_coordinate_L15[i] = generic_coordinates_L_output[14][i] # 15
    ab_coordinate_L16[i] = generic_coordinates_L_output[15][i] # 16

    # output by ABINIT
    # left side of centrale region (cell #4)
    ab_coordinate1[i] = generic_coordinates_output[0][i] # 1
    ab_coordinate2[i] = generic_coordinates_output[1][i] # 2
    ab_coordinate3[i] = generic_coordinates_output[2][i] # 3
    ab_coordinate4[i] = generic_coordinates_output[3][i] # 4
    ab_coordinate5[i] = generic_coordinates_output[4][i] # 5
    ab_coordinate6[i] = generic_coordinates_output[5][i] # 6
    ab_coordinate7[i] = generic_coordinates_output[6][i] # 7
    ab_coordinate8[i] = generic_coordinates_output[7][i] # 8

    # right side of centrale region (cell #5)
    ab_coordinate9[i]  = generic_coordinates_output[8][i]  # 9
    ab_coordinate10[i] = generic_coordinates_output[9][i]  # 10
    ab_coordinate11[i] = generic_coordinates_output[10][i] # 11
    ab_coordinate12[i] = generic_coordinates_output[11][i] # 12
    ab_coordinate13[i] = generic_coordinates_output[12][i] # 13
    ab_coordinate14[i] = generic_coordinates_output[13][i] # 14
    ab_coordinate15[i] = generic_coordinates_output[14][i] # 15
    ab_coordinate16[i] = generic_coordinates_output[15][i] # 16

    ###
    # output by ABINIT (right region, cell #6 & #7)
    # left side
    ab_coordinate_R1[i] = generic_coordinates_R_output[0][i] # 1
    ab_coordinate_R2[i] = generic_coordinates_R_output[1][i] # 2
    ab_coordinate_R3[i] = generic_coordinates_R_output[2][i] # 3
    ab_coordinate_R4[i] = generic_coordinates_R_output[3][i] # 4
    ab_coordinate_R5[i] = generic_coordinates_R_output[4][i] # 5
    ab_coordinate_R6[i] = generic_coordinates_R_output[5][i] # 6
    ab_coordinate_R7[i] = generic_coordinates_R_output[6][i] # 7
    ab_coordinate_R8[i] = generic_coordinates_R_output[7][i] # 8

    # right side
    ab_coordinate_R9[i]  = generic_coordinates_R_output[8][i]  # 9
    ab_coordinate_R10[i] = generic_coordinates_R_output[9][i]  # 10
    ab_coordinate_R11[i] = generic_coordinates_R_output[10][i] # 11
    ab_coordinate_R12[i] = generic_coordinates_R_output[11][i] # 12
    ab_coordinate_R13[i] = generic_coordinates_R_output[12][i] # 13
    ab_coordinate_R14[i] = generic_coordinates_R_output[13][i] # 14
    ab_coordinate_R15[i] = generic_coordinates_R_output[14][i] # 15
    ab_coordinate_R16[i] = generic_coordinates_R_output[15][i] # 16

# s_: shift
s_coordinate1 = np.zeros(dof, dtype='float64')
s_coordinate2 = np.zeros(dof, dtype='float64')
s_coordinate3 = np.zeros(dof, dtype='float64')
s_coordinate4 = np.zeros(dof, dtype='float64')
s_coordinate5 = np.zeros(dof, dtype='float64')
s_coordinate6 = np.zeros(dof, dtype='float64')
s_coordinate7 = np.zeros(dof, dtype='float64')
s_coordinate8 = np.zeros(dof, dtype='float64')
s_coordinate9 = np.zeros(dof, dtype='float64')
s_coordinate10 = np.zeros(dof, dtype='float64')
s_coordinate11 = np.zeros(dof, dtype='float64')
s_coordinate12 = np.zeros(dof, dtype='float64')
s_coordinate13 = np.zeros(dof, dtype='float64')
s_coordinate14 = np.zeros(dof, dtype='float64')
s_coordinate15 = np.zeros(dof, dtype='float64')
s_coordinate16 = np.zeros(dof, dtype='float64')

# extraction start
# z direction translation
for n in range(-1, 2, 1): # zloop (-1 -> 0 -> +1)
    # skip n=-1
    #if n==-1:
    #    continue

    if n==-1: # left (cell # 2,3)
        # non-shift coordinates, prepared by excel
        s_coordinate1 = copy.deepcopy(ab_coordinate_L1)
        s_coordinate2 = copy.deepcopy(ab_coordinate_L2)
        s_coordinate3 = copy.deepcopy(ab_coordinate_L3)
        s_coordinate4 = copy.deepcopy(ab_coordinate_L4)
        s_coordinate5 = copy.deepcopy(ab_coordinate_L5)
        s_coordinate6 = copy.deepcopy(ab_coordinate_L6)
        s_coordinate7 = copy.deepcopy(ab_coordinate_L7)
        s_coordinate8 = copy.deepcopy(ab_coordinate_L8)

        s_coordinate9 = copy.deepcopy(ab_coordinate_L9)
        s_coordinate10 = copy.deepcopy(ab_coordinate_L10)
        s_coordinate11 = copy.deepcopy(ab_coordinate_L11)
        s_coordinate12 = copy.deepcopy(ab_coordinate_L12)
        s_coordinate13 = copy.deepcopy(ab_coordinate_L13)
        s_coordinate14 = copy.deepcopy(ab_coordinate_L14)
        s_coordinate15 = copy.deepcopy(ab_coordinate_L15)
        s_coordinate16 = copy.deepcopy(ab_coordinate_L16)

    elif n==0: # center (cell # 4,5)
        # non-shift coordinates, prepared by excel
        s_coordinate1 = copy.deepcopy(ab_coordinate1)
        s_coordinate2 = copy.deepcopy(ab_coordinate2)
        s_coordinate3 = copy.deepcopy(ab_coordinate3)
        s_coordinate4 = copy.deepcopy(ab_coordinate4)
        s_coordinate5 = copy.deepcopy(ab_coordinate5)
        s_coordinate6 = copy.deepcopy(ab_coordinate6)
        s_coordinate7 = copy.deepcopy(ab_coordinate7)
        s_coordinate8 = copy.deepcopy(ab_coordinate8)
        # gap is here
        s_coordinate9 = copy.deepcopy(ab_coordinate9)
        s_coordinate10 = copy.deepcopy(ab_coordinate10)
        s_coordinate11 = copy.deepcopy(ab_coordinate11)
        s_coordinate12 = copy.deepcopy(ab_coordinate12)
        s_coordinate13 = copy.deepcopy(ab_coordinate13)
        s_coordinate14 = copy.deepcopy(ab_coordinate14)
        s_coordinate15 = copy.deepcopy(ab_coordinate15)
        s_coordinate16 = copy.deepcopy(ab_coordinate16)

    elif n==1: # n=1, right (cell # 6,7)
        # non-shift coordinates, prepared by excel
        s_coordinate1 = copy.deepcopy(ab_coordinate_R1)
        s_coordinate2 = copy.deepcopy(ab_coordinate_R2)
        s_coordinate3 = copy.deepcopy(ab_coordinate_R3)
        s_coordinate4 = copy.deepcopy(ab_coordinate_R4)
        s_coordinate5 = copy.deepcopy(ab_coordinate_R5)
        s_coordinate6 = copy.deepcopy(ab_coordinate_R6)
        s_coordinate7 = copy.deepcopy(ab_coordinate_R7)
        s_coordinate8 = copy.deepcopy(ab_coordinate_R8)
        s_coordinate9 = copy.deepcopy(ab_coordinate_R9)

        s_coordinate10 = copy.deepcopy(ab_coordinate_R10)
        s_coordinate11 = copy.deepcopy(ab_coordinate_R11)
        s_coordinate12 = copy.deepcopy(ab_coordinate_R12)
        s_coordinate13 = copy.deepcopy(ab_coordinate_R13)
        s_coordinate14 = copy.deepcopy(ab_coordinate_R14)
        s_coordinate15 = copy.deepcopy(ab_coordinate_R15)
        s_coordinate16 = copy.deepcopy(ab_coordinate_R16)

    #print(s_coordinate1)

    for i in range(-1, 2, 1): # xloop (-1 -> 0 -> +1)
        # skip i=-1
        #if i==-1:
        #    continue

        # x direction
        s_coordinate1[0] += i*lcsi_bohr
        s_coordinate2[0] += i*lcsi_bohr
        s_coordinate3[0] += i*lcsi_bohr
        s_coordinate4[0] += i*lcsi_bohr
        s_coordinate5[0] += i*lcsi_bohr
        s_coordinate6[0] += i*lcsi_bohr
        s_coordinate7[0] += i*lcsi_bohr
        s_coordinate8[0] += i*lcsi_bohr
        s_coordinate9[0] += i*lcsi_bohr
        s_coordinate10[0] += i*lcsi_bohr
        s_coordinate11[0] += i*lcsi_bohr
        s_coordinate12[0] += i*lcsi_bohr
        s_coordinate13[0] += i*lcsi_bohr
        s_coordinate14[0] += i*lcsi_bohr
        s_coordinate15[0] += i*lcsi_bohr
        s_coordinate16[0] += i*lcsi_bohr

        for j in range(-1, 2, 1): # yloop (-1 -> 0 -> +1)
            # skip i=-1
            #if j==-1:
            #    continue

            # y direction
            s_coordinate1[1] += j*lcsi_bohr
            s_coordinate2[1] += j*lcsi_bohr
            s_coordinate3[1] += j*lcsi_bohr
            s_coordinate4[1] += j*lcsi_bohr
            s_coordinate5[1] += j*lcsi_bohr
            s_coordinate6[1] += j*lcsi_bohr
            s_coordinate7[1] += j*lcsi_bohr
            s_coordinate8[1] += j*lcsi_bohr
            s_coordinate9[1] += j*lcsi_bohr
            s_coordinate10[1] += j*lcsi_bohr
            s_coordinate11[1] += j*lcsi_bohr
            s_coordinate12[1] += j*lcsi_bohr
            s_coordinate13[1] += j*lcsi_bohr
            s_coordinate14[1] += j*lcsi_bohr
            s_coordinate15[1] += j*lcsi_bohr
            s_coordinate16[1] += j*lcsi_bohr

            #print("n:{:.0f}".format(n) + "[-]")
            #print("j:{:.0f}".format(j) + "[-]")
            #print(s_coordinate1)

            # Call GA functions
            # GA1
            GA1(i,j,n, adjustment(s_coordinate1), adjustment(s_coordinate2)\
            ,adjustment(s_coordinate3), adjustment(s_coordinate4), adjustment(s_coordinate5)\
            ,adjustment(s_coordinate6), adjustment(s_coordinate7), adjustment(s_coordinate8)\
            ,adjustment(s_coordinate9), adjustment(s_coordinate10), adjustment(s_coordinate11)\
            ,adjustment(s_coordinate12), adjustment(s_coordinate13), adjustment(s_coordinate14)\
            ,adjustment(s_coordinate15), adjustment(s_coordinate16))

            # initialize to primitive cell coordinate, y direction
            for k in range(0, dof): # yloop
                if k==1:
                    if n==-1:
                        s_coordinate1[k] = copy.deepcopy(ab_coordinate_L1[k])
                        s_coordinate2[k] = copy.deepcopy(ab_coordinate_L2[k])
                        s_coordinate3[k] = copy.deepcopy(ab_coordinate_L3[k])
                        s_coordinate4[k] = copy.deepcopy(ab_coordinate_L4[k])
                        s_coordinate5[k] = copy.deepcopy(ab_coordinate_L5[k])
                        s_coordinate6[k] = copy.deepcopy(ab_coordinate_L6[k])
                        s_coordinate7[k] = copy.deepcopy(ab_coordinate_L7[k])
                        s_coordinate8[k] = copy.deepcopy(ab_coordinate_L8[k])

                        s_coordinate9[k] = copy.deepcopy(ab_coordinate_L9[k])
                        s_coordinate10[k] = copy.deepcopy(ab_coordinate_L10[k])
                        s_coordinate11[k] = copy.deepcopy(ab_coordinate_L11[k])
                        s_coordinate12[k] = copy.deepcopy(ab_coordinate_L12[k])
                        s_coordinate13[k] = copy.deepcopy(ab_coordinate_L13[k])
                        s_coordinate14[k] = copy.deepcopy(ab_coordinate_L14[k])
                        s_coordinate15[k] = copy.deepcopy(ab_coordinate_L15[k])
                        s_coordinate16[k] = copy.deepcopy(ab_coordinate_L16[k])

                        #print('initialize')
                        #print(ab_coordinate_L1)
                    elif n==0: # center (cell # 4,5)
                        s_coordinate1[k] = copy.deepcopy(ab_coordinate1[k])
                        s_coordinate2[k] = copy.deepcopy(ab_coordinate2[k])
                        s_coordinate3[k] = copy.deepcopy(ab_coordinate3[k])
                        s_coordinate4[k] = copy.deepcopy(ab_coordinate4[k])
                        s_coordinate5[k] = copy.deepcopy(ab_coordinate5[k])
                        s_coordinate6[k] = copy.deepcopy(ab_coordinate6[k])
                        s_coordinate7[k] = copy.deepcopy(ab_coordinate7[k])
                        s_coordinate8[k] = copy.deepcopy(ab_coordinate8[k])
                        # gap is here
                        s_coordinate9[k] = copy.deepcopy(ab_coordinate9[k])
                        s_coordinate10[k] = copy.deepcopy(ab_coordinate10[k])
                        s_coordinate11[k] = copy.deepcopy(ab_coordinate11[k])
                        s_coordinate12[k] = copy.deepcopy(ab_coordinate12[k])
                        s_coordinate13[k] = copy.deepcopy(ab_coordinate13[k])
                        s_coordinate14[k] = copy.deepcopy(ab_coordinate14[k])
                        s_coordinate15[k] = copy.deepcopy(ab_coordinate15[k])
                        s_coordinate16[k] = copy.deepcopy(ab_coordinate16[k])

                    elif n==1: # n=1, right (cell # 6,7)
                        s_coordinate1[k] = copy.deepcopy(ab_coordinate_R1[k])
                        s_coordinate2[k] = copy.deepcopy(ab_coordinate_R2[k])
                        s_coordinate3[k] = copy.deepcopy(ab_coordinate_R3[k])
                        s_coordinate4[k] = copy.deepcopy(ab_coordinate_R4[k])
                        s_coordinate5[k] = copy.deepcopy(ab_coordinate_R5[k])
                        s_coordinate6[k] = copy.deepcopy(ab_coordinate_R6[k])
                        s_coordinate7[k] = copy.deepcopy(ab_coordinate_R7[k])
                        s_coordinate8[k] = copy.deepcopy(ab_coordinate_R8[k])
                        s_coordinate9[k] = copy.deepcopy(ab_coordinate_R9[k])

                        s_coordinate10[k] = copy.deepcopy(ab_coordinate_R10[k])
                        s_coordinate11[k] = copy.deepcopy(ab_coordinate_R11[k])
                        s_coordinate12[k] = copy.deepcopy(ab_coordinate_R12[k])
                        s_coordinate13[k] = copy.deepcopy(ab_coordinate_R13[k])
                        s_coordinate14[k] = copy.deepcopy(ab_coordinate_R14[k])
                        s_coordinate15[k] = copy.deepcopy(ab_coordinate_R15[k])
                        s_coordinate16[k] = copy.deepcopy(ab_coordinate_R16[k])
#            print(s_coordinate1)

        # initialize to primitive cell coordinate, x & y direction
        for l in range(0, dof): # x & y loop
            if l==0 or l==1:
                if n==-1:
                    s_coordinate1[l] = copy.deepcopy(ab_coordinate_L1[l])
                    s_coordinate2[l] = copy.deepcopy(ab_coordinate_L2[l])
                    s_coordinate3[l] = copy.deepcopy(ab_coordinate_L3[l])
                    s_coordinate4[l] = copy.deepcopy(ab_coordinate_L4[l])
                    s_coordinate5[l] = copy.deepcopy(ab_coordinate_L5[l])
                    s_coordinate6[l] = copy.deepcopy(ab_coordinate_L6[l])
                    s_coordinate7[l] = copy.deepcopy(ab_coordinate_L7[l])
                    s_coordinate8[l] = copy.deepcopy(ab_coordinate_L8[l])

                    s_coordinate9[l] = copy.deepcopy(ab_coordinate_L9[l])
                    s_coordinate10[l] = copy.deepcopy(ab_coordinate_L10[l])
                    s_coordinate11[l] = copy.deepcopy(ab_coordinate_L11[l])
                    s_coordinate12[l] = copy.deepcopy(ab_coordinate_L12[l])
                    s_coordinate13[l] = copy.deepcopy(ab_coordinate_L13[l])
                    s_coordinate14[l] = copy.deepcopy(ab_coordinate_L14[l])
                    s_coordinate15[l] = copy.deepcopy(ab_coordinate_L15[l])
                    s_coordinate16[l] = copy.deepcopy(ab_coordinate_L16[l])

                elif n==0: # center (cell # 4,5)
                    s_coordinate1[l] = copy.deepcopy(ab_coordinate1[l])
                    s_coordinate2[l] = copy.deepcopy(ab_coordinate2[l])
                    s_coordinate3[l] = copy.deepcopy(ab_coordinate3[l])
                    s_coordinate4[l] = copy.deepcopy(ab_coordinate4[l])
                    s_coordinate5[l] = copy.deepcopy(ab_coordinate5[l])
                    s_coordinate6[l] = copy.deepcopy(ab_coordinate6[l])
                    s_coordinate7[l] = copy.deepcopy(ab_coordinate7[l])
                    s_coordinate8[l] = copy.deepcopy(ab_coordinate8[l])
                    # gap is here
                    s_coordinate9[l] = copy.deepcopy(ab_coordinate9[l])
                    s_coordinate10[l] = copy.deepcopy(ab_coordinate10[l])
                    s_coordinate11[l] = copy.deepcopy(ab_coordinate11[l])
                    s_coordinate12[l] = copy.deepcopy(ab_coordinate12[l])
                    s_coordinate13[l] = copy.deepcopy(ab_coordinate13[l])
                    s_coordinate14[l] = copy.deepcopy(ab_coordinate14[l])
                    s_coordinate15[l] = copy.deepcopy(ab_coordinate15[l])
                    s_coordinate16[l] = copy.deepcopy(ab_coordinate16[l])

                elif n==1: # n=1, right (cell # 6,7)
                    s_coordinate1[l] = copy.deepcopy(ab_coordinate_R1[l])
                    s_coordinate2[l] = copy.deepcopy(ab_coordinate_R2[l])
                    s_coordinate3[l] = copy.deepcopy(ab_coordinate_R3[l])
                    s_coordinate4[l] = copy.deepcopy(ab_coordinate_R4[l])
                    s_coordinate5[l] = copy.deepcopy(ab_coordinate_R5[l])
                    s_coordinate6[l] = copy.deepcopy(ab_coordinate_R6[l])
                    s_coordinate7[l] = copy.deepcopy(ab_coordinate_R7[l])
                    s_coordinate8[l] = copy.deepcopy(ab_coordinate_R8[l])

                    s_coordinate9[l] = copy.deepcopy(ab_coordinate_R9[l])
                    s_coordinate10[l] = copy.deepcopy(ab_coordinate_R10[l])
                    s_coordinate11[l] = copy.deepcopy(ab_coordinate_R11[l])
                    s_coordinate12[l] = copy.deepcopy(ab_coordinate_R12[l])
                    s_coordinate13[l] = copy.deepcopy(ab_coordinate_R13[l])
                    s_coordinate14[l] = copy.deepcopy(ab_coordinate_R14[l])
                    s_coordinate15[l] = copy.deepcopy(ab_coordinate_R15[l])
                    s_coordinate16[l] = copy.deepcopy(ab_coordinate_R16[l])

    # initialize to primitive cell coordinate, x y z direction
    #for m in range(0, dof): # x, y & z loop

    # no need for z loop since initialization
    # since s_coordinate# is reset at the beginning

# end
end()

# time display
elapsed_time = time.time()-start
print("elapsed_time:{:.2f}".format(elapsed_time) + "[sec]")
