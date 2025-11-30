import os
import mlatom as ml

root_dir = os.getcwd()

# Load initial conditions
init_cond_db = ml.data.molecular_database.load(f'{root_dir}/ic.json', format="json")

# Set singlepoint calculation
aiqm1 = ml.models.methods(method='ODM2', read_keywords_from_file='mndokw')

# Set NAMD arguments
maximum_propagation_time = 200
time_step = 0.5
nstates = 4
initial_state = IS

namd_kwargs = {
            'model': aiqm1,
            'time_step': time_step,
            'maximum_propagation_time': maximum_propagation_time,
            'hopping_algorithm': 'FSSH',
            'decoherence_model': 'SDM',
            'rescale_velocity_direction': 'nacv',
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

