from lammps import PyLammps
import numpy as np
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

for n in range(1,11):
    #generate random angles for PKA
    if rank == 0:
        np.random.seed()
        #this is a really bad way to do this btw
        sintheta = np.random.rand()
        sinphi = np.random.rand()
        cosphi = np.sqrt(1-sinphi**2)

        with open("casc_template.lammps", "r") as file:
            template = file.read()

            # the displacement energy seems to be pretty high in SiC...

            #Write the cascade input script
            script = template.format(v_x=400.0*sintheta*cosphi, v_y=400.0*sintheta*sinphi, v_z=400.0*cosphi, m=n-1,n=n,PKA_id = np.random.randint(1,64000))
        with open(f"cascade_{n}.lammps", "w") as file:
            file.write(script)

    comm.Barrier()  # Ensure all processes wait until rank 0 has written the files
    lmp = PyLammps()
    lmp.include(f"cascade_{n}.lammps")
lmp.close()
#MPI.Finalize()
