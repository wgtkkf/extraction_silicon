#!/bin/bash
# file clear
python file_clear.py

python coordinate_ABINIT_extraction_general.py  # consistent input file name
python split_c_general.py                       # consistent input file name
python coordinate_generic_extraction_general.py # consistent input file name

# routine for V_CL, V_CR, & KC
python coordinate_c_general_plus.py # heavy routine, input as lattice constant
python mat_construction_LCR_plus.py # V_CL, V_CR, & KC

# all unit conversion
python unit_conversion_C.py

# copy rotine: copy V_CL for K01L, V_CR for K10L, and KC for K00L
python copy_rename_LCR.py

# mass
python mass_matrices_supercell.py 