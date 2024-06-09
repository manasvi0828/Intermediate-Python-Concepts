#random distribution has random values between 0 and 1
import numpy as np
list=[1,2,3,4,5]
arr=np.array(list)
arr2= np.random.rand(3,3)
print(arr2)

arr3= np.random.randn(4,4)
print(arr2)

arr4= np.random.randint(2,3)
print(arr4)