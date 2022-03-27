# Coded by Takuro TOKUNAGA
# Force constant matrices only for central region
# Last modified: September 03, 2020

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

# parameters
dof = 3                      # [-], dgree of freedom
cell_num = 2                 # [-], number of cell
si_atoms_conventional = 8    # [-], number of Si atoms in conventional unit cell, fixed
si_atoms_toal = cell_num*si_atoms_conventional # number of total Si atoms in the suprecell

# unit conversion
ucangs = 1.0*np.power(10.,-10) # [m]
ucbohr = 0.529177249*ucangs    # [m]

# lattice constant of Si
lcsi = 5.470*ucangs           # [m], don't change
lcsi_bohr = lcsi/ucbohr      # [bohr] 4/4

# read generic coordinates from ABINIT input
generic_coordinates_input=[list(map(np.float64,line.rstrip().split(" "))) for line in open("ABINIT_generic_atoms_coordinates_input.txt").readlines()]
# read generic coordinates from ABINIT output
generic_coordinates_output=[list(map(np.float64,line.rstrip().split(" "))) for line in open("ABINIT_generic_atoms_coordinates_output.txt").readlines()]

# primitive cell atom's coordinates
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

# primitive cell atom's coordinates by ABNINIT output
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
for i in range(0, dof):
    # input of ABINIT
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
    # left side
    ab_coordinate1[i] = generic_coordinates_output[0][i] # 1
    ab_coordinate2[i] = generic_coordinates_output[1][i] # 2
    ab_coordinate3[i] = generic_coordinates_output[2][i] # 3
    ab_coordinate4[i] = generic_coordinates_output[3][i] # 4
    ab_coordinate5[i] = generic_coordinates_output[4][i] # 5
    ab_coordinate6[i] = generic_coordinates_output[5][i] # 6
    ab_coordinate7[i] = generic_coordinates_output[6][i] # 7
    ab_coordinate8[i] = generic_coordinates_output[7][i] # 8

    # right side
    ab_coordinate9[i]  = generic_coordinates_output[8][i]  # 9
    ab_coordinate10[i] = generic_coordinates_output[9][i]  # 10
    ab_coordinate11[i] = generic_coordinates_output[10][i] # 11
    ab_coordinate12[i] = generic_coordinates_output[11][i] # 12
    ab_coordinate13[i] = generic_coordinates_output[12][i] # 13
    ab_coordinate14[i] = generic_coordinates_output[13][i] # 14
    ab_coordinate15[i] = generic_coordinates_output[14][i] # 15
    ab_coordinate16[i] = generic_coordinates_output[15][i] # 16

# shift factor by ABINIT
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

# shifting procedures start
# This code does not have shifting procedures
# shifting procedures end

# no zloop, instead z fixing procedures:
# z coordinates are always fixed
s_coordinate1[2] = coordinate1[2]
s_coordinate2[2] = coordinate2[2]
s_coordinate3[2] = coordinate3[2]
s_coordinate4[2] = coordinate4[2]
s_coordinate5[2] = coordinate5[2]
s_coordinate6[2] = coordinate6[2]
s_coordinate7[2] = coordinate7[2]
s_coordinate8[2] = coordinate8[2]
s_coordinate9[2] = coordinate9[2]
s_coordinate10[2] = coordinate10[2]
s_coordinate11[2] = coordinate11[2]
s_coordinate12[2] = coordinate12[2]
s_coordinate13[2] = coordinate13[2]
s_coordinate14[2] = coordinate14[2]
s_coordinate15[2] = coordinate15[2]
s_coordinate16[2] = coordinate16[2]

# no zloop, only device region
# extraction start
for i in range(-1, 2, 1): # xloop (-1 -> 0 -> +1)
    # x direction
    s_coordinate1[0] = coordinate1[0] + i*lcsi_bohr
    s_coordinate2[0] = coordinate2[0] + i*lcsi_bohr
    s_coordinate3[0] = coordinate3[0] + i*lcsi_bohr
    s_coordinate4[0] = coordinate4[0] + i*lcsi_bohr
    s_coordinate5[0] = coordinate5[0] + i*lcsi_bohr
    s_coordinate6[0] = coordinate6[0] + i*lcsi_bohr
    s_coordinate7[0] = coordinate7[0] + i*lcsi_bohr
    s_coordinate8[0] = coordinate8[0] + i*lcsi_bohr
    s_coordinate9[0] = coordinate9[0] + i*lcsi_bohr
    s_coordinate10[0] = coordinate10[0] + i*lcsi_bohr
    s_coordinate11[0] = coordinate11[0] + i*lcsi_bohr
    s_coordinate12[0] = coordinate12[0] + i*lcsi_bohr
    s_coordinate13[0] = coordinate13[0] + i*lcsi_bohr
    s_coordinate14[0] = coordinate14[0] + i*lcsi_bohr
    s_coordinate15[0] = coordinate15[0] + i*lcsi_bohr
    s_coordinate16[0] = coordinate16[0] + i*lcsi_bohr

    for j in range(-1, 2, 1): # yloop (-1 -> 0 -> +1)
        # y direction
        s_coordinate1[1] = coordinate1[1] + j*lcsi_bohr
        s_coordinate2[1] = coordinate2[1] + j*lcsi_bohr
        s_coordinate3[1] = coordinate3[1] + j*lcsi_bohr
        s_coordinate4[1] = coordinate4[1] + j*lcsi_bohr
        s_coordinate5[1] = coordinate5[1] + j*lcsi_bohr
        s_coordinate6[1] = coordinate6[1] + j*lcsi_bohr
        s_coordinate7[1] = coordinate7[1] + j*lcsi_bohr
        s_coordinate8[1] = coordinate8[1] + j*lcsi_bohr
        s_coordinate9[1] = coordinate9[1] + j*lcsi_bohr
        s_coordinate10[1] = coordinate10[1] + j*lcsi_bohr
        s_coordinate11[1] = coordinate11[1] + j*lcsi_bohr
        s_coordinate12[1] = coordinate12[1] + j*lcsi_bohr
        s_coordinate13[1] = coordinate13[1] + j*lcsi_bohr
        s_coordinate14[1] = coordinate14[1] + j*lcsi_bohr
        s_coordinate15[1] = coordinate15[1] + j*lcsi_bohr
        s_coordinate16[1] = coordinate16[1] + j*lcsi_bohr

        # Call GA functions
        # GA1
        GA1(i,j,0, adjustment(s_coordinate1+sf1), adjustment(s_coordinate2+sf1)\
        ,adjustment(s_coordinate3+sf1), adjustment(s_coordinate4+sf1), adjustment(s_coordinate5+sf1)\
        ,adjustment(s_coordinate6+sf1), adjustment(s_coordinate7+sf1), adjustment(s_coordinate8+sf1)\
        ,adjustment(s_coordinate9+sf1), adjustment(s_coordinate10+sf1), adjustment(s_coordinate11+sf1)\
        ,adjustment(s_coordinate12+sf1), adjustment(s_coordinate13+sf1), adjustment(s_coordinate14+sf1)\
        ,adjustment(s_coordinate15+sf1), adjustment(s_coordinate16+sf1))

        # GA2
        GA2(i,j,0, adjustment(s_coordinate1+sf2), adjustment(s_coordinate2+sf2)\
        ,adjustment(s_coordinate3+sf2), adjustment(s_coordinate4+sf2), adjustment(s_coordinate5+sf2)\
        ,adjustment(s_coordinate6+sf2), adjustment(s_coordinate7+sf2), adjustment(s_coordinate8+sf2)\
        ,adjustment(s_coordinate9+sf2), adjustment(s_coordinate10+sf2), adjustment(s_coordinate11+sf2)\
        ,adjustment(s_coordinate12+sf2), adjustment(s_coordinate13+sf2), adjustment(s_coordinate14+sf2)\
        ,adjustment(s_coordinate15+sf2), adjustment(s_coordinate16+sf2))

        # GA3
        GA3(i,j,0, adjustment(s_coordinate1+sf3), adjustment(s_coordinate2+sf3)\
        ,adjustment(s_coordinate3+sf3), adjustment(s_coordinate4+sf3), adjustment(s_coordinate5+sf3)\
        ,adjustment(s_coordinate6+sf3), adjustment(s_coordinate7+sf3), adjustment(s_coordinate8+sf3)\
        ,adjustment(s_coordinate9+sf3), adjustment(s_coordinate10+sf3), adjustment(s_coordinate11+sf3)\
        ,adjustment(s_coordinate12+sf3), adjustment(s_coordinate13+sf3), adjustment(s_coordinate14+sf3)\
        ,adjustment(s_coordinate15+sf3), adjustment(s_coordinate16+sf3))

        # GA4
        GA4(i,j,0, adjustment(s_coordinate1+sf4), adjustment(s_coordinate2+sf4)\
        ,adjustment(s_coordinate3+sf4), adjustment(s_coordinate4+sf4), adjustment(s_coordinate5+sf4)\
        ,adjustment(s_coordinate6+sf4), adjustment(s_coordinate7+sf4), adjustment(s_coordinate8+sf4)\
        ,adjustment(s_coordinate9+sf4), adjustment(s_coordinate10+sf4), adjustment(s_coordinate11+sf4)\
        ,adjustment(s_coordinate12+sf4), adjustment(s_coordinate13+sf4), adjustment(s_coordinate14+sf4)\
        ,adjustment(s_coordinate15+sf4), adjustment(s_coordinate16+sf4))

        # GA5
        GA5(i,j,0, adjustment(s_coordinate1+sf5), adjustment(s_coordinate2+sf5)\
        ,adjustment(s_coordinate3+sf5), adjustment(s_coordinate4+sf5), adjustment(s_coordinate5+sf5)\
        ,adjustment(s_coordinate6+sf5), adjustment(s_coordinate7+sf5), adjustment(s_coordinate8+sf5)\
        ,adjustment(s_coordinate9+sf5), adjustment(s_coordinate10+sf5), adjustment(s_coordinate11+sf5)\
        ,adjustment(s_coordinate12+sf5), adjustment(s_coordinate13+sf5), adjustment(s_coordinate14+sf5)\
        ,adjustment(s_coordinate15+sf5), adjustment(s_coordinate16+sf5))

        # GA6
        GA6(i,j,0, adjustment(s_coordinate1+sf6), adjustment(s_coordinate2+sf6)\
        ,adjustment(s_coordinate3+sf6), adjustment(s_coordinate4+sf6), adjustment(s_coordinate5+sf6)\
        ,adjustment(s_coordinate6+sf6), adjustment(s_coordinate7+sf6), adjustment(s_coordinate8+sf6)\
        ,adjustment(s_coordinate9+sf6), adjustment(s_coordinate10+sf6), adjustment(s_coordinate11+sf6)\
        ,adjustment(s_coordinate12+sf6), adjustment(s_coordinate13+sf6), adjustment(s_coordinate14+sf6)\
        ,adjustment(s_coordinate15+sf6), adjustment(s_coordinate16+sf6))

        # GA7
        GA7(i,j,0, adjustment(s_coordinate1+sf7), adjustment(s_coordinate2+sf7)\
        ,adjustment(s_coordinate3+sf7), adjustment(s_coordinate4+sf7), adjustment(s_coordinate5+sf7)\
        ,adjustment(s_coordinate6+sf7), adjustment(s_coordinate7+sf7), adjustment(s_coordinate8+sf7)\
        ,adjustment(s_coordinate9+sf7), adjustment(s_coordinate10+sf7), adjustment(s_coordinate11+sf7)\
        ,adjustment(s_coordinate12+sf7), adjustment(s_coordinate13+sf7), adjustment(s_coordinate14+sf7)\
        ,adjustment(s_coordinate15+sf7), adjustment(s_coordinate16+sf7))

        # GA8
        GA8(i,j,0, adjustment(s_coordinate1+sf8), adjustment(s_coordinate2+sf8)\
        ,adjustment(s_coordinate3+sf8), adjustment(s_coordinate4+sf8), adjustment(s_coordinate5+sf8)\
        ,adjustment(s_coordinate6+sf8), adjustment(s_coordinate7+sf8), adjustment(s_coordinate8+sf8)\
        ,adjustment(s_coordinate9+sf8), adjustment(s_coordinate10+sf8), adjustment(s_coordinate11+sf8)\
        ,adjustment(s_coordinate12+sf8), adjustment(s_coordinate13+sf8), adjustment(s_coordinate14+sf8)\
        ,adjustment(s_coordinate15+sf8), adjustment(s_coordinate16+sf8))

        # GA9
        GA9(i,j,0, adjustment(s_coordinate1+sf9), adjustment(s_coordinate2+sf9)\
        ,adjustment(s_coordinate3+sf9), adjustment(s_coordinate4+sf9), adjustment(s_coordinate5+sf9)\
        ,adjustment(s_coordinate6+sf9), adjustment(s_coordinate7+sf9), adjustment(s_coordinate8+sf9)\
        ,adjustment(s_coordinate9+sf9), adjustment(s_coordinate10+sf9), adjustment(s_coordinate11+sf9)\
        ,adjustment(s_coordinate12+sf9), adjustment(s_coordinate13+sf9), adjustment(s_coordinate14+sf9)\
        ,adjustment(s_coordinate15+sf9), adjustment(s_coordinate16+sf9))

        # GA10
        GA10(i,j,0, adjustment(s_coordinate1+sf10), adjustment(s_coordinate2+sf10)\
        ,adjustment(s_coordinate3+sf10), adjustment(s_coordinate4+sf10), adjustment(s_coordinate5+sf10)\
        ,adjustment(s_coordinate6+sf10), adjustment(s_coordinate7+sf10), adjustment(s_coordinate8+sf10)\
        ,adjustment(s_coordinate9+sf10), adjustment(s_coordinate10+sf10), adjustment(s_coordinate11+sf10)\
        ,adjustment(s_coordinate12+sf10), adjustment(s_coordinate13+sf10), adjustment(s_coordinate14+sf10)\
        ,adjustment(s_coordinate15+sf10), adjustment(s_coordinate16+sf10))

        # GA11
        GA11(i,j,0, adjustment(s_coordinate1+sf11), adjustment(s_coordinate2+sf11)\
        ,adjustment(s_coordinate3+sf11), adjustment(s_coordinate4+sf11), adjustment(s_coordinate5+sf11)\
        ,adjustment(s_coordinate6+sf11), adjustment(s_coordinate7+sf11), adjustment(s_coordinate8+sf11)\
        ,adjustment(s_coordinate9+sf11), adjustment(s_coordinate10+sf11), adjustment(s_coordinate11+sf11)\
        ,adjustment(s_coordinate12+sf11), adjustment(s_coordinate13+sf11), adjustment(s_coordinate14+sf11)\
        ,adjustment(s_coordinate15+sf11), adjustment(s_coordinate16+sf11))

        # GA12
        GA12(i,j,0, adjustment(s_coordinate1+sf12), adjustment(s_coordinate2+sf12)\
        ,adjustment(s_coordinate3+sf12), adjustment(s_coordinate4+sf12), adjustment(s_coordinate5+sf12)\
        ,adjustment(s_coordinate6+sf12), adjustment(s_coordinate7+sf12), adjustment(s_coordinate8+sf12)\
        ,adjustment(s_coordinate9+sf12), adjustment(s_coordinate10+sf12), adjustment(s_coordinate11+sf12)\
        ,adjustment(s_coordinate12+sf12), adjustment(s_coordinate13+sf12), adjustment(s_coordinate14+sf12)\
        ,adjustment(s_coordinate15+sf12), adjustment(s_coordinate16+sf12))

        # GA13
        GA13(i,j,0, adjustment(s_coordinate1+sf13), adjustment(s_coordinate2+sf13)\
        ,adjustment(s_coordinate3+sf13), adjustment(s_coordinate4+sf13), adjustment(s_coordinate5+sf13)\
        ,adjustment(s_coordinate6+sf13), adjustment(s_coordinate7+sf13), adjustment(s_coordinate8+sf13)\
        ,adjustment(s_coordinate9+sf13), adjustment(s_coordinate10+sf13), adjustment(s_coordinate11+sf13)\
        ,adjustment(s_coordinate12+sf13), adjustment(s_coordinate13+sf13), adjustment(s_coordinate14+sf13)\
        ,adjustment(s_coordinate15+sf13), adjustment(s_coordinate16+sf13))

        # GA14
        GA14(i,j,0, adjustment(s_coordinate1+sf14), adjustment(s_coordinate2+sf14)\
        ,adjustment(s_coordinate3+sf14), adjustment(s_coordinate4+sf14), adjustment(s_coordinate5+sf14)\
        ,adjustment(s_coordinate6+sf14), adjustment(s_coordinate7+sf14), adjustment(s_coordinate8+sf14)\
        ,adjustment(s_coordinate9+sf14), adjustment(s_coordinate10+sf14), adjustment(s_coordinate11+sf14)\
        ,adjustment(s_coordinate12+sf14), adjustment(s_coordinate13+sf14), adjustment(s_coordinate14+sf14)\
        ,adjustment(s_coordinate15+sf14), adjustment(s_coordinate16+sf14))

        # GA15
        GA15(i,j,0, adjustment(s_coordinate1+sf15), adjustment(s_coordinate2+sf15)\
        ,adjustment(s_coordinate3+sf15), adjustment(s_coordinate4+sf15), adjustment(s_coordinate5+sf15)\
        ,adjustment(s_coordinate6+sf15), adjustment(s_coordinate7+sf15), adjustment(s_coordinate8+sf15)\
        ,adjustment(s_coordinate9+sf15), adjustment(s_coordinate10+sf15), adjustment(s_coordinate11+sf15)\
        ,adjustment(s_coordinate12+sf15), adjustment(s_coordinate13+sf15), adjustment(s_coordinate14+sf15)\
        ,adjustment(s_coordinate15+sf15), adjustment(s_coordinate16+sf15))

        # GA16
        GA16(i,j,0, adjustment(s_coordinate1+sf16), adjustment(s_coordinate2+sf16)\
        ,adjustment(s_coordinate3+sf16), adjustment(s_coordinate4+sf16), adjustment(s_coordinate5+sf16)\
        ,adjustment(s_coordinate6+sf16), adjustment(s_coordinate7+sf16), adjustment(s_coordinate8+sf16)\
        ,adjustment(s_coordinate9+sf16), adjustment(s_coordinate10+sf16), adjustment(s_coordinate11+sf16)\
        ,adjustment(s_coordinate12+sf16), adjustment(s_coordinate13+sf16), adjustment(s_coordinate14+sf16)\
        ,adjustment(s_coordinate15+sf16), adjustment(s_coordinate16+sf16))


        # initialize to primitive cell coordinate, y direction
        for k in range(0, dof): # yloop
            if k==1:
                s_coordinate1[k] = coordinate1[k]
                s_coordinate2[k] = coordinate2[k]
                s_coordinate3[k] = coordinate3[k]
                s_coordinate4[k] = coordinate4[k]
                s_coordinate5[k] = coordinate5[k]
                s_coordinate6[k] = coordinate6[k]
                s_coordinate7[k] = coordinate7[k]
                s_coordinate8[k] = coordinate8[k]
                s_coordinate9[k] = coordinate9[k]
                s_coordinate10[k] = coordinate10[k]
                s_coordinate11[k] = coordinate11[k]
                s_coordinate12[k] = coordinate12[k]
                s_coordinate13[k] = coordinate13[k]
                s_coordinate14[k] = coordinate14[k]
                s_coordinate15[k] = coordinate15[k]
                s_coordinate16[k] = coordinate16[k]

    # initialize to primitive cell coordinate, x & y direction
    for l in range(0, dof): # x & y loop
        if l==0 or l==1:
            s_coordinate1[l] = coordinate1[l]
            s_coordinate2[l] = coordinate2[l]
            s_coordinate3[l] = coordinate3[l]
            s_coordinate4[l] = coordinate4[l]
            s_coordinate5[l] = coordinate5[l]
            s_coordinate6[l] = coordinate6[l]
            s_coordinate7[l] = coordinate7[l]
            s_coordinate8[l] = coordinate8[l]
            s_coordinate9[l] = coordinate9[l]
            s_coordinate10[l] = coordinate10[l]
            s_coordinate11[l] = coordinate11[l]
            s_coordinate12[l] = coordinate12[l]
            s_coordinate13[l] = coordinate13[l]
            s_coordinate14[l] = coordinate14[l]
            s_coordinate15[l] = coordinate15[l]
            s_coordinate16[l] = coordinate16[l]

# end
end()

# time display
elapsed_time = time.time()-start
print("elapsed_time:{:.2f}".format(elapsed_time) + "[sec]")
