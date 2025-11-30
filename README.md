# FSSH-in-MLatom

Preprint:
- Jakub Martinka, Mikołaj Martyka, Jiří Pittner* and Pavlo O. Dral*. Flexible Framework for Surface Hopping: From Hybrid Schemes for Machine Learning to Benchmarkable Nonadiabatic Dynamics. 

Preprint on: 

- This repository contains a Jupyter notebook with Supporting Information (`SI.ipynb`), `examples/` containing input files and scripts to run surface hopping simulations and `res/` with resulting figures.

Code and data
-------------

Run `ansep.py` to create TRAJs or create `pop.txt`, run surface hopping by `run.py`, `data/` contains initial conditions and QC inputs and/or ML models.

```
Structure:
examples/
│
├── CNH4p_CASSCF_FSSH
├── CNH4p_CASSCF_LZSH
├── CNH4p_CASSCF_TDBA
├── CNH4p_MRCI_FSSH
│
├── FERRO_WIRE_FSSH
├── FERRO_WIRE_LZSH
├── FERRO_WIRE_TDBA
├── FERRO_WIRE_TDBA_0.5eV
│
├── FULVENE_FSSH
├── FULVENE_FSSH_MLQM
├── FULVENE_FSSH_MLQM_0.5eV
├── FULVENE_LZSH
├── FULVENE_TDBA
├── FULVENE_TDBA_0.5eV
└── FULVENE_TDBA_dgrad - rescale velocity $g_{ij}$
res/
```

Trajectories in H5MD format (exceeding 55 GB in total) can be provided upon request due to their size.

