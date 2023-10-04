from numpy import *

arr1=array([

[1,2,3,6,7,8],[4,5,6,9,8,45]

])

arr2=arr1.flatten() #return one array using two dimensional array
arr3=arr1.reshape(3,4) #create new array by passing rows and columns
arr4=arr1.reshape(2,2,3) #create new array by passing rows and columns
m=matrix(arr1)
m1=matrix('1,2,3;4,5,6;7,8,9')
m2=matrix('1,2,8;4,9,6;7,8,9')

m3=m1+m2
m4=m1-m2
m5=m1*m2
#print(arr1.dtype) #return data type
#print(arr1.size) #return total no of element
#print(arr1.ndim) #retun no of dimension
#print(arr1.shape) #return no of rows & column

#print(arr2)
#print(arr3)
#print(arr4)
#print(m)
#print(m1)
#print(diagonal(m1))
#print(m1.min())
#print(m1.max())

print(m1)
print(m2)
#print(m3)
#print(m4)
print(m5)
