import os
import mlatom as ml
import numpy as np

root_dir = os.getcwd()

# Load initial conditions
init_cond_db = ml.data.molecular_database.load(f'{root_dir}/data/ic.json', format="json")

# Set singlepoint calculation
msani = ml.models.msani(model_file=f'{root_dir}/data/msani.pt')

# Set NAMD arguments
maximum_propagation_time = 60
time_step = 0.1
nstates = 2
initial_state = 1

namd_kwargs = {
            'model': msani,
            'time_step': time_step,
            'maximum_propagation_time': maximum_propagation_time,
            'hopping_algorithm': 'LZSH',
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

