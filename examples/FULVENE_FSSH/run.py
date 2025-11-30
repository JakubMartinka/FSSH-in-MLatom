import os
import mlatom as ml
import numpy as np

root_dir = os.getcwd()

# Load initial conditions
init_cond_db = ml.data.molecular_database.load(f'{root_dir}/data/ic.json', format="json")

# Set singlepoint calculation
col = ml.models.methods(program='columbus', command_line_arguments=['-m','1700'], directory_with_input_files='%s/data/sp_input' % root_dir, save_files_in_currect_directory=False)

# Set NAMD arguments
maximum_propagation_time = 60
time_step = 0.1
time_step_tdse = None
nstates = 2
initial_state = 1

namd_kwargs = {
            'model': col,
            'time_step': time_step,
            'time_step_tdse': time_step_tdse,
            'maximum_propagation_time': maximum_propagation_time,
            'hopping_algorithm': 'FSSH',
            'decoherence_model': 'SDM',
            'rescale_velocity_direction': 'nacs',
            'prevent_back_hop': False,
            'nstates': nstates,
            'initial_state': initial_state,
            }

# Run trajectories
dyns = ml.simulations.run_in_parallel(molecular_database=init_cond_db,
                                      task=ml.namd.surface_hopping_md,
                                      task_kwargs=namd_kwargs,
                                      create_and_keep_temp_directories=False)
trajs = [d.molecular_trajectory for d in dyns]

itraj=0
for traj in trajs:
    itraj+=1
    traj.dump(filename=f"traj{itraj}.h5",format='h5md')


