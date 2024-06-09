import numpy as np
arr= np.arange(20)
out=arr.copy()
out[out%2 != 0] = -1
print(out)
