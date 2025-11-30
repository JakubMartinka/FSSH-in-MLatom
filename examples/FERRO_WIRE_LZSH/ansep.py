import mlatom as ml
import os

time_step = 0.5
maximum_propagation_time = 200
nstates = 4

db = ml.data.molecular_database.load('data/init_cond_db.json', format='json')

ntrajs = len(db)

with open('data/state_init.dat', 'r') as fr:
    lines = fr.readlines()
IS = [int(line) for line in lines]

trajs = []
for i in range(ntrajs):
    if not os.path.isdir(f'TRAJ{i+1}'):
        os.system(f'mkdir TRAJ{i+1}')
        os.system(f'cp run.py TRAJ{i+1}')
        os.system(f'cp subme TRAJ{i+1}')
        os.system(f'cp data/mndokw TRAJ{i+1}')
        os.system(f'sed -i "s/initial_state = IS/initial_state = {IS[i]-1}/g" TRAJ{i+1}/run.py')
        ic = db[i:i+1]
        ic.dump(f'TRAJ{i+1}/ic.json', format='json')
    if os.path.isfile(f'TRAJ{i+1}/traj1.h5'):
        traj = ml.data.molecular_trajectory()
        traj.load(f'TRAJ{i+1}/traj1.h5', format='h5md')
        trajs.append(traj)

if len(trajs) > 0:
    ml.namd.analyze_trajs(trajectories=trajs, maximum_propagation_time=maximum_propagation_time)
    ml.namd.plot_population(trajectories=trajs, time_step=time_step, max_propagation_time=maximum_propagation_time, nstates=nstates, filename=f'pop.png', pop_filename='pop.txt')


