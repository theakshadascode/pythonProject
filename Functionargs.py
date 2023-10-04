def update(x):
    x=8
    print(x)

#update(10)

def update1(x):
    print(id(x))
    x=8
    print(id(x))
    print("x",x)

a=10
print(id(a))
update1(a)
print("a",a)

def update2(lst):
    print(id(lst))
    lst[1]=25
    print(id(lst))
    print("lstD",lst)

lst=[10,20,20]
print(id(lst))
update2(lst)
print("lstC",lst)
