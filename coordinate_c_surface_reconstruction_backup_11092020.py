# Coded by Takuro TOKUNAGA
# Force constant matrices only for central region
# Last modified: October 1, 2020

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
from coordinate_shift import shift             # import function

start = time.time()

def begin():
    print ("begin")

def comments():
    print ("extracting..")

def end():
    print ("end")

def debug():
    print ("debug")

# comments
comments()

# main
begin()

# unit conversion
ucangs = 1.0*np.power(10.,-10) # [m]
ucbohr = 0.529177249*ucangs    # [m]

# lattice constant of Si
dof = 3                        # [-], dgree of freedom
lcsi = 5.470*ucangs            # [m], don't change
lcsi_bohr = lcsi/ucbohr        # [bohr] 4/4

# read generic coordinates from ABINIT input
generic_coordinates_L_input=[list(map(np.float64,line.rstrip().split(" "))) for line in open("ABINIT_generic_atoms_coordinates_input_L.txt").readlines()]
generic_coordinates_input=[list(map(np.float64,line.rstrip().split(" "))) for line in open("ABINIT_generic_atoms_coordinates_input.txt").readlines()]
generic_coordinates_R_input=[list(map(np.float64,line.rstrip().split(" "))) for line in open("ABINIT_generic_atoms_coordinates_input_R.txt").readlines()]

# read generic coordinates from ABINIT output
generic_coordinates_output=[list(map(np.float64,line.rstrip().split(" "))) for line in open("ABINIT_generic_atoms_coordinates_output.txt").readlines()]

# primitive cell atom's coordinates, left cells (cell #2, #3)
coordinate_L1 = np.zeros(dof, dtype='float64')
coordinate_L2 = np.zeros(dof, dtype='float64')
coordinate_L3 = np.zeros(dof, dtype='float64')
coordinate_L4 = np.zeros(dof, dtype='float64')
coordinate_L5 = np.zeros(dof, dtype='float64')
coordinate_L6 = np.zeros(dof, dtype='float64')
coordinate_L7 = np.zeros(dof, dtype='float64')
coordinate_L8 = np.zeros(dof, dtype='float64')
coordinate_L9 = np.zeros(dof, dtype='float64')
coordinate_L10 = np.zeros(dof, dtype='float64')
coordinate_L11 = np.zeros(dof, dtype='float64')
coordinate_L12 = np.zeros(dof, dtype='float64')
coordinate_L13 = np.zeros(dof, dtype='float64')
coordinate_L14 = np.zeros(dof, dtype='float64')
coordinate_L15 = np.zeros(dof, dtype='float64')
coordinate_L16 = np.zeros(dof, dtype='float64')

# primitive cell atom's coordinates, centrale cells (cell #4, #5)
coordinate1 = np.zeros(dof, dtype='float64')
coordinate2 = np.zeros(dof, dtype='float64')
coordinate3 = np.zeros(dof, dtype='float64')
coordinate4 = np.zeros(dof, dtype='float64')
coordinate5 = np.zeros(dof, dtype='float64')
coordinate6 = np.zeros(dof, dtype='float64')
coordinate7 = np.zeros(dof, dtype='float64')
coordinate8 = np.zeros(dof, dtype='float64')
coordinate9 = np.zeros(dof, dtype='float64')
coordinate10 = np.zeros(dof, dtype='float64')
coordinate11 = np.zeros(dof, dtype='float64')
coordinate12 = np.zeros(dof, dtype='float64')
coordinate13 = np.zeros(dof, dtype='float64')
coordinate14 = np.zeros(dof, dtype='float64')
coordinate15 = np.zeros(dof, dtype='float64')
coordinate16 = np.zeros(dof, dtype='float64')

# primitive cell atom's coordinates, right cells (cell #6, #7)
coordinate_R1 = np.zeros(dof, dtype='float64')
coordinate_R2 = np.zeros(dof, dtype='float64')
coordinate_R3 = np.zeros(dof, dtype='float64')
coordinate_R4 = np.zeros(dof, dtype='float64')
coordinate_R5 = np.zeros(dof, dtype='float64')
coordinate_R6 = np.zeros(dof, dtype='float64')
coordinate_R7 = np.zeros(dof, dtype='float64')
coordinate_R8 = np.zeros(dof, dtype='float64')
coordinate_R9 = np.zeros(dof, dtype='float64')
coordinate_R10 = np.zeros(dof, dtype='float64')
coordinate_R11 = np.zeros(dof, dtype='float64')
coordinate_R12 = np.zeros(dof, dtype='float64')
coordinate_R13 = np.zeros(dof, dtype='float64')
coordinate_R14 = np.zeros(dof, dtype='float64')
coordinate_R15 = np.zeros(dof, dtype='float64')
coordinate_R16 = np.zeros(dof, dtype='float64')

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
    # input of ABINIT (left region, cell #2 & #3)
    # left side
    coordinate_L1[i] = generic_coordinates_L_input[0][i] # 1
    coordinate_L2[i] = generic_coordinates_L_input[1][i] # 2
    coordinate_L3[i] = generic_coordinates_L_input[2][i] # 3
    coordinate_L4[i] = generic_coordinates_L_input[3][i] # 4
    coordinate_L5[i] = generic_coordinates_L_input[4][i] # 5
    coordinate_L6[i] = generic_coordinates_L_input[5][i] # 6
    coordinate_L7[i] = generic_coordinates_L_input[6][i] # 7
    coordinate_L8[i] = generic_coordinates_L_input[7][i] # 8

    # right side
    coordinate_L9[i]  = generic_coordinates_L_input[8][i]  # 9
    coordinate_L10[i] = generic_coordinates_L_input[9][i]  # 10
    coordinate_L11[i] = generic_coordinates_L_input[10][i] # 11
    coordinate_L12[i] = generic_coordinates_L_input[11][i] # 12
    coordinate_L13[i] = generic_coordinates_L_input[12][i] # 13
    coordinate_L14[i] = generic_coordinates_L_input[13][i] # 14
    coordinate_L15[i] = generic_coordinates_L_input[14][i] # 15
    coordinate_L16[i] = generic_coordinates_L_input[15][i] # 16

    # input of ABINIT (centrale region, cell #4 & #5)
    # left side
    coordinate1[i] = generic_coordinates_input[0][i] # 1
    coordinate2[i] = generic_coordinates_input[1][i] # 2
    coordinate3[i] = generic_coordinates_input[2][i] # 3
    coordinate4[i] = generic_coordinates_input[3][i] # 4
    coordinate5[i] = generic_coordinates_input[4][i] # 5
    coordinate6[i] = generic_coordinates_input[5][i] # 6
    coordinate7[i] = generic_coordinates_input[6][i] # 7
    coordinate8[i] = generic_coordinates_input[7][i] # 8

    # right side
    coordinate9[i]  = generic_coordinates_input[8][i]  # 9
    coordinate10[i] = generic_coordinates_input[9][i]  # 10
    coordinate11[i] = generic_coordinates_input[10][i] # 11
    coordinate12[i] = generic_coordinates_input[11][i] # 12
    coordinate13[i] = generic_coordinates_input[12][i] # 13
    coordinate14[i] = generic_coordinates_input[13][i] # 14
    coordinate15[i] = generic_coordinates_input[14][i] # 15
    coordinate16[i] = generic_coordinates_input[15][i] # 16

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
    # input of ABINIT (left region, cell #6 & #7)
    # right side
    coordinate_R1[i] = generic_coordinates_R_input[0][i] # 1
    coordinate_R2[i] = generic_coordinates_R_input[1][i] # 2
    coordinate_R3[i] = generic_coordinates_R_input[2][i] # 3
    coordinate_R4[i] = generic_coordinates_R_input[3][i] # 4
    coordinate_R5[i] = generic_coordinates_R_input[4][i] # 5
    coordinate_R6[i] = generic_coordinates_R_input[5][i] # 6
    coordinate_R7[i] = generic_coordinates_R_input[6][i] # 7
    coordinate_R8[i] = generic_coordinates_R_input[7][i] # 8

    # right side
    coordinate_R9[i]  = generic_coordinates_R_input[8][i]  # 9
    coordinate_R10[i] = generic_coordinates_R_input[9][i]  # 10
    coordinate_R11[i] = generic_coordinates_R_input[10][i] # 11
    coordinate_R12[i] = generic_coordinates_R_input[11][i] # 12
    coordinate_R13[i] = generic_coordinates_R_input[12][i] # 13
    coordinate_R14[i] = generic_coordinates_R_input[13][i] # 14
    coordinate_R15[i] = generic_coordinates_R_input[14][i] # 15
    coordinate_R16[i] = generic_coordinates_R_input[15][i] # 16

# shift factor by ABINIT (cell #4, #5)
sf1 = shift(coordinate1, ab_coordinate1) # shift factor for atom 1
sf2 = shift(coordinate2, ab_coordinate2) # shift factor for atom 2
sf3 = shift(coordinate3, ab_coordinate3) # shift factor for atom 3
sf4 = shift(coordinate4, ab_coordinate4) # shift factor for atom 4
sf5 = shift(coordinate5, ab_coordinate5) # shift factor for atom 5
sf6 = shift(coordinate6, ab_coordinate6) # shift factor for atom 6
sf7 = shift(coordinate7, ab_coordinate7) # shift factor for atom 7
sf8 = shift(coordinate8, ab_coordinate8) # shift factor for atom 8

sf9 = shift(coordinate9, ab_coordinate9) # shift factor for atom 9
sf10 = shift(coordinate10, ab_coordinate10) # shift factor for atom 10
sf11 = shift(coordinate11, ab_coordinate11) # shift factor for atom 11
sf12 = shift(coordinate12, ab_coordinate12) # shift factor for atom 12
sf13 = shift(coordinate13, ab_coordinate13) # shift factor for atom 13
sf14 = shift(coordinate14, ab_coordinate14) # shift factor for atom 14
sf15 = shift(coordinate15, ab_coordinate15) # shift factor for atom 15
sf16 = shift(coordinate16, ab_coordinate16) # shift factor for atom 16

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

    # skip n=0 & 1
    #if n==0 or n==1:
    #    continue

    if n==-1: # left (cell # 2,3)
        # non-shift coordinates, prepared by excel
        s_coordinate1 = copy.deepcopy(coordinate_L1)
        s_coordinate2 = copy.deepcopy(coordinate_L2)
        s_coordinate3 = copy.deepcopy(coordinate_L3)
        s_coordinate4 = copy.deepcopy(coordinate_L4)
        s_coordinate5 = copy.deepcopy(coordinate_L5)
        s_coordinate6 = copy.deepcopy(coordinate_L6)
        s_coordinate7 = copy.deepcopy(coordinate_L7)
        s_coordinate8 = copy.deepcopy(coordinate_L8)

        s_coordinate9 = copy.deepcopy(coordinate_L9)
        s_coordinate10 = copy.deepcopy(coordinate_L10)
        s_coordinate11 = copy.deepcopy(coordinate_L11)
        s_coordinate12 = copy.deepcopy(coordinate_L12)
        s_coordinate13 = copy.deepcopy(coordinate_L13)
        s_coordinate14 = copy.deepcopy(coordinate_L14)
        s_coordinate15 = copy.deepcopy(coordinate_L15)
        s_coordinate16 = copy.deepcopy(coordinate_L16)

    elif n==0: # center (cell # 4,5)
        # non-shift coordinates, prepared by excel
        s_coordinate1 = copy.deepcopy(coordinate1)
        s_coordinate2 = copy.deepcopy(coordinate2)
        s_coordinate3 = copy.deepcopy(coordinate3)
        s_coordinate4 = copy.deepcopy(coordinate4)
        s_coordinate5 = copy.deepcopy(coordinate5)
        s_coordinate6 = copy.deepcopy(coordinate6)
        s_coordinate7 = copy.deepcopy(coordinate7)
        s_coordinate8 = copy.deepcopy(coordinate8)
        # gap is here
        s_coordinate9 = copy.deepcopy(coordinate9)
        s_coordinate10 = copy.deepcopy(coordinate10)
        s_coordinate11 = copy.deepcopy(coordinate11)
        s_coordinate12 = copy.deepcopy(coordinate12)
        s_coordinate13 = copy.deepcopy(coordinate13)
        s_coordinate14 = copy.deepcopy(coordinate14)
        s_coordinate15 = copy.deepcopy(coordinate15)
        s_coordinate16 = copy.deepcopy(coordinate16)

    elif n==1: # n=1, right (cell # 6,7)
        # non-shift coordinates, prepared by excel
        s_coordinate1 = copy.deepcopy(coordinate_R1)
        s_coordinate2 = copy.deepcopy(coordinate_R2)
        s_coordinate3 = copy.deepcopy(coordinate_R3)
        s_coordinate4 = copy.deepcopy(coordinate_R4)
        s_coordinate5 = copy.deepcopy(coordinate_R5)
        s_coordinate6 = copy.deepcopy(coordinate_R6)
        s_coordinate7 = copy.deepcopy(coordinate_R7)
        s_coordinate8 = copy.deepcopy(coordinate_R8)
        s_coordinate9 = copy.deepcopy(coordinate_R9)

        s_coordinate10 = copy.deepcopy(coordinate_R10)
        s_coordinate11 = copy.deepcopy(coordinate_R11)
        s_coordinate12 = copy.deepcopy(coordinate_R12)
        s_coordinate13 = copy.deepcopy(coordinate_R13)
        s_coordinate14 = copy.deepcopy(coordinate_R14)
        s_coordinate15 = copy.deepcopy(coordinate_R15)
        s_coordinate16 = copy.deepcopy(coordinate_R16)

    for i in range(-1, 2, 1): # xloop (-1 -> 0 -> +1)

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

            # Call GA functions
            # GA1
            GA1(i,j,n, adjustment(s_coordinate1+sf1), adjustment(s_coordinate2+sf1)\
            ,adjustment(s_coordinate3+sf1), adjustment(s_coordinate4+sf1), adjustment(s_coordinate5+sf1)\
            ,adjustment(s_coordinate6+sf1), adjustment(s_coordinate7+sf1), adjustment(s_coordinate8+sf1)\
            ,adjustment(s_coordinate9+sf1), adjustment(s_coordinate10+sf1), adjustment(s_coordinate11+sf1)\
            ,adjustment(s_coordinate12+sf1), adjustment(s_coordinate13+sf1), adjustment(s_coordinate14+sf1)\
            ,adjustment(s_coordinate15+sf1), adjustment(s_coordinate16+sf1))

            # GA2
            GA2(i,j,n, adjustment(s_coordinate1+sf2), adjustment(s_coordinate2+sf2)\
            ,adjustment(s_coordinate3+sf2), adjustment(s_coordinate4+sf2), adjustment(s_coordinate5+sf2)\
            ,adjustment(s_coordinate6+sf2), adjustment(s_coordinate7+sf2), adjustment(s_coordinate8+sf2)\
            ,adjustment(s_coordinate9+sf2), adjustment(s_coordinate10+sf2), adjustment(s_coordinate11+sf2)\
            ,adjustment(s_coordinate12+sf2), adjustment(s_coordinate13+sf2), adjustment(s_coordinate14+sf2)\
            ,adjustment(s_coordinate15+sf2), adjustment(s_coordinate16+sf2))

            # GA3
            GA3(i,j,n, adjustment(s_coordinate1+sf3), adjustment(s_coordinate2+sf3)\
            ,adjustment(s_coordinate3+sf3), adjustment(s_coordinate4+sf3), adjustment(s_coordinate5+sf3)\
            ,adjustment(s_coordinate6+sf3), adjustment(s_coordinate7+sf3), adjustment(s_coordinate8+sf3)\
            ,adjustment(s_coordinate9+sf3), adjustment(s_coordinate10+sf3), adjustment(s_coordinate11+sf3)\
            ,adjustment(s_coordinate12+sf3), adjustment(s_coordinate13+sf3), adjustment(s_coordinate14+sf3)\
            ,adjustment(s_coordinate15+sf3), adjustment(s_coordinate16+sf3))

            # GA4
            GA4(i,j,n, adjustment(s_coordinate1+sf4), adjustment(s_coordinate2+sf4)\
            ,adjustment(s_coordinate3+sf4), adjustment(s_coordinate4+sf4), adjustment(s_coordinate5+sf4)\
            ,adjustment(s_coordinate6+sf4), adjustment(s_coordinate7+sf4), adjustment(s_coordinate8+sf4)\
            ,adjustment(s_coordinate9+sf4), adjustment(s_coordinate10+sf4), adjustment(s_coordinate11+sf4)\
            ,adjustment(s_coordinate12+sf4), adjustment(s_coordinate13+sf4), adjustment(s_coordinate14+sf4)\
            ,adjustment(s_coordinate15+sf4), adjustment(s_coordinate16+sf4))

            # GA5
            GA5(i,j,n, adjustment(s_coordinate1+sf5), adjustment(s_coordinate2+sf5)\
            ,adjustment(s_coordinate3+sf5), adjustment(s_coordinate4+sf5), adjustment(s_coordinate5+sf5)\
            ,adjustment(s_coordinate6+sf5), adjustment(s_coordinate7+sf5), adjustment(s_coordinate8+sf5)\
            ,adjustment(s_coordinate9+sf5), adjustment(s_coordinate10+sf5), adjustment(s_coordinate11+sf5)\
            ,adjustment(s_coordinate12+sf5), adjustment(s_coordinate13+sf5), adjustment(s_coordinate14+sf5)\
            ,adjustment(s_coordinate15+sf5), adjustment(s_coordinate16+sf5))

            # GA6
            GA6(i,j,n, adjustment(s_coordinate1+sf6), adjustment(s_coordinate2+sf6)\
            ,adjustment(s_coordinate3+sf6), adjustment(s_coordinate4+sf6), adjustment(s_coordinate5+sf6)\
            ,adjustment(s_coordinate6+sf6), adjustment(s_coordinate7+sf6), adjustment(s_coordinate8+sf6)\
            ,adjustment(s_coordinate9+sf6), adjustment(s_coordinate10+sf6), adjustment(s_coordinate11+sf6)\
            ,adjustment(s_coordinate12+sf6), adjustment(s_coordinate13+sf6), adjustment(s_coordinate14+sf6)\
            ,adjustment(s_coordinate15+sf6), adjustment(s_coordinate16+sf6))

            # GA7
            GA7(i,j,n, adjustment(s_coordinate1+sf7), adjustment(s_coordinate2+sf7)\
            ,adjustment(s_coordinate3+sf7), adjustment(s_coordinate4+sf7), adjustment(s_coordinate5+sf7)\
            ,adjustment(s_coordinate6+sf7), adjustment(s_coordinate7+sf7), adjustment(s_coordinate8+sf7)\
            ,adjustment(s_coordinate9+sf7), adjustment(s_coordinate10+sf7), adjustment(s_coordinate11+sf7)\
            ,adjustment(s_coordinate12+sf7), adjustment(s_coordinate13+sf7), adjustment(s_coordinate14+sf7)\
            ,adjustment(s_coordinate15+sf7), adjustment(s_coordinate16+sf7))

            # GA8
            GA8(i,j,n, adjustment(s_coordinate1+sf8), adjustment(s_coordinate2+sf8)\
            ,adjustment(s_coordinate3+sf8), adjustment(s_coordinate4+sf8), adjustment(s_coordinate5+sf8)\
            ,adjustment(s_coordinate6+sf8), adjustment(s_coordinate7+sf8), adjustment(s_coordinate8+sf8)\
            ,adjustment(s_coordinate9+sf8), adjustment(s_coordinate10+sf8), adjustment(s_coordinate11+sf8)\
            ,adjustment(s_coordinate12+sf8), adjustment(s_coordinate13+sf8), adjustment(s_coordinate14+sf8)\
            ,adjustment(s_coordinate15+sf8), adjustment(s_coordinate16+sf8))

            # GA9
            GA9(i,j,n, adjustment(s_coordinate1+sf9), adjustment(s_coordinate2+sf9)\
            ,adjustment(s_coordinate3+sf9), adjustment(s_coordinate4+sf9), adjustment(s_coordinate5+sf9)\
            ,adjustment(s_coordinate6+sf9), adjustment(s_coordinate7+sf9), adjustment(s_coordinate8+sf9)\
            ,adjustment(s_coordinate9+sf9), adjustment(s_coordinate10+sf9), adjustment(s_coordinate11+sf9)\
            ,adjustment(s_coordinate12+sf9), adjustment(s_coordinate13+sf9), adjustment(s_coordinate14+sf9)\
            ,adjustment(s_coordinate15+sf9), adjustment(s_coordinate16+sf9))

            # GA10
            GA10(i,j,n, adjustment(s_coordinate1+sf10), adjustment(s_coordinate2+sf10)\
            ,adjustment(s_coordinate3+sf10), adjustment(s_coordinate4+sf10), adjustment(s_coordinate5+sf10)\
            ,adjustment(s_coordinate6+sf10), adjustment(s_coordinate7+sf10), adjustment(s_coordinate8+sf10)\
            ,adjustment(s_coordinate9+sf10), adjustment(s_coordinate10+sf10), adjustment(s_coordinate11+sf10)\
            ,adjustment(s_coordinate12+sf10), adjustment(s_coordinate13+sf10), adjustment(s_coordinate14+sf10)\
            ,adjustment(s_coordinate15+sf10), adjustment(s_coordinate16+sf10))

            # GA11
            GA11(i,j,n, adjustment(s_coordinate1+sf11), adjustment(s_coordinate2+sf11)\
            ,adjustment(s_coordinate3+sf11), adjustment(s_coordinate4+sf11), adjustment(s_coordinate5+sf11)\
            ,adjustment(s_coordinate6+sf11), adjustment(s_coordinate7+sf11), adjustment(s_coordinate8+sf11)\
            ,adjustment(s_coordinate9+sf11), adjustment(s_coordinate10+sf11), adjustment(s_coordinate11+sf11)\
            ,adjustment(s_coordinate12+sf11), adjustment(s_coordinate13+sf11), adjustment(s_coordinate14+sf11)\
            ,adjustment(s_coordinate15+sf11), adjustment(s_coordinate16+sf11))

            # GA12
            GA12(i,j,n, adjustment(s_coordinate1+sf12), adjustment(s_coordinate2+sf12)\
            ,adjustment(s_coordinate3+sf12), adjustment(s_coordinate4+sf12), adjustment(s_coordinate5+sf12)\
            ,adjustment(s_coordinate6+sf12), adjustment(s_coordinate7+sf12), adjustment(s_coordinate8+sf12)\
            ,adjustment(s_coordinate9+sf12), adjustment(s_coordinate10+sf12), adjustment(s_coordinate11+sf12)\
            ,adjustment(s_coordinate12+sf12), adjustment(s_coordinate13+sf12), adjustment(s_coordinate14+sf12)\
            ,adjustment(s_coordinate15+sf12), adjustment(s_coordinate16+sf12))

            # GA13
            GA13(i,j,n, adjustment(s_coordinate1+sf13), adjustment(s_coordinate2+sf13)\
            ,adjustment(s_coordinate3+sf13), adjustment(s_coordinate4+sf13), adjustment(s_coordinate5+sf13)\
            ,adjustment(s_coordinate6+sf13), adjustment(s_coordinate7+sf13), adjustment(s_coordinate8+sf13)\
            ,adjustment(s_coordinate9+sf13), adjustment(s_coordinate10+sf13), adjustment(s_coordinate11+sf13)\
            ,adjustment(s_coordinate12+sf13), adjustment(s_coordinate13+sf13), adjustment(s_coordinate14+sf13)\
            ,adjustment(s_coordinate15+sf13), adjustment(s_coordinate16+sf13))

            # GA14
            GA14(i,j,n, adjustment(s_coordinate1+sf14), adjustment(s_coordinate2+sf14)\
            ,adjustment(s_coordinate3+sf14), adjustment(s_coordinate4+sf14), adjustment(s_coordinate5+sf14)\
            ,adjustment(s_coordinate6+sf14), adjustment(s_coordinate7+sf14), adjustment(s_coordinate8+sf14)\
            ,adjustment(s_coordinate9+sf14), adjustment(s_coordinate10+sf14), adjustment(s_coordinate11+sf14)\
            ,adjustment(s_coordinate12+sf14), adjustment(s_coordinate13+sf14), adjustment(s_coordinate14+sf14)\
            ,adjustment(s_coordinate15+sf14), adjustment(s_coordinate16+sf14))

            # GA15
            GA15(i,j,n, adjustment(s_coordinate1+sf15), adjustment(s_coordinate2+sf15)\
            ,adjustment(s_coordinate3+sf15), adjustment(s_coordinate4+sf15), adjustment(s_coordinate5+sf15)\
            ,adjustment(s_coordinate6+sf15), adjustment(s_coordinate7+sf15), adjustment(s_coordinate8+sf15)\
            ,adjustment(s_coordinate9+sf15), adjustment(s_coordinate10+sf15), adjustment(s_coordinate11+sf15)\
            ,adjustment(s_coordinate12+sf15), adjustment(s_coordinate13+sf15), adjustment(s_coordinate14+sf15)\
            ,adjustment(s_coordinate15+sf15), adjustment(s_coordinate16+sf15))

            # GA16
            GA16(i,j,n, adjustment(s_coordinate1+sf16), adjustment(s_coordinate2+sf16)\
            ,adjustment(s_coordinate3+sf16), adjustment(s_coordinate4+sf16), adjustment(s_coordinate5+sf16)\
            ,adjustment(s_coordinate6+sf16), adjustment(s_coordinate7+sf16), adjustment(s_coordinate8+sf16)\
            ,adjustment(s_coordinate9+sf16), adjustment(s_coordinate10+sf16), adjustment(s_coordinate11+sf16)\
            ,adjustment(s_coordinate12+sf16), adjustment(s_coordinate13+sf16), adjustment(s_coordinate14+sf16)\
            ,adjustment(s_coordinate15+sf16), adjustment(s_coordinate16+sf16))

            # initialize to primitive cell coordinate, y direction
            for k in range(0, dof): # yloop
                if k==1:
                    if n==-1:
                        s_coordinate1[k] = copy.deepcopy(coordinate_L1[k])
                        s_coordinate2[k] = copy.deepcopy(coordinate_L2[k])
                        s_coordinate3[k] = copy.deepcopy(coordinate_L3[k])
                        s_coordinate4[k] = copy.deepcopy(coordinate_L4[k])
                        s_coordinate5[k] = copy.deepcopy(coordinate_L5[k])
                        s_coordinate6[k] = copy.deepcopy(coordinate_L6[k])
                        s_coordinate7[k] = copy.deepcopy(coordinate_L7[k])
                        s_coordinate8[k] = copy.deepcopy(coordinate_L8[k])

                        s_coordinate9[k] = copy.deepcopy(coordinate_L9[k])
                        s_coordinate10[k] = copy.deepcopy(coordinate_L10[k])
                        s_coordinate11[k] = copy.deepcopy(coordinate_L11[k])
                        s_coordinate12[k] = copy.deepcopy(coordinate_L12[k])
                        s_coordinate13[k] = copy.deepcopy(coordinate_L13[k])
                        s_coordinate14[k] = copy.deepcopy(coordinate_L14[k])
                        s_coordinate15[k] = copy.deepcopy(coordinate_L15[k])
                        s_coordinate16[k] = copy.deepcopy(coordinate_L16[k])

                    elif n==0: # center (cell # 4,5)
                        s_coordinate1[k] = copy.deepcopy(coordinate1[k])
                        s_coordinate2[k] = copy.deepcopy(coordinate2[k])
                        s_coordinate3[k] = copy.deepcopy(coordinate3[k])
                        s_coordinate4[k] = copy.deepcopy(coordinate4[k])
                        s_coordinate5[k] = copy.deepcopy(coordinate5[k])
                        s_coordinate6[k] = copy.deepcopy(coordinate6[k])
                        s_coordinate7[k] = copy.deepcopy(coordinate7[k])
                        s_coordinate8[k] = copy.deepcopy(coordinate8[k])
                        # gap is here
                        s_coordinate9[k] = copy.deepcopy(coordinate9[k])
                        s_coordinate10[k] = copy.deepcopy(coordinate10[k])
                        s_coordinate11[k] = copy.deepcopy(coordinate11[k])
                        s_coordinate12[k] = copy.deepcopy(coordinate12[k])
                        s_coordinate13[k] = copy.deepcopy(coordinate13[k])
                        s_coordinate14[k] = copy.deepcopy(coordinate14[k])
                        s_coordinate15[k] = copy.deepcopy(coordinate15[k])
                        s_coordinate16[k] = copy.deepcopy(coordinate16[k])

                    elif n==1: # n=1, right (cell # 6,7)
                        s_coordinate1[k] = copy.deepcopy(coordinate_R1[k])
                        s_coordinate2[k] = copy.deepcopy(coordinate_R2[k])
                        s_coordinate3[k] = copy.deepcopy(coordinate_R3[k])
                        s_coordinate4[k] = copy.deepcopy(coordinate_R4[k])
                        s_coordinate5[k] = copy.deepcopy(coordinate_R5[k])
                        s_coordinate6[k] = copy.deepcopy(coordinate_R6[k])
                        s_coordinate7[k] = copy.deepcopy(coordinate_R7[k])
                        s_coordinate8[k] = copy.deepcopy(coordinate_R8[k])
                        s_coordinate9[k] = copy.deepcopy(coordinate_R9[k])

                        s_coordinate10[k] = copy.deepcopy(coordinate_R10[k])
                        s_coordinate11[k] = copy.deepcopy(coordinate_R11[k])
                        s_coordinate12[k] = copy.deepcopy(coordinate_R12[k])
                        s_coordinate13[k] = copy.deepcopy(coordinate_R13[k])
                        s_coordinate14[k] = copy.deepcopy(coordinate_R14[k])
                        s_coordinate15[k] = copy.deepcopy(coordinate_R15[k])
                        s_coordinate16[k] = copy.deepcopy(coordinate_R16[k])

        # initialize to primitive cell coordinate, x & y direction
        for l in range(0, dof): # x & y loop
            if l==0 or l==1:
                if n==-1:
                    s_coordinate1[l] = copy.deepcopy(coordinate_L1[l])
                    s_coordinate2[l] = copy.deepcopy(coordinate_L2[l])
                    s_coordinate3[l] = copy.deepcopy(coordinate_L3[l])
                    s_coordinate4[l] = copy.deepcopy(coordinate_L4[l])
                    s_coordinate5[l] = copy.deepcopy(coordinate_L5[l])
                    s_coordinate6[l] = copy.deepcopy(coordinate_L6[l])
                    s_coordinate7[l] = copy.deepcopy(coordinate_L7[l])
                    s_coordinate8[l] = copy.deepcopy(coordinate_L8[l])

                    s_coordinate9[l] = copy.deepcopy(coordinate_L9[l])
                    s_coordinate10[l] = copy.deepcopy(coordinate_L10[l])
                    s_coordinate11[l] = copy.deepcopy(coordinate_L11[l])
                    s_coordinate12[l] = copy.deepcopy(coordinate_L12[l])
                    s_coordinate13[l] = copy.deepcopy(coordinate_L13[l])
                    s_coordinate14[l] = copy.deepcopy(coordinate_L14[l])
                    s_coordinate15[l] = copy.deepcopy(coordinate_L15[l])
                    s_coordinate16[l] = copy.deepcopy(coordinate_L16[l])

                elif n==0: # center (cell # 4,5)
                    s_coordinate1[l] = copy.deepcopy(coordinate1[l])
                    s_coordinate2[l] = copy.deepcopy(coordinate2[l])
                    s_coordinate3[l] = copy.deepcopy(coordinate3[l])
                    s_coordinate4[l] = copy.deepcopy(coordinate4[l])
                    s_coordinate5[l] = copy.deepcopy(coordinate5[l])
                    s_coordinate6[l] = copy.deepcopy(coordinate6[l])
                    s_coordinate7[l] = copy.deepcopy(coordinate7[l])
                    s_coordinate8[l] = copy.deepcopy(coordinate8[l])
                    # gap is here
                    s_coordinate9[l] = copy.deepcopy(coordinate9[l])
                    s_coordinate10[l] = copy.deepcopy(coordinate10[l])
                    s_coordinate11[l] = copy.deepcopy(coordinate11[l])
                    s_coordinate12[l] = copy.deepcopy(coordinate12[l])
                    s_coordinate13[l] = copy.deepcopy(coordinate13[l])
                    s_coordinate14[l] = copy.deepcopy(coordinate14[l])
                    s_coordinate15[l] = copy.deepcopy(coordinate15[l])
                    s_coordinate16[l] = copy.deepcopy(coordinate16[l])

                elif n==1: # n=1, right (cell # 6,7)
                    s_coordinate1[l] = copy.deepcopy(coordinate_R1[l])
                    s_coordinate2[l] = copy.deepcopy(coordinate_R2[l])
                    s_coordinate3[l] = copy.deepcopy(coordinate_R3[l])
                    s_coordinate4[l] = copy.deepcopy(coordinate_R4[l])
                    s_coordinate5[l] = copy.deepcopy(coordinate_R5[l])
                    s_coordinate6[l] = copy.deepcopy(coordinate_R6[l])
                    s_coordinate7[l] = copy.deepcopy(coordinate_R7[l])
                    s_coordinate8[l] = copy.deepcopy(coordinate_R8[l])
                    s_coordinate9[l] = copy.deepcopy(coordinate_R9[l])

                    s_coordinate10[l] = copy.deepcopy(coordinate_R10[l])
                    s_coordinate11[l] = copy.deepcopy(coordinate_R11[l])
                    s_coordinate12[l] = copy.deepcopy(coordinate_R12[l])
                    s_coordinate13[l] = copy.deepcopy(coordinate_R13[l])
                    s_coordinate14[l] = copy.deepcopy(coordinate_R14[l])
                    s_coordinate15[l] = copy.deepcopy(coordinate_R15[l])
                    s_coordinate16[l] = copy.deepcopy(coordinate_R16[l])

    # initialize to primitive cell coordinate, x y z direction
    #for m in range(0, dof): # x, y & z loop

    # no need for z loop since initialization
    # since s_coordinate# is reset at the beginning

# end
end()

# time display
elapsed_time = time.time()-start
print("elapsed_time:{:.2f}".format(elapsed_time) + "[sec]")
