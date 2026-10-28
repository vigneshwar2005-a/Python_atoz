# PIP 

''' pip is a package manager for python packages or modules numpy is a python 
library used for working with arrays

.numpy stands for numerical python

>> why use numpy:

in python we have list that serve the purpose of arrays , but they are slow to process
numpy aims to provide and array object that is up to 50 times fister then the list

>> the array object in numpy is called ndarray  it provide a lot of functions
we can create a nd array object by using the array()
 '''


from hashlib import new

import numpy as np
arr = np.array([1,2,3,4,5,6,7,8,9])
for i in arr:
    print(i)
print(type(arr))

arr1 = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(arr1)
print(arr.ndim)
print(arr1.ndim)

# Access array elements

print(arr[1])  # Access the first element of arr
print(arr1[0, 0])  # Access the first element of the first row of arr1  

# Array Slicing

'''Start:end or start:stop:step'''

print(arr[1:5])  # Slice elements from index 1 to 4
print(arr[1:6:2])  # Slice elements from index 1 to 5 with a step of 2
print(arr[-1])
print(arr[1])
print(arr[::-1])
print(arr1[0:2, 1:3])  # Slice elements from rows 0 to 1 and columns 1 to 2

x=np.sort([9,4,6,2,5,1])
print(x)

arr3=np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr3.ndim)
print(arr3[1][1][0])

# Shape of an array 

arr4 = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(arr4.shape)

# Reshaping array

arr5 = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
newarr=arr5.reshape(4,3)
print(newarr)

# iterating arrays using nditer()

for x in np.nditer(arr5):
    print(x)

# Enumerate iteration using ndenumerator

arr5 = np.array([20,30,40])
for idx, x in np.ndenumerate(arr4):
    print(idx,x)

# Joining arrays

arr6 = np.array([[1,2],[3,4]])
arr7= np.array([[5,6],[7,8]])
arr8=np.concatenate((arr6,arr7),axis=1)
print(arr8)

# Array Split

arr9 = np.array([1,2,3,4,5,6])
new_array=np.array_split(arr9,3)
print(new_array)

# Searching array using where method

arr10 = np.array([1,2,3,4,5,4,4])
x=np.where(arr10==4)
print(x)

arr11 = np.array([1,2,3,4,5,6,7,8])
y = np.where(arr11%2==0)
print(y)