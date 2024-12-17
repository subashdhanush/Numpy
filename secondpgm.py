import numpy as np

np1=np.array([1,2,3,4,5,6,7,8,9])

#slicing the array
print(np1[1:5])

#return from something till the end of the array
print(np1[3:])

#return Negative Slices
#7,8
print(np1[-3:-1])

#steps
print(np1[1:5])
print(np1[1:5:2])

#steps on the entire array
print(np1[::2])
print(np1[::3])


#slice a 2-d array
np2=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(np2[1,2])

#slice a 2-d array
print(np2[0:1,1:3])

#slice from both rows 2,3 and 7,8
print(np2[0:2,1:3])