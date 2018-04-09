
from netCDF4 import Dataset
path = "C:/Users/M543015/Desktop/GitHub/coralbleaching/"
#file = "sst.mon.mean.nc"
file = "sst.mnmean.nc"
infile = Dataset(path+file,'r')
import numpy as np
sst = np.array(infile.variables['sst'][:])
#lat goes from -89.5 to 89.5
#lon goes from 0.5 to 359.5
#time is days since 1891-1-1 (0-46294, 1522 obs)
#that's wrong, I think...days since 1800, and the lowest is 54?
#sst is from -5 to 40 (1522, 180, 360)
#1e20 is missing
#18° S, 148° E

series = infile.variables["sst"]
time = infile.variables["time"][:]
time = [item[0][0] for item in time.tolist()]

series = infile.variables["sst"][:,53:54, 74:75]
series = [item[0][0] for item in series.tolist()]
series = [str(s)+"\n" for s in series]
#pairs = [(time[i], series[i]) for i in range(len(series))]
outfile = "series.txt"
with open(path+outfile,'w') as f:
	f.writelines(series)
