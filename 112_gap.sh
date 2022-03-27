### routine for device region ###
# correctly  working: checked by 114 cell output


#!/bin/bash
# extract only device region (si_4c_d.out)
pyhton split_c_device.py

# other text file clear
python file_clear_device.py

# delete and rename general files for IFCs extraction
pyhton split_c_del_change.py

python coordinate_ABINIT_extraction_for_device.py
python coordinate_generic_extraction_general.py
python coordinate_c_general_device_gap.py # heavy routine, only KC, input as lattice constant
python mat_construction_LCR_plus.py       # V_CL, V_CR, & KC
python unit_conversion_C.py