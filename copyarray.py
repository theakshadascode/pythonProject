from numpy import *

arr1=array([1,3,4,5,6])

#arr2=arr1.view()#return shallow copy
arr2=arr1.copy()# return deep copy

arr1[1]=9

print(arr1)
print(arr2)

print(id(arr1))
print(id(arr2))

print(sqrt(arr1))
print(max(arr1))
print(min(arr1))
