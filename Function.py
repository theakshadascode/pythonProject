
def greet():
    print("Hello")
    print("GM")

def add(x,y):
    c=x+y
    print(c)

def add1(x,y):
    c=x+y
    return c

def add_sub(x,y):
    c=x+y
    d=x-y
    return c,d

greet()
add(4,5)
result=add1(10,20)
print(result)

result1,result2=add_sub(20,10)
print(result1,result2)
