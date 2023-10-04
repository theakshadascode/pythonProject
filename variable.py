
a=10 #Global variable
print(id(a))
def var():

     a=5  #local variable
     x=globals()['a']
     print(id(x))
     globals()['a']=15

     print("In function",a)
var()



print("outside",a)



