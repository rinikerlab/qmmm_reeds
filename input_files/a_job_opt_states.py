#!/usr/bin/env python3
import os, sys, glob
from reeds.modules import do_RE_EDS_generateOptimizedStates as optimizeStates 

sys.path.append(os.getcwd())

from global_definitions import fM, bash
from global_definitions import name, root_dir
from global_definitions import gromosXX_bin, gromosPP_bin, ene_ana_lib
from global_definitions import in_top_file, in_cnf_file, in_pert_file, in_disres_file, in_template_md_imd, in_qmmm_file

#STEP specifics
out_gOptStates_dir = root_dir+"/a_optimizedState"
in_name = name + "_optimize_single_state"

##make folder
out_gOptStates_dir = bash.make_folder(out_gOptStates_dir)

#In- Files
topology_state_opt = fM.Topology(top_path=in_top_file, disres_path=in_disres_file, perturbation_path=in_pert_file, qmmm_path = in_qmmm_file)
system = fM.System(coordinates=in_cnf_file, name=in_name, top=topology_state_opt)
print(system)

#DO
optimizeStates.do(in_simSystem=system,
                  in_imd_template_path=in_template_md_imd, 
                  out_root_dir=out_gOptStates_dir,
                  in_gromosXX_bin_dir=gromosXX_bin, 
                  vacuum_simulation=False, 
                  memory = 2048, 
                  nmpi_per_replica=56,
                  simulation_steps=2000000,
                  job_duration="288:00:00",  
                  ene_ana_lib=ene_ana_lib)

