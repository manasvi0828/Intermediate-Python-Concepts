import numpy as np
a= np.array([1,2,3,4,5,6])
b= np.array([7,8,9,4,5,7])
print(np.intersect1d(a,b))
print(np.setdiff1d(a,b))
print(np.where(a==b))