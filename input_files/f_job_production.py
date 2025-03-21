#!/usr/bin/env python3
import os, sys, glob
from reeds.modules import do_RE_EDS_production as production

sys.path.append(os.getcwd())

from global_definitions import fM, bash
from global_definitions import name, root_dir
from global_definitions import gromosXX_bin, gromosPP_bin, ene_ana_lib
from global_definitions import in_top_file, in_pert_file, in_disres_file, in_qmmm_file
from global_definitions import undersampling_frac_thresh
from global_definitions import undersampling_occurrence_fraction

        
#STEP Specifics
in_name = name + "prod_4"
next_production_dir = root_dir+"/input_production" #CHANGE HERE
out_production_dir = root_dir+"/f_" + in_name
optimized_states_dir = root_dir + "/a_optimizedState/analysis/next"
lower_bound_dir = root_dir + "/b_lowerBound/analysis/next"
 
##make folder
out_production_dir = bash.make_folder(out_production_dir)

#In-Files
topology = fM.Topology(top_path=in_top_file, disres_path=in_disres_file, perturbation_path=in_pert_file, qmmm_path=in_qmmm_file)
coords = glob.glob(next_production_dir+"/*cnf") 
system = fM.System(coordinates=coords, name=in_name, top=topology)
in_template_reeds_imd = glob.glob(next_production_dir+"/*imd")[0]

print(system)

memory=2000

#Do:
last_jobID = production.do(out_root_dir=out_production_dir,
                           in_simSystem=system,
                           in_template_imd=in_template_reeds_imd, 
                           in_ene_ana_lib_path=ene_ana_lib,
                           verbose=True,
                           gromosXX_bin_dir = gromosXX_bin,
                           gromosPP_bin_dir= gromosPP_bin,
                           undersampling_fraction_threshold=undersampling_occurrence_fraction,
                           num_simulation_runs=1, 
                           submit=True,
                           do_not_doubly_submit_to_queue = False,
                           optimized_states_dir = optimized_states_dir,
                           lower_bound_dir = lower_bound_dir,
                           nmpi_per_replica=4,
                           memory = memory,
                           duration_per_job = "14-00:00:00",
                           randomize=True)

