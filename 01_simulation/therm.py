from lammps import PyLammps
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

lmp = PyLammps()
lmp.include("therm_in.lammps")
lmp.close()
MPI.Finalize()
