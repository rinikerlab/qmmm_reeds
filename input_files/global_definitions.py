import os
from pygromos.utils import bash
from pygromos.euler_submissions import FileManager as fM

#needs to be provided via gromos compiling
gromosXX_bin = '/cluster/home/dpregeljc/src/gromos_alchemicalqmmm/build/program'
gromosPP_bin = '/cluster/home/dpregeljc/src/gromosPlsPls_ubuntu/gromos++/bin'
ene_ana_lib ="/cluster/home/dpregeljc/src/reeds/reeds/data/ene_ana_libs/new_ene_ana_REEDS_8state.md++.lib"

#System Dependent settings:
name = "diols_QMMM"
root_dir = os.getcwd()
input_folder =    root_dir+"/0_input"

print(root_dir)

##input Files
###general Templates
in_template_md_imd = input_folder+"/template_md.imd"
in_template_reeds_imd = input_folder+"/template_reeds.imd"

###System dependent Files
in_cnf_file =     input_folder+"/md_diols.cnf"
in_top_file =     input_folder+"/diols_cut.top"
in_pert_file =    input_folder+"/pert_eds.ptp"
in_disres_file =  input_folder+"/disres.dsr"
in_qmmm_file =    input_folder+"/diols.qmmm"

undersampling_frac_thresh = "a_optimizedState/analysis/next/state_occurence_physical_pot_thresh.csv"
undersampling_occurrence_fraction = 0.9


