#!/usr/bin/env python3
import os, sys, glob
from reeds.modules import do_RE_EDS_eoffEstimation as eoffEstm


sys.path.append(os.getcwd())

from global_definitions import fM, bash
from global_definitions import name, root_dir
from global_definitions import gromosXX_bin, gromosPP_bin, ene_ana_lib
from global_definitions import in_top_file, in_pert_file, in_disres_file, in_template_reeds_imd, in_qmmm_file

#STEP specifics
out_eoff_dir = root_dir+"/c_eoff_equil"
next_lowerBound_dir = root_dir+"/b_lowerBound/analysis/next"
sval_file = root_dir + "/b_lowerBound/analysis/next/s_vals.csv"
optimized_states = root_dir + "/a_optimizedState/analysis/next"
in_name = name+"_energy_offsets"

##make folder
out_eoff_dir = bash.make_folder(out_eoff_dir)

#In- Files
topology = fM.Topology(top_path=in_top_file, disres_path=in_disres_file, perturbation_path=in_pert_file, qmmm_path=in_qmmm_file)
coords  =glob.glob(next_lowerBound_dir+"/*.cnf")
system = fM.System(coordinates=coords, name=in_name, top=topology)

last_jobID = eoffEstm.do(out_root_dir=out_eoff_dir, 
                         in_simSystem=system, 
                         in_template_imd_path=in_template_reeds_imd, 
                         in_ene_ana_lib=ene_ana_lib, 
                         verbose=True, 
                         submit=True,
                         #, exclude_residues="WAT",  
                         duration_per_job="120:00:00", 
                         do_not_doubly_submit_to_queue=False,  
                         sval_file = sval_file, 
                         optimized_states=optimized_states,  
                         nmpi_per_replica=16, 
                         gromosXX_bin_dir=gromosXX_bin,  
                         gromosPP_bin_dir=gromosPP_bin, 
                         num_simulation_runs = 1, 
                         steps_between_trials=200, 
                         trials_per_run=10000)
