import statistics
from numpy import minimum
import pandas as pd
from torch import maximum
  
sr = pd.Series([10, 50, 80, 70, 49, 23,11, 4])

maximum=sr.max()
minimum=sr.min()
mean = sr.mean()
#median = sr.median()
#mode = sr.mode()
#range1 = sr.max() - sr.min(); 
stdeviation = sr.std(axis=0,skipna=True)

print(minimum)
print(maximum)

print(mean)
#print(median)

#print(mode)

print(stdeviation)
print("Variance of sample set is % s"%(statistics.variance(sr)))
