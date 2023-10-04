def person(name,age):
    print(name)
    print(age)

def person1(name,age=18):
    print(name)
    print(age)

def sum(a,*b):
    c=a
    for i in b:
        c=c+i
    print(c)


def sum1(*b):
    c=0
    for i in b:
        c=c+i
    print(c)


def persondata(name,**data):
    print(name)
    print(data)

    for i,j in data.items():
        print(i,j)


#person(age=29,name='Akshada')  #keyword
#person1('Akshada')              #default
#sum(1,2,34,4,5)   #variable length
#sum1(1,2,34,5,5)   #position
persondata('akshada',age=18,city='pune',mobile=9370160) #keyworded variable length

