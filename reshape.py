import numpy as np
list=[1,2,3,4,5]
list2=[5,6,7,8,9]
list3=[4,5,6,7,8]
arr=np.array([list,list2,list3]) #whole data in array form is very fast
print(arr)
print(arr.shape)
print(arr.reshape(5,3)) #change row and column orientation