#!/usr/bin/env python3
import os, sys, glob
sys.path.append(os.getcwd())

from global_definitions import fM, bash
from global_definitions import name, root_dir
from global_definitions import gromosXX_bin, gromosPP_bin, ene_ana_lib
from global_definitions import in_top_file, in_pert_file, in_disres_file, in_template_reeds_imd, in_qmmm_file
from global_definitions import undersampling_occurrence_fraction

from reeds.modules import do_RE_EDS_mixedOptimisation as mixedOpt

#Paths
in_name = name+"_mixed_opt"
out_sopt_dir = root_dir+"/d_mixedOptimization"
next_sopt_dir = root_dir+"/c_eoff_equil/analysis/next/"
optimized_states_dir = root_dir + "/a_optimizedState/analysis/next"
lower_bound_dir = root_dir + "/b_lowerBound/analysis/next"

##make folder
out_sopt_dir = bash.make_folder(out_sopt_dir)

#In-Files
topology = fM.Topology(top_path=in_top_file, disres_path=in_disres_file, perturbation_path=in_pert_file, qmmm_path=in_qmmm_file)
coords = glob.glob(next_sopt_dir+"/*cnf")
system = fM.System(coordinates=coords, name=in_name, top=topology)
print(system)

#Additional Options
## Simulation Params
job_duration="48:00:00"
nmpi_per_replica = 4
iterations = 10
memory = 1000

## EoffRB - Params
learningFactors = None
individualCorrection = False
### Intensity factor
intensity_factor = 5

# S-opt options
run_NGRTO = True
run_NLRTO = False
sOpt_add_replicas = 0



last_jobID = mixedOpt.do(out_root_dir=out_sopt_dir,
                         in_simSystem=system,
                         in_template_imd=next_sopt_dir+"next.imd",
                         in_ene_ana_lib_path=ene_ana_lib,
                         undersampling_fraction_threshold=undersampling_occurrence_fraction,
                         nmpi_per_replica=nmpi_per_replica,
                         duration_per_job = job_duration,
                         iterations=iterations,
                         learningFactors=learningFactors,
                         individualCorrection=individualCorrection,
                         verbose= True,
                         memory = memory,
                         steps_between_trials = 100,
                         trials_per_run = 5000,
                         run_NGRTO = run_NGRTO,
                         run_NLRTO = run_NLRTO,
                         sOpt_add_replicas = sOpt_add_replicas,
                         optimized_states_dir = optimized_states_dir,
                         lower_bound_dir = lower_bound_dir,
                         intensity_factor = intensity_factor,
                         in_gromosPP_bin_dir=gromosPP_bin,
                         in_gromosXX_bin_dir=gromosXX_bin,
                         submit = True,
                         equil_runs = 0
                      )
