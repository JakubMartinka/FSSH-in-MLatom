import os
import mlatom as ml

root_dir = os.getcwd()

# Load initial conditions
init_cond_db = ml.data.molecular_database.load(f'{root_dir}/data/ic.json', format="json")

# Set singlepoint calculation
col = ml.models.methods(program='columbus', command_line_arguments=['-m', '1700'], directory_with_input_files=f'data/sp_input_casscf', save_files_in_current_directory=True, look_for_mocoef=True)

# Set NAMD arguments
maximum_propagation_time = 100
time_step = 0.5
time_step_tdse = None
nstates = 3
initial_state = 2

namd_kwargs = {
            'model': col,
            'model_predict_kwargs': {'level_of_theory': 'CASSCF', 'calculate_energy_gradients': [True]*nstates},
            'time_step': time_step,
            'maximum_propagation_time': maximum_propagation_time,
            'hopping_algorithm': 'LZSH',
            'prevent_back_hop': False,
            'nstates': nstates,
            'initial_state': initial_state,
            'dump_trajectory_interval': 5,
            'reduce_memory_usage': True
            }

# Run trajectories
dyns = ml.simulations.run_in_parallel(molecular_database=init_cond_db,
                                      task=ml.namd.surface_hopping_md,
                                      task_kwargs=namd_kwargs,
                                      create_and_keep_temp_directories=True)
trajs = [d.molecular_trajectory for d in dyns]

itraj=0
for traj in trajs:
    itraj+=1
    traj.dump(filename=f"traj{itraj}.h5",format='h5md')

