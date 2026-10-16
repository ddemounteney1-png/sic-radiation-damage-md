import atomman as am
import os

def sort_key(name):
   if name.endswith(".dump"):
      # Split on dots: SiC.18.dump → ["SiC", "18", "dump"]
      return int(name.split('.')[1])
   return 0

cwd = os.getcwd() 
DumpFilesFolder = cwd
volume= []

for file in sorted(os.listdir(DumpFilesFolder), key=sort_key):
    filename = os.fsdecode(file)
    if filename.endswith(".dump"):
        # print("Filename:", filename)
        SiC = filename
        system = am.load('atom_dump', SiC, symbols=['Si','C'])
        cell = system.box
        CellVolume = cell.volume
        volume.append(CellVolume)
        # print("CellVolume:", CellVolume)
        print(filename, CellVolume)
        continue
    else:
        continue
LastVolume = volume[-1]
FirstVolume = volume[0] # Was [1]

VolumeChange = LastVolume - FirstVolume
Percentage = (VolumeChange / FirstVolume)*100
print("FirstVolume:", FirstVolume)
print("LastVolume:", LastVolume)
print("Volume change:", VolumeChange)
print("Percentage:", Percentage)
