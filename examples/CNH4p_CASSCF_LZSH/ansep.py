import mlatom as ml
import os

time_step = 0.5
maximum_propagation_time = 100
nstates = 3
ntrajs = 63

db = ml.data.molecular_database.load('data/ic.json', format='json')

trajs = []
for i in range(ntrajs):
    if not os.path.isdir(f'TRAJ{i+1}'):
        os.system(f'mkdir TRAJ{i+1}')
        os.system(f'mkdir TRAJ{i+1}/data')
        os.system(f'cp -r data/sp_input_casscf/ TRAJ{i+1}/data/')
        os.system(f'cp run.py TRAJ{i+1}')
        os.system(f'cp subme TRAJ{i+1}')
        ic = db[i:i+1]
        ic.dump(f'TRAJ{i+1}/data/ic.json', format='json')
    os.system(f'mv TRAJ{i+1}/*-*-*-*-*.h5 TRAJ{i+1}/traj_fin.h5')
    if os.path.isfile(f'TRAJ{i+1}/traj_fin.h5'):
        traj = ml.data.molecular_trajectory()
        traj.load(f'TRAJ{i+1}/traj_fin.h5', format='h5md')
        trajs.append(traj)

if len(trajs) > 0:
    ml.namd.analyze_trajs(trajectories=trajs, maximum_propagation_time=maximum_propagation_time)
    ml.namd.plot_population(trajectories=trajs, time_step=time_step, max_propagation_time=maximum_propagation_time, nstates=nstates, filename=f'pop.png', pop_filename='pop.txt')
