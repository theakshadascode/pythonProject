from array import *

value=array('i',[1,-2,3,4,5,9,10])
value.reverse() #reverse array
print(value)
print(value.buffer_info()) #give you address and size of array
print(value.typecode)  #return data type of array

for i in range(len(value)):
    print(value[i])

for e in value:
    print(e)

newarr=array(value.typecode,(a for a in value)) #creating new array from existing array

for j in newarr:
    print(j)

newarrsqr=array(value.typecode,(a*a for a in value)) #creating new array from existing array  with sqaur

for k in newarrsqr:
    print(k)
