# force constant matrix extract & generation code from ABINIT output
# Coded by Takuro TOKUNAGA
# Last modified: August 11 2020

import numpy as np
import time
#import scipy.io
import itertools
from decimal import Decimal, ROUND_HALF_UP
start = time.time()

def GA7(argi,argj,argk,arg1,arg2,arg3,arg4,arg5,arg6,arg7,arg8,\
arg9,arg10,arg11,arg12,arg13,arg14,arg15,arg16):

    dof = 3            # degree of freedom
    atom_num = 16      # number of atom's in the primitive cell
    size= atom_num*dof # matrix size

    # coordinates of atoms in in the central region
    coord1 = arg1   # generic atom 1's coordinate
    coord2 = arg2   # generic atom 2's coordinate
    coord3 = arg3   # generic atom 3's coordinate
    coord4 = arg4   # generic atom 4's coordinate
    coord5 = arg5   # generic atom 5's coordinate
    coord6 = arg6   # generic atom 6's coordinate
    coord7 = arg7   # generic atom 7's coordinate
    coord8 = arg8   # generic atom 8's coordinate
    coord9 = arg9   # generic atom 9's coordinate
    coord10 = arg10 # generic atom 10's coordinate
    coord11 = arg11 # generic atom 11's coordinate
    coord12 = arg12 # generic atom 12's coordinate
    coord13 = arg13 # generic atom 13's coordinate
    coord14 = arg14 # generic atom 14's coordinate
    coord15 = arg15 # generic atom 15's coordinate
    coord16 = arg16 # generic atom 16's coordinate

    # file open, GA: Generic Atom
    if argk==-1:
        f1 =  open("../abinit/small_mat_center/general/si_4_Generic7_Generic1_K10_"+str(argi)+str(argj)+".txt", 'w')  # write mode
        f2 =  open("../abinit/small_mat_center/general/si_4_Generic7_Generic2_K10_"+str(argi)+str(argj)+".txt", 'w')  # write mode
        f3 =  open("../abinit/small_mat_center/general/si_4_Generic7_Generic3_K10_"+str(argi)+str(argj)+".txt", 'w')  # write mode
        f4 =  open("../abinit/small_mat_center/general/si_4_Generic7_Generic4_K10_"+str(argi)+str(argj)+".txt", 'w')  # write mode
        f5 =  open("../abinit/small_mat_center/general/si_4_Generic7_Generic5_K10_"+str(argi)+str(argj)+".txt", 'w')  # write mode
        f6 =  open("../abinit/small_mat_center/general/si_4_Generic7_Generic6_K10_"+str(argi)+str(argj)+".txt", 'w')  # write mode
        f7 =  open("../abinit/small_mat_center/general/si_4_Generic7_Generic7_K10_"+str(argi)+str(argj)+".txt", 'w')  # write mode
        f8 =  open("../abinit/small_mat_center/general/si_4_Generic7_Generic8_K10_"+str(argi)+str(argj)+".txt", 'w')  # write mode
        f9 =  open("../abinit/small_mat_center/general/si_4_Generic7_Generic9_K10_"+str(argi)+str(argj)+".txt", 'w')  # write mode
        f10 = open("../abinit/small_mat_center/general/si_4_Generic7_Generic10_K10_"+str(argi)+str(argj)+".txt", 'w') # write mode
        f11 = open("../abinit/small_mat_center/general/si_4_Generic7_Generic11_K10_"+str(argi)+str(argj)+".txt", 'w') # write mode
        f12 = open("../abinit/small_mat_center/general/si_4_Generic7_Generic12_K10_"+str(argi)+str(argj)+".txt", 'w') # write mode
        f13 = open("../abinit/small_mat_center/general/si_4_Generic7_Generic13_K10_"+str(argi)+str(argj)+".txt", 'w') # write mode
        f14 = open("../abinit/small_mat_center/general/si_4_Generic7_Generic14_K10_"+str(argi)+str(argj)+".txt", 'w') # write mode
        f15 = open("../abinit/small_mat_center/general/si_4_Generic7_Generic15_K10_"+str(argi)+str(argj)+".txt", 'w') # write mode
        f16 = open("../abinit/small_mat_center/general/si_4_Generic7_Generic16_K10_"+str(argi)+str(argj)+".txt", 'w') # write mode

    elif argk==0:
        f1 =  open("../abinit/small_mat_center/general/si_4_Generic7_Generic1_K00_"+str(argi)+str(argj)+".txt", 'w')  # write mode
        f2 =  open("../abinit/small_mat_center/general/si_4_Generic7_Generic2_K00_"+str(argi)+str(argj)+".txt", 'w')  # write mode
        f3 =  open("../abinit/small_mat_center/general/si_4_Generic7_Generic3_K00_"+str(argi)+str(argj)+".txt", 'w')  # write mode
        f4 =  open("../abinit/small_mat_center/general/si_4_Generic7_Generic4_K00_"+str(argi)+str(argj)+".txt", 'w')  # write mode
        f5 =  open("../abinit/small_mat_center/general/si_4_Generic7_Generic5_K00_"+str(argi)+str(argj)+".txt", 'w')  # write mode
        f6 =  open("../abinit/small_mat_center/general/si_4_Generic7_Generic6_K00_"+str(argi)+str(argj)+".txt", 'w')  # write mode
        f7 =  open("../abinit/small_mat_center/general/si_4_Generic7_Generic7_K00_"+str(argi)+str(argj)+".txt", 'w')  # write mode
        f8 =  open("../abinit/small_mat_center/general/si_4_Generic7_Generic8_K00_"+str(argi)+str(argj)+".txt", 'w')  # write mode
        f9 =  open("../abinit/small_mat_center/general/si_4_Generic7_Generic9_K00_"+str(argi)+str(argj)+".txt", 'w')  # write mode
        f10 = open("../abinit/small_mat_center/general/si_4_Generic7_Generic10_K00_"+str(argi)+str(argj)+".txt", 'w') # write mode
        f11 = open("../abinit/small_mat_center/general/si_4_Generic7_Generic11_K00_"+str(argi)+str(argj)+".txt", 'w') # write mode
        f12 = open("../abinit/small_mat_center/general/si_4_Generic7_Generic12_K00_"+str(argi)+str(argj)+".txt", 'w') # write mode
        f13 = open("../abinit/small_mat_center/general/si_4_Generic7_Generic13_K00_"+str(argi)+str(argj)+".txt", 'w') # write mode
        f14 = open("../abinit/small_mat_center/general/si_4_Generic7_Generic14_K00_"+str(argi)+str(argj)+".txt", 'w') # write mode
        f15 = open("../abinit/small_mat_center/general/si_4_Generic7_Generic15_K00_"+str(argi)+str(argj)+".txt", 'w') # write mode
        f16 = open("../abinit/small_mat_center/general/si_4_Generic7_Generic16_K00_"+str(argi)+str(argj)+".txt", 'w') # write mode

    elif argk==1:
        f1  = open("../abinit/small_mat_center/general/si_4_Generic7_Generic1_K01_"+str(argi)+str(argj)+".txt", 'w')  # write mode
        f2  = open("../abinit/small_mat_center/general/si_4_Generic7_Generic2_K01_"+str(argi)+str(argj)+".txt", 'w')  # write mode
        f3  = open("../abinit/small_mat_center/general/si_4_Generic7_Generic3_K01_"+str(argi)+str(argj)+".txt", 'w')  # write mode
        f4  = open("../abinit/small_mat_center/general/si_4_Generic7_Generic4_K01_"+str(argi)+str(argj)+".txt", 'w')  # write mode
        f5  = open("../abinit/small_mat_center/general/si_4_Generic7_Generic5_K01_"+str(argi)+str(argj)+".txt", 'w')  # write mode
        f6  = open("../abinit/small_mat_center/general/si_4_Generic7_Generic6_K01_"+str(argi)+str(argj)+".txt", 'w')  # write mode
        f7  = open("../abinit/small_mat_center/general/si_4_Generic7_Generic7_K01_"+str(argi)+str(argj)+".txt", 'w')  # write mode
        f8  = open("../abinit/small_mat_center/general/si_4_Generic7_Generic8_K01_"+str(argi)+str(argj)+".txt", 'w')  # write mode
        f9  = open("../abinit/small_mat_center/general/si_4_Generic7_Generic9_K01_"+str(argi)+str(argj)+".txt", 'w')  # write mode
        f10 = open("../abinit/small_mat_center/general/si_4_Generic7_Generic10_K01_"+str(argi)+str(argj)+".txt", 'w') # write mode
        f11 = open("../abinit/small_mat_center/general/si_4_Generic7_Generic11_K01_"+str(argi)+str(argj)+".txt", 'w') # write mode
        f12 = open("../abinit/small_mat_center/general/si_4_Generic7_Generic12_K01_"+str(argi)+str(argj)+".txt", 'w') # write mode
        f13 = open("../abinit/small_mat_center/general/si_4_Generic7_Generic13_K01_"+str(argi)+str(argj)+".txt", 'w') # write mode
        f14 = open("../abinit/small_mat_center/general/si_4_Generic7_Generic14_K01_"+str(argi)+str(argj)+".txt", 'w') # write mode
        f15 = open("../abinit/small_mat_center/general/si_4_Generic7_Generic15_K01_"+str(argi)+str(argj)+".txt", 'w') # write mode
        f16 = open("../abinit/small_mat_center/general/si_4_Generic7_Generic16_K01_"+str(argi)+str(argj)+".txt", 'w') # write mode

    else:
        print(str('error'))

    # open
    f0 = open('si_4c_general_7.txt', 'r') # read mode
    # lines
    lines0 = [line for line in f0]

    # atom number 1 of central region:
    moji1 = 'with coordinates'
    if coord1[0] >= 0:
        moji2 = '     ' # 5 space
        moji3 = np.format_float_scientific(Decimal(coord1[0]).quantize(Decimal("1.0E-11"),rounding=ROUND_HALF_UP), precision=6, unique=False, exp_digits=2).upper() # atom1 x

    elif coord1[0] < 0:
        moji2 = '    '  # 4 space
        moji3 = np.format_float_scientific(Decimal(coord1[0]).quantize(Decimal("1.0E-11"),rounding=ROUND_HALF_UP), precision=6, unique=False, exp_digits=2).upper() # atom1 x

    if coord1[1] >= 0:
        moji4 = '    '  # 4 space
        moji5 = np.format_float_scientific(Decimal(coord1[1]).quantize(Decimal("1.0E-11"),rounding=ROUND_HALF_UP), precision=6, unique=False, exp_digits=2).upper() # atom1 y

    elif coord1[1] < 0:
        moji4 = '   '   # 3 space
        moji5 = np.format_float_scientific(Decimal(coord1[1]).quantize(Decimal("1.0E-11"),rounding=ROUND_HALF_UP), precision=6, unique=False, exp_digits=2).upper() # atom1 y

    if coord1[2] >= 0:
        moji6 = '    '  # 4 space
        moji7 = np.format_float_scientific(Decimal(coord1[2]).quantize(Decimal("1.0E-11"),rounding=ROUND_HALF_UP), precision=6, unique=False, exp_digits=2).upper() # atom1 z

    elif coord1[2] < 0:
        moji6 = '   '   # 3 space
        moji7 = np.format_float_scientific(Decimal(coord1[2]).quantize(Decimal("1.0E-11"),rounding=ROUND_HALF_UP), precision=6, unique=False, exp_digits=2).upper() # atom1 z

    moji = moji1 + moji2 + moji3 + moji4 + moji5 + moji6 + moji7
    moji = str(moji)

    # # DEBUG:
    #if argi==0 and argj==0 and argk==0: # x y z
    #    print(moji)

    # write
    for i in lines0:
        if moji in i:
            for line in itertools.islice(lines0, int(lines0.index(i)+2), int(lines0.index(i)+5)):
                f1.write(line)

                # # DEBUG:
                #if argi==0 and argj==0 and argk==0: # x y z
                #    print(line)

    # atom number 2 of central region:
    moji1 = 'with coordinates'
    #print(coord2[0])
    if coord2[0] >= 0:
        moji2 = '     ' # 5 space
        moji3 = np.format_float_scientific(Decimal(coord2[0]).quantize(Decimal("1.0E-11"),rounding=ROUND_HALF_UP), precision=6, unique=False, exp_digits=2).upper() # atom2 x

    elif coord2[0] < 0:
        moji2 = '    '  # 4 space
        moji3 = np.format_float_scientific(Decimal(coord2[0]).quantize(Decimal("1.0E-11"),rounding=ROUND_HALF_UP), precision=6, unique=False, exp_digits=2).upper() # atom2 x

    if coord2[1] >= 0:
        moji4 = '    '  # 4 space
        moji5 = np.format_float_scientific(Decimal(coord2[1]).quantize(Decimal("1.0E-11"),rounding=ROUND_HALF_UP), precision=6, unique=False, exp_digits=2).upper() # atom2 y
    elif coord2[1] < 0:
        moji4 = '   '   # 3 space
        moji5 = np.format_float_scientific(Decimal(coord2[1]).quantize(Decimal("1.0E-11"),rounding=ROUND_HALF_UP), precision=6, unique=False, exp_digits=2).upper() # atom2 y

    if coord2[2] >= 0:
        moji6 = '    '  # 4 space
        moji7 = np.format_float_scientific(Decimal(coord2[2]).quantize(Decimal("1.0E-11"),rounding=ROUND_HALF_UP), precision=6, unique=False, exp_digits=2).upper() # atom2 z

    elif coord2[2] < 0:
        moji6 = '   ' # 3 space
        moji7 = np.format_float_scientific(Decimal(coord2[2]).quantize(Decimal("1.0E-11"),rounding=ROUND_HALF_UP), precision=6, unique=False, exp_digits=2).upper() # atom2 z

    moji = moji1 + moji2 + moji3 + moji4 + moji5 + moji6 + moji7
    moji = str(moji)

    # # DEBUG:
    #if argi==0 and argj==0 and argk==0: # x y z
    #    print(moji)

    # write
    for i in lines0:
        if moji in i: # 10
            for line in itertools.islice(lines0, int(lines0.index(i)+2), int(lines0.index(i)+5)):
                f2.write(line)

    # atom number 3 of central region:
    moji1 = 'with coordinates'
    if coord3[0] >= 0:
        moji2 = '     ' # 5 space
        moji3 = np.format_float_scientific(Decimal(coord3[0]).quantize(Decimal("1.0E-11"),rounding=ROUND_HALF_UP), precision=6, unique=False, exp_digits=2).upper() # atom3 x
    elif coord3[0] < 0:
        moji2 = '    '  # 4 space
        moji3 = np.format_float_scientific(Decimal(coord3[0]).quantize(Decimal("1.0E-11"),rounding=ROUND_HALF_UP), precision=6, unique=False, exp_digits=2).upper() # atom3 x

    if coord3[1] >= 0:
        moji4 = '    '  # 4 space
        moji5 = np.format_float_scientific(Decimal(coord3[1]).quantize(Decimal("1.0E-11"),rounding=ROUND_HALF_UP), precision=6, unique=False, exp_digits=2).upper() # atom3 y
    elif coord3[1] < 0:
        moji4 = '   '   # 3 space
        moji5 = np.format_float_scientific(Decimal(coord3[1]).quantize(Decimal("1.0E-11"),rounding=ROUND_HALF_UP), precision=6, unique=False, exp_digits=2).upper() # atom3 y

    if coord3[2] >= 0:
        moji6 = '    '  # 4 space
        moji7 = np.format_float_scientific(Decimal(coord3[2]).quantize(Decimal("1.0E-11"),rounding=ROUND_HALF_UP), precision=6, unique=False, exp_digits=2).upper() # atom3 z
    elif coord3[2] < 0:
        moji6 = '   '   # 3 space
        moji7 = np.format_float_scientific(Decimal(coord3[2]).quantize(Decimal("1.0E-11"),rounding=ROUND_HALF_UP), precision=6, unique=False, exp_digits=2).upper() # atom3 z

    moji = moji1 + moji2 + moji3 + moji4 + moji5 + moji6 + moji7
    moji = str(moji)

    # write
    for i in lines0:
        if moji in i: # 3
            for line in itertools.islice(lines0, int(lines0.index(i)+2), int(lines0.index(i)+5)):
                f3.write(line)

    # atom number 4 of central region:
    moji1 = 'with coordinates'
    if coord4[0] >= 0:
        moji2 = '     ' # 5 space
        moji3 = np.format_float_scientific(Decimal(coord4[0]).quantize(Decimal("1.0E-11"),rounding=ROUND_HALF_UP), precision=6, unique=False, exp_digits=2).upper() # atom4 x
    elif coord4[0] < 0:
        moji2 = '    '  # 4 space
        moji3 = np.format_float_scientific(Decimal(coord4[0]).quantize(Decimal("1.0E-11"),rounding=ROUND_HALF_UP), precision=6, unique=False, exp_digits=2).upper() # atom4 x

    if coord4[1] >= 0:
        moji4 = '    '  # 4 space
        moji5 = np.format_float_scientific(Decimal(coord4[1]).quantize(Decimal("1.0E-11"),rounding=ROUND_HALF_UP), precision=6, unique=False, exp_digits=2).upper() # atom4 y
    elif coord4[1] < 0:
        moji4 = '   '   # 3 space
        moji5 = np.format_float_scientific(Decimal(coord4[1]).quantize(Decimal("1.0E-11"),rounding=ROUND_HALF_UP), precision=6, unique=False, exp_digits=2).upper() # atom4 y

    if coord4[2] >= 0:
        moji6 = '    '  # 4 space
        moji7 = np.format_float_scientific(Decimal(coord4[2]).quantize(Decimal("1.0E-11"),rounding=ROUND_HALF_UP), precision=6, unique=False, exp_digits=2).upper() # atom4 z
    elif coord4[2] < 0:
        moji6 = '   '   # 3 space
        moji7 = np.format_float_scientific(Decimal(coord4[2]).quantize(Decimal("1.0E-11"),rounding=ROUND_HALF_UP), precision=6, unique=False, exp_digits=2).upper() # atom4 z

    moji = moji1 + moji2 + moji3 + moji4 + moji5 + moji6 + moji7
    moji = str(moji)

    # write
    for i in lines0:
        if moji in i: # 4
            for line in itertools.islice(lines0, int(lines0.index(i)+2), int(lines0.index(i)+5)):
                f4.write(line)

    # atom number 5 of central region:
    moji1 = 'with coordinates'
    if coord5[0] >= 0:
        moji2 = '     ' # 5 space
        moji3 = np.format_float_scientific(Decimal(coord5[0]).quantize(Decimal("1.0E-11"),rounding=ROUND_HALF_UP), precision=6, unique=False, exp_digits=2).upper() # atom5 x
    elif coord5[0] < 0:
        moji2 = '    '  # 4 space
        moji3 = np.format_float_scientific(Decimal(coord5[0]).quantize(Decimal("1.0E-11"),rounding=ROUND_HALF_UP), precision=6, unique=False, exp_digits=2).upper() # atom5 x

    if coord5[1] >= 0:
        moji4 = '    '  # 4 space
        moji5 = np.format_float_scientific(Decimal(coord5[1]).quantize(Decimal("1.0E-11"),rounding=ROUND_HALF_UP), precision=6, unique=False, exp_digits=2).upper() # atom5 y
    elif coord5[1] < 0:
        moji4 = '   '   # 3 space
        moji5 = np.format_float_scientific(Decimal(coord5[1]).quantize(Decimal("1.0E-11"),rounding=ROUND_HALF_UP), precision=6, unique=False, exp_digits=2).upper() # atom5 y

    if coord5[2] >= 0:
        moji6 = '    '  # 4 space
        moji7 = np.format_float_scientific(Decimal(coord5[2]).quantize(Decimal("1.0E-11"),rounding=ROUND_HALF_UP), precision=6, unique=False, exp_digits=2).upper() # atom5 z
    elif coord5[2] < 0:
        moji6 = '   '   # 3 space
        moji7 = np.format_float_scientific(Decimal(coord5[2]).quantize(Decimal("1.0E-11"),rounding=ROUND_HALF_UP), precision=6, unique=False, exp_digits=2).upper() # atom5 z

    moji = moji1 + moji2 + moji3 + moji4 + moji5 + moji6 + moji7
    moji = str(moji)

    # # DEBUG:
    #if argi==0 and argj==0 and argk==0: # x y z
    #    print(moji)

    # write
    for i in lines0:
        if moji in i: # 5
            for line in itertools.islice(lines0, int(lines0.index(i)+2), int(lines0.index(i)+5)):
                f5.write(line)

                # # DEBUG:
                #if argi==0 and argj==0 and argk==0: # x y z
                #    print(line)

    # atom number 6 of central region:
    moji1 = 'with coordinates'
    if coord6[0] >= 0:
        moji2 = '     ' # 5 space
        moji3 = np.format_float_scientific(Decimal(coord6[0]).quantize(Decimal("1.0E-11"),rounding=ROUND_HALF_UP), precision=6, unique=False, exp_digits=2).upper() # atom6 x
    elif coord6[0] < 0:
        moji2 = '    '  # 4 space
        moji3 = np.format_float_scientific(Decimal(coord6[0]).quantize(Decimal("1.0E-11"),rounding=ROUND_HALF_UP), precision=6, unique=False, exp_digits=2).upper() # atom6 x

    if coord6[1] >= 0:
        moji4 = '    '  # 4 space
        moji5 = np.format_float_scientific(Decimal(coord6[1]).quantize(Decimal("1.0E-11"),rounding=ROUND_HALF_UP), precision=6, unique=False, exp_digits=2).upper() # atom6 y
    elif coord6[1] < 0:
        moji4 = '   '   # 3 space
        moji5 = np.format_float_scientific(Decimal(coord6[1]).quantize(Decimal("1.0E-11"),rounding=ROUND_HALF_UP), precision=6, unique=False, exp_digits=2).upper() # atom6 y

    if coord6[2] >= 0:
        moji6 = '    '  # 4 space
        moji7 = np.format_float_scientific(Decimal(coord6[2]).quantize(Decimal("1.0E-11"),rounding=ROUND_HALF_UP), precision=6, unique=False, exp_digits=2).upper() # atom6 z
    elif coord6[2] < 0:
        moji6 = '   '   # 3 space
        moji7 = np.format_float_scientific(Decimal(coord6[2]).quantize(Decimal("1.0E-11"),rounding=ROUND_HALF_UP), precision=6, unique=False, exp_digits=2).upper() # atom6 z

    moji = moji1 + moji2 + moji3 + moji4 + moji5 + moji6 + moji7
    moji = str(moji)

    # write
    for i in lines0:
        if moji in i: # 6
            for line in itertools.islice(lines0, int(lines0.index(i)+2), int(lines0.index(i)+5)):
                f6.write(line)

    # atom number 7 of central region:
    moji1 = 'with coordinates'
    if coord7[0] >= 0:
        moji2 = '     ' # 5 space
        moji3 = np.format_float_scientific(Decimal(coord7[0]).quantize(Decimal("1.0E-11"),rounding=ROUND_HALF_UP), precision=6, unique=False, exp_digits=2).upper() # atom7 x
    elif coord7[0] < 0:
        moji2 = '    '  # 4 space
        moji3 = np.format_float_scientific(Decimal(coord7[0]).quantize(Decimal("1.0E-11"),rounding=ROUND_HALF_UP), precision=6, unique=False, exp_digits=2).upper() # atom7 x

    if coord7[1] >= 0:
        moji4 = '    '  # 4 space
        moji5 = np.format_float_scientific(Decimal(coord7[1]).quantize(Decimal("1.0E-11"),rounding=ROUND_HALF_UP), precision=6, unique=False, exp_digits=2).upper() # atom7 y
    elif coord7[1] < 0:
        moji4 = '   '   # 3 space
        moji5 = np.format_float_scientific(Decimal(coord7[1]).quantize(Decimal("1.0E-11"),rounding=ROUND_HALF_UP), precision=6, unique=False, exp_digits=2).upper() # atom7 y

    if coord7[2] >= 0:
        moji6 = '    '  # 4 space
        moji7 = np.format_float_scientific(Decimal(coord7[2]).quantize(Decimal("1.0E-11"),rounding=ROUND_HALF_UP), precision=6, unique=False, exp_digits=2).upper() # atom7 z
    elif coord7[2] < 0:
        moji6 = '   '   # 3 space
        moji7 = np.format_float_scientific(Decimal(coord7[2]).quantize(Decimal("1.0E-11"),rounding=ROUND_HALF_UP), precision=6, unique=False, exp_digits=2).upper() # atom7 z

    moji = moji1 + moji2 + moji3 + moji4 + moji5 + moji6 + moji7
    moji = str(moji)

    # write
    for i in lines0:
        if moji in i: # 7
            for line in itertools.islice(lines0, int(lines0.index(i)+2), int(lines0.index(i)+5)):
                f7.write(line)

    # atom number 8 of central region:
    moji1 = 'with coordinates'
    if coord8[0] >= 0:
        moji2 = '     ' # 5 space
        moji3 = np.format_float_scientific(Decimal(coord8[0]).quantize(Decimal("1.0E-11"),rounding=ROUND_HALF_UP), precision=6, unique=False, exp_digits=2).upper() # atom8 x
    elif coord8[0] < 0:
        moji2 = '    '  # 4 space
        moji3 = np.format_float_scientific(Decimal(coord8[0]).quantize(Decimal("1.0E-11"),rounding=ROUND_HALF_UP), precision=6, unique=False, exp_digits=2).upper() # atom8 x

    if coord8[1] >= 0:
        moji4 = '    '  # 4 space
        moji5 = np.format_float_scientific(Decimal(coord8[1]).quantize(Decimal("1.0E-11"),rounding=ROUND_HALF_UP), precision=6, unique=False, exp_digits=2).upper() # atom8 y
    elif coord8[1] < 0:
        moji4 = '   '   # 3 space
        moji5 = np.format_float_scientific(Decimal(coord8[1]).quantize(Decimal("1.0E-11"),rounding=ROUND_HALF_UP), precision=6, unique=False, exp_digits=2).upper() # atom8 y

    if coord8[2] >= 0:
        moji6 = '    '  # 4 space
        moji7 = np.format_float_scientific(Decimal(coord8[2]).quantize(Decimal("1.0E-11"),rounding=ROUND_HALF_UP), precision=6, unique=False, exp_digits=2).upper() # atom8 z
    elif coord8[2] < 0:
        moji6 = '   '   # 3 space
        moji7 = np.format_float_scientific(Decimal(coord8[2]).quantize(Decimal("1.0E-11"),rounding=ROUND_HALF_UP), precision=6, unique=False, exp_digits=2).upper() # atom8 z

    moji = moji1 + moji2 + moji3 + moji4 + moji5 + moji6 + moji7
    moji = str(moji)

    # write
    for i in lines0:
        if moji in i: # 8
            for line in itertools.islice(lines0, int(lines0.index(i)+2), int(lines0.index(i)+5)):
                f8.write(line)

    # atom number 9 of central region:
    moji1 = 'with coordinates'
    if coord9[0] >= 0:
        moji2 = '     ' # 5 space
        moji3 = np.format_float_scientific(Decimal(coord9[0]).quantize(Decimal("1.0E-11"),rounding=ROUND_HALF_UP), precision=6, unique=False, exp_digits=2).upper() # atom9 x
    elif coord9[0] < 0:
        moji2 = '    '  # 4 space
        moji3 = np.format_float_scientific(Decimal(coord9[0]).quantize(Decimal("1.0E-11"),rounding=ROUND_HALF_UP), precision=6, unique=False, exp_digits=2).upper() # atom9 x

    if coord9[1] >= 0:
        moji4 = '    '  # 4 space
        moji5 = np.format_float_scientific(Decimal(coord9[1]).quantize(Decimal("1.0E-11"),rounding=ROUND_HALF_UP), precision=6, unique=False, exp_digits=2).upper() # atom9 y
    elif coord9[1] < 0:
        moji4 = '   '   # 3 space
        moji5 = np.format_float_scientific(Decimal(coord9[1]).quantize(Decimal("1.0E-11"),rounding=ROUND_HALF_UP), precision=6, unique=False, exp_digits=2).upper() # atom9 y

    if coord9[2] >= 0:
        moji6 = '    '  # 4 space
        moji7 = np.format_float_scientific(Decimal(coord9[2]).quantize(Decimal("1.0E-11"),rounding=ROUND_HALF_UP), precision=6, unique=False, exp_digits=2).upper() # atom9 z
    elif coord9[2] < 0:
        moji6 = '   '   # 3 space
        moji7 = np.format_float_scientific(Decimal(coord9[2]).quantize(Decimal("1.0E-11"),rounding=ROUND_HALF_UP), precision=6, unique=False, exp_digits=2).upper() # atom9 z

    moji = moji1 + moji2 + moji3 + moji4 + moji5 + moji6 + moji7
    moji = str(moji)

    # write
    for i in lines0:
        if moji in i: # 9
            for line in itertools.islice(lines0, int(lines0.index(i)+2), int(lines0.index(i)+5)):
                f9.write(line)

    # atom number 10 of central region:
    moji1 = 'with coordinates'
    if coord10[0] >= 0:
        moji2 = '     ' # 5 space
        moji3 = np.format_float_scientific(Decimal(coord10[0]).quantize(Decimal("1.0E-11"),rounding=ROUND_HALF_UP), precision=6, unique=False, exp_digits=2).upper() # atom10 x
    elif coord10[0] < 0:
        moji2 = '    '  # 4 space
        moji3 = np.format_float_scientific(Decimal(coord10[0]).quantize(Decimal("1.0E-11"),rounding=ROUND_HALF_UP), precision=6, unique=False, exp_digits=2).upper() # atom10 x

    if coord10[1] >= 0:
        moji4 = '    '  # 4 space
        moji5 = np.format_float_scientific(Decimal(coord10[1]).quantize(Decimal("1.0E-11"),rounding=ROUND_HALF_UP), precision=6, unique=False, exp_digits=2).upper() # atom10 y
    elif coord10[1] < 0:
        moji4 = '   '   # 3 space
        moji5 = np.format_float_scientific(Decimal(coord10[1]).quantize(Decimal("1.0E-11"),rounding=ROUND_HALF_UP), precision=6, unique=False, exp_digits=2).upper() # atom10 y

    if coord10[2] >= 0:
        moji6 = '    '  # 4 space
        moji7 = np.format_float_scientific(Decimal(coord10[2]).quantize(Decimal("1.0E-11"),rounding=ROUND_HALF_UP), precision=6, unique=False, exp_digits=2).upper() # atom10 z
    elif coord10[2] < 0:
        moji6 = '   '   # 3 space
        moji7 = np.format_float_scientific(Decimal(coord10[2]).quantize(Decimal("1.0E-11"),rounding=ROUND_HALF_UP), precision=6, unique=False, exp_digits=2).upper() # atom10 z

    moji = moji1 + moji2 + moji3 + moji4 + moji5 + moji6 + moji7
    moji = str(moji)

    # write
    for i in lines0:
        if moji in i: # 10
            for line in itertools.islice(lines0, int(lines0.index(i)+2), int(lines0.index(i)+5)):
                f10.write(line)

    # atom number 11 of central region:
    moji1 = 'with coordinates'
    if coord11[0] >= 0:
        moji2 = '     ' # 5 space
        moji3 = np.format_float_scientific(Decimal(coord11[0]).quantize(Decimal("1.0E-11"),rounding=ROUND_HALF_UP), precision=6, unique=False, exp_digits=2).upper() # atom11 x
    elif coord11[0] < 0:
        moji2 = '    '  # 4 space
        moji3 = np.format_float_scientific(Decimal(coord11[0]).quantize(Decimal("1.0E-11"),rounding=ROUND_HALF_UP), precision=6, unique=False, exp_digits=2).upper() # atom11 x

    if coord11[1] >= 0:
        moji4 = '    '  # 4 space
        moji5 = np.format_float_scientific(Decimal(coord11[1]).quantize(Decimal("1.0E-11"),rounding=ROUND_HALF_UP), precision=6, unique=False, exp_digits=2).upper() # atom11 y
    elif coord11[1] < 0:
        moji4 = '   '   # 3 space
        moji5 = np.format_float_scientific(Decimal(coord11[1]).quantize(Decimal("1.0E-11"),rounding=ROUND_HALF_UP), precision=6, unique=False, exp_digits=2).upper() # atom11 y

    if coord11[2] >= 0:
        moji6 = '    '  # 4 space
        moji7 = np.format_float_scientific(Decimal(coord11[2]).quantize(Decimal("1.0E-11"),rounding=ROUND_HALF_UP), precision=6, unique=False, exp_digits=2).upper() # atom11 z
    elif coord11[2] < 0:
        moji6 = '   '   # 3 space
        moji7 = np.format_float_scientific(Decimal(coord11[2]).quantize(Decimal("1.0E-11"),rounding=ROUND_HALF_UP), precision=6, unique=False, exp_digits=2).upper() # atom11 z

    moji = moji1 + moji2 + moji3 + moji4 + moji5 + moji6 + moji7
    moji = str(moji)

    # write
    for i in lines0:
        if moji in i: # 11
            for line in itertools.islice(lines0, int(lines0.index(i)+2), int(lines0.index(i)+5)):
                f11.write(line)

    # atom number 12 of central region:
    moji1 = 'with coordinates'
    if coord12[0] >= 0:
        moji2 = '     ' # 5 space
        moji3 = np.format_float_scientific(Decimal(coord12[0]).quantize(Decimal("1.0E-11"),rounding=ROUND_HALF_UP), precision=6, unique=False, exp_digits=2).upper() # atom12 x
    elif coord12[0] < 0:
        moji2 = '    '  # 4 space
        moji3 = np.format_float_scientific(Decimal(coord12[0]).quantize(Decimal("1.0E-11"),rounding=ROUND_HALF_UP), precision=6, unique=False, exp_digits=2).upper() # atom12 x

    if coord12[1] >= 0:
        moji4 = '    '  # 4 space
        moji5 = np.format_float_scientific(Decimal(coord12[1]).quantize(Decimal("1.0E-11"),rounding=ROUND_HALF_UP), precision=6, unique=False, exp_digits=2).upper() # atom12 y
    elif coord12[1] < 0:
        moji4 = '   '   # 3 space
        moji5 = np.format_float_scientific(Decimal(coord12[1]).quantize(Decimal("1.0E-11"),rounding=ROUND_HALF_UP), precision=6, unique=False, exp_digits=2).upper() # atom12 y

    if coord12[2] >= 0:
        moji6 = '    '  # 4 space
        moji7 = np.format_float_scientific(Decimal(coord12[2]).quantize(Decimal("1.0E-11"),rounding=ROUND_HALF_UP), precision=6, unique=False, exp_digits=2).upper() # atom12 z
    elif coord12[2] < 0:
        moji6 = '   '   # 3 space
        moji7 = np.format_float_scientific(Decimal(coord12[2]).quantize(Decimal("1.0E-11"),rounding=ROUND_HALF_UP), precision=6, unique=False, exp_digits=2).upper() # atom12 z

    moji = moji1 + moji2 + moji3 + moji4 + moji5 + moji6 + moji7
    moji = str(moji)

    # write
    for i in lines0:
        if moji in i: # 12
            for line in itertools.islice(lines0, int(lines0.index(i)+2), int(lines0.index(i)+5)):
                f12.write(line)

    # atom number 13 of central region:
    moji1 = 'with coordinates'
    if coord13[0] >= 0:
        moji2 = '     ' # 5 space
        moji3 = np.format_float_scientific(Decimal(coord13[0]).quantize(Decimal("1.0E-11"),rounding=ROUND_HALF_UP), precision=6, unique=False, exp_digits=2).upper() # atom13 x
    elif coord13[0] < 0:
        moji2 = '    '  # 4 space
        moji3 = np.format_float_scientific(Decimal(coord13[0]).quantize(Decimal("1.0E-11"),rounding=ROUND_HALF_UP), precision=6, unique=False, exp_digits=2).upper() # atom13 x

    if coord13[1] >= 0:
        moji4 = '    '  # 4 space
        moji5 = np.format_float_scientific(Decimal(coord13[1]).quantize(Decimal("1.0E-11"),rounding=ROUND_HALF_UP), precision=6, unique=False, exp_digits=2).upper() # atom13 y
    elif coord13[1] < 0:
        moji4 = '   '   # 3 space
        moji5 = np.format_float_scientific(Decimal(coord13[1]).quantize(Decimal("1.0E-11"),rounding=ROUND_HALF_UP), precision=6, unique=False, exp_digits=2).upper() # atom13 y

    if coord13[2] >= 0:
        moji6 = '    '  # 4 space
        moji7 = np.format_float_scientific(Decimal(coord13[2]).quantize(Decimal("1.0E-11"),rounding=ROUND_HALF_UP), precision=6, unique=False, exp_digits=2).upper() # atom13 z
    elif coord13[2] < 0:
        moji6 = '   '   # 3 space
        moji7 = np.format_float_scientific(Decimal(coord13[2]).quantize(Decimal("1.0E-11"),rounding=ROUND_HALF_UP), precision=6, unique=False, exp_digits=2).upper() # atom13 z

    moji = moji1 + moji2 + moji3 + moji4 + moji5 + moji6 + moji7
    moji = str(moji)

    # write
    for i in lines0:
        if moji in i: # 13
            for line in itertools.islice(lines0, int(lines0.index(i)+2), int(lines0.index(i)+5)):
                f13.write(line)

                # # DEBUG:
                #if argi==0 and argj==0 and argk==1: # x y z
                #    print(line)

    # atom number 14 of central region:
    moji1 = 'with coordinates'
    if coord14[0] >= 0:
        moji2 = '     ' # 5 space
        moji3 = np.format_float_scientific(Decimal(coord14[0]).quantize(Decimal("1.0E-11"),rounding=ROUND_HALF_UP), precision=6, unique=False, exp_digits=2).upper() # atom14 x
    elif coord14[0] < 0:
        moji2 = '    '  # 4 space
        moji3 = np.format_float_scientific(Decimal(coord14[0]).quantize(Decimal("1.0E-11"),rounding=ROUND_HALF_UP), precision=6, unique=False, exp_digits=2).upper() # atom14 x

    if coord14[1] >= 0:
        moji4 = '    '  # 4 space
        moji5 = np.format_float_scientific(Decimal(coord14[1]).quantize(Decimal("1.0E-11"),rounding=ROUND_HALF_UP), precision=6, unique=False, exp_digits=2).upper() # atom14 y
    elif coord14[1] < 0:
        moji4 = '   '   # 3 space
        moji5 = np.format_float_scientific(Decimal(coord14[1]).quantize(Decimal("1.0E-11"),rounding=ROUND_HALF_UP), precision=6, unique=False, exp_digits=2).upper() # atom14 y

    if coord14[2] >= 0:
        moji6 = '    '  # 4 space
        moji7 = np.format_float_scientific(Decimal(coord14[2]).quantize(Decimal("1.0E-11"),rounding=ROUND_HALF_UP), precision=6, unique=False, exp_digits=2).upper() # atom14 z
    elif coord14[2] < 0:
        moji6 = '   '   # 3 space
        moji7 = np.format_float_scientific(Decimal(coord14[2]).quantize(Decimal("1.0E-11"),rounding=ROUND_HALF_UP), precision=6, unique=False, exp_digits=2).upper() # atom14 z

    moji = moji1 + moji2 + moji3 + moji4 + moji5 + moji6 + moji7
    moji = str(moji)

    # write
    for i in lines0:
        if moji in i: # 14
            for line in itertools.islice(lines0, int(lines0.index(i)+2), int(lines0.index(i)+5)):
                f14.write(line)

    # atom number 15 of central region:
    moji1 = 'with coordinates'
    if coord15[0] >= 0:
        moji2 = '     ' # 5 space
        moji3 = np.format_float_scientific(Decimal(coord15[0]).quantize(Decimal("1.0E-11"),rounding=ROUND_HALF_UP), precision=6, unique=False, exp_digits=2).upper() # atom15 x
    elif coord15[0] < 0:
        moji2 = '    '  # 4 space
        moji3 = np.format_float_scientific(Decimal(coord15[0]).quantize(Decimal("1.0E-11"),rounding=ROUND_HALF_UP), precision=6, unique=False, exp_digits=2).upper() # atom15 x

    if coord15[1] >= 0:
        moji4 = '    '  # 4 space
        moji5 = np.format_float_scientific(Decimal(coord15[1]).quantize(Decimal("1.0E-11"),rounding=ROUND_HALF_UP), precision=6, unique=False, exp_digits=2).upper() # atom15 y
    elif coord15[1] < 0:
        moji4 = '   '   # 3 space
        moji5 = np.format_float_scientific(Decimal(coord15[1]).quantize(Decimal("1.0E-11"),rounding=ROUND_HALF_UP), precision=6, unique=False, exp_digits=2).upper() # atom15 y

    if coord15[2] >= 0:
        moji6 = '    '  # 4 space
        moji7 = np.format_float_scientific(Decimal(coord15[2]).quantize(Decimal("1.0E-11"),rounding=ROUND_HALF_UP), precision=6, unique=False, exp_digits=2).upper() # atom15 z
    elif coord15[2] < 0:
        moji6 = '   '   # 3 space
        moji7 = np.format_float_scientific(Decimal(coord15[2]).quantize(Decimal("1.0E-11"),rounding=ROUND_HALF_UP), precision=6, unique=False, exp_digits=2).upper() # atom15 z

    moji = moji1 + moji2 + moji3 + moji4 + moji5 + moji6 + moji7
    moji = str(moji)

    # write
    for i in lines0:
        if moji in i: # 15
            for line in itertools.islice(lines0, int(lines0.index(i)+2), int(lines0.index(i)+5)):
                f15.write(line)

    # atom number 16 of central region:
    moji1 = 'with coordinates'
    if coord16[0] >= 0:
        moji2 = '     ' # 5 space
        moji3 = np.format_float_scientific(Decimal(coord16[0]).quantize(Decimal("1.0E-11"),rounding=ROUND_HALF_UP), precision=6, unique=False, exp_digits=2).upper() # atom16 x
    elif coord16[0] < 0:
        moji2 = '    '  # 4 space
        moji3 = np.format_float_scientific(Decimal(coord16[0]).quantize(Decimal("1.0E-11"),rounding=ROUND_HALF_UP), precision=6, unique=False, exp_digits=2).upper() # atom16 x

    if coord16[1] >= 0:
        moji4 = '    '  # 4 space
        moji5 = np.format_float_scientific(Decimal(coord16[1]).quantize(Decimal("1.0E-11"),rounding=ROUND_HALF_UP), precision=6, unique=False, exp_digits=2).upper() # atom16 y
    elif coord16[1] < 0:
        moji4 = '   '   # 3 space
        moji5 = np.format_float_scientific(Decimal(coord16[1]).quantize(Decimal("1.0E-11"),rounding=ROUND_HALF_UP), precision=6, unique=False, exp_digits=2).upper() # atom16 y

    if coord16[2] >= 0:
        moji6 = '    '  # 4 space
        moji7 = np.format_float_scientific(Decimal(coord16[2]).quantize(Decimal("1.0E-11"),rounding=ROUND_HALF_UP), precision=6, unique=False, exp_digits=2).upper() # atom16 z
    elif coord16[2] < 0:
        moji6 = '   '   # 3 space
        moji7 = np.format_float_scientific(Decimal(coord16[2]).quantize(Decimal("1.0E-11"),rounding=ROUND_HALF_UP), precision=6, unique=False, exp_digits=2).upper() # atom16 z

    moji = moji1 + moji2 + moji3 + moji4 + moji5 + moji6 + moji7
    moji = str(moji)

    # write
    for i in lines0:
        if moji in i: # 16
            for line in itertools.islice(lines0, int(lines0.index(i)+2), int(lines0.index(i)+5)):
                f16.write(line)

    # file close
    f0.close()
    f1.close()
    f2.close()
    f3.close()
    f4.close()
    f5.close()
    f6.close()
    f7.close()
    f8.close()
    f9.close()
    f10.close()
    f11.close()
    f12.close()
    f13.close()
    f14.close()
    f15.close()
    f16.close()

    return 0

# time display
elapsed_time = time.time()-start
#print("elapsed_time:{:.2f}".format(elapsed_time) + "[sec]")
