from lammps import PyLammps
import numpy as np
from mpi4py import MPI
import random
import math

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
    
for n in range(1, 96): # Defines number of cascades to run
    if rank == 0:
        # Generate random angles for PKA
        np.random.seed()
        theta = np.random.uniform(0, np.pi)
        phi = np.random.uniform(0, 2*np.pi)
        
        # Read template and configure with the random angles and random PKA velocity
        with open("casc_template.lammps", "r") as file:
            template = file.read()
            script = template.format(e=2000, theta=theta, phi=phi, m=n-1, n=n, PKA_id = np.random.randint(1,537600))
        
        # Write the cascade input script
        with open(f"cascade_{n}.lammps", "w") as file:
            file.write(script)
    
    comm.Barrier() # Ensure all processes wait until rank 0 has written the files
    lmp = PyLammps()
    lmp.include(f"cascade_{n}.lammps")
lmp.close()
#MPI.Finalize()
