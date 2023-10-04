from functools import reduce

lst=[2,3,45,5,6,7,8,89,9,19]

evens =list(filter(lambda n:n%2==0,lst)) #Filter
doubles =list(map(lambda n:n*2,evens)) #map
sum=reduce(lambda a,b:a+b,doubles) #reduce


print(evens)
print(doubles)
print(sum)
