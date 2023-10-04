from array import * #import everything

arr=array('i',[])  #blank array

n=int(input("Enter length of array"))

for i in range(n):
    x=int(input("Enter next values"))
    arr.append(x)

print(arr)


val=int(input("Enter value which you want to search in array"))

k=0        #without fun
for j in arr:
    if j==val:
        print(k)
        break
    k+=1

print(arr.index(val))  #with fun
