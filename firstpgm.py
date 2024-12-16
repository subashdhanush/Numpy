import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr)

print(type(arr))

list2=["john elder",41,arr,True]
print(list2)

# numpy==>Numeric Python
# ndarry = n-dimensional array
np1=np.array([0,1,2,3,4,5,6,7,8,9])
print(np1)
print(np1.shape)

#Range
np2=np.arange(10)
print(np2)

#Step
np3=np.arange(0,10,2)
print(np3)

#Zeros
np4=np.zeros(10)
print(np4)


#multidimensional arrat
np5=np.zeros((2,10))
print(np5)

#full
np6=np.full((10),6)
print(np6)


#multidimensional 
np7=np.full((2,10),6)
print(np7)

#convert python lists to np
my_list=[1,2,3,4,5]
np8=np.array(my_list)
print(np8)