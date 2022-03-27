### comments ###
Inputs:
si_4c_d.out for split_c_device.py / coordinate_ABINIT_extraction_for_device.py
normalized_coordinate.txt / coordinate_generic_input_extraction.py

Outputs:
ABINIT_coordinates_general.txt by coordinate_ABINIT_extraction_for_device.py (whole the coordinates)
ABINIT_generic_atoms_coordinates_output.txt by coordinate_generic_extraction_general.py (coordinates for generic atoms)
################


#!/bin/bash
# extract only device region (si_4c_d.out)
python split_c_device.py
python coordinate_generic_extraction_LR.py        # left & right region 
python coordinate_generic_input_extraction.py

# previous text file clear
python file_clear_device.py

# delete and rename general files for IFCs extraction
pyhton split_c_del_change.py

python coordinate_ABINIT_extraction_for_device.py # device region
python coordinate_generic_extraction_general.py   # device region
python coordinate_c_surface_reconstruction.py     # heavy routine, only KC, input as lattice constant
python mat_construction_LCR_plus.py               # V_CL, V_CR, & KC
python unit_conversion_C.py
python copy_rename_LCR.py                         # copy rotine: copy V_CL for K01L, V_CR for K10L, and KC for K00L
