import numpy as np
a= np.arange(10).reshape(2,-1)
b= np.repeat(1, 10).reshape(2,-1) #configuringto -1 automatically sets the number of columns
c=np.tile(a,3)
print(c)
print(np.vstack([a,b]))
print(np.hstack([a,b]))