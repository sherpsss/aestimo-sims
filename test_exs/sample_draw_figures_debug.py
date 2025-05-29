#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -------------------------------------------------------------------
# Input File Description:  Barrier doped AlGaAs/GaAs heterostructure.
# -------------------------------------------------------------------
# ----------------
# GENERAL SETTINGS
# ----------------
import time
import sys
from os import path
sys.path.append(path.join(path.dirname(__file__), '..'))

import aestimo
import database
time0 = time.time() # timing audit
# TEMPERATURE
T = 300.0 #Kelvin

# COMPUTATIONAL SCHEME
# 0: Schrodinger
# 1: Schrodinger + nonparabolicity
# 2: Schrodinger-Poisson
# 3: Schrodinger-Poisson with nonparabolicity
# 4: Schrodinger-Exchange interaction
# 5: Schrodinger-Poisson + Exchange interaction
# 6: Schrodinger-Poisson + Exchange interaction with nonparabolicity
# 7: Schrodinger-Poisson-Drift_Diffusion (Schrodinger solved with poisson then  poisson and DD)
# 8: Schrodinger-Poisson-Drift_Diffusion (Schrodinger solved with poisson and DD)
# 9: Schrodinger-Poisson-Drift_Diffusion (Schrodinger solved with poisson and DD) using Gummel & Newton map
computation_scheme = 2
# drawFigures = True

# QUANTUM
# Total subband number to be calculated for electrons
subnumber_h = 10
subnumber_e = 2
# APPLIED ELECTRIC FIELD
Fapplied =  0.0# (V/m)-20e8
vmax= 1.3
vmin= 0.0
Each_Step=0.05# --------------------------------
# REGIONAL SETTINGS FOR SIMULATION
# --------------------------------
contact=0.0
# GRID
# For 1D, z-axis is choosen
gridfactor = 0.2#nm
maxgridpoints = 200000 #for controlling the size
mat_type='Zincblende'
# REGIONS
# Region input is a two-dimensional list input.
# An example:
# Si p-n diode. Firstly lets picturize the regional input.
#         | Thickness (nm) | Material | Alloy fraction | Doping(cm^-3) | n or p type |
# Layer 0 |      250.0     |   Si     |      0         |     1e16      |     n       |
# Layer 1 |      250.0     |   Si     |      0         |     1e16      |     p       |
#
# To input this list in Gallium, we use lists as:
doping_conc = 0.5e17
barrier_type_dope = 'n'
well_width = 4.5

material=[[ 20.0, 'AlGaAs',  0.53, 0.47, doping_conc, 'n','b'],
            [10.0, 'AlGaAs', 0.53, 0.47,doping_conc, barrier_type_dope,'b'],
            [ well_width, 'GaAs', 0.0, 0.0, 0, 'i','w'],
            [10.0, 'AlGaAs', 0.53, 0.47, doping_conc,barrier_type_dope,'b'],
            [ well_width, 'GaAs', 0.0, 0.0, 0, 'i','w'],
            [10.0, 'AlGaAs', 0.53, 0.47, doping_conc, barrier_type_dope,'b'],
            [ well_width, 'GaAs', 0.0, 0.0, 0, 'i','w'],
            [10.0, 'AlGaAs', 0.53, 0.47, doping_conc, barrier_type_dope,'b'],
            [well_width, 'GaAs', 0.0, 0.0, 0, 'i','w'],
            [10.0, 'AlGaAs', 0.53, 0.47,doping_conc, barrier_type_dope,'b'],
            [ 20.0, 'AlGaAs', 0.53, 0.47, doping_conc, 'n','b']]
#----------------------------------------
import numpy as np
x_max = sum([layer[0] for layer in material])
def round2int(x):
    return int(x+0.5)
n_max=round2int(x_max/gridfactor)
#----------------------------------------
dop_profile=np.zeros(n_max)
#----------------------------------------
Quantum_Regions=False
Quantum_Regions_boundary=np.zeros((1,2))
Quantum_Regions_boundary[0,0]=25
Quantum_Regions_boundary[0,1]=70
#----------------------------------------
surface=np.zeros(2)
#surface[0]=-0.6
#----------------------------------------
# inputfilename = "sample_2qw_AlGaAs_GaAs"
# drawfigures = True
# from os import path

input_obj = vars()
# drawFigures = True
model = aestimo.StructureFrom(input_obj, database)
result = aestimo.Poisson_Schrodinger(model)
# %matplotlib inline
aestimo.drawFigures = True
aestimo.save_and_plot(result,model)
# solver.logger.info("Simulation is finished.")

# if __name__ == "__main__": #this code allows you to run the input file directly
#     input_obj = vars()
#     # drawFigures = True
#     import sys
#     sys.path.append(path.join(path.dirname(__file__), '..'))
#     import aestimo
#     aestimo.run_aestimo(input_obj)

time1 = time.time()
print("total running time=",time1-time0)
