import numpy as np
a = np.array([0,8,4,8,5,4,9])
print(np.sum(a==8))
unique, counts = np.unique(a,return_counts=True)
print(unique,counts)