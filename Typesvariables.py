class Car:

    wheel=20 #class variable
    def __init__(self):
       self.mil=10      #Instance variable
       self.com="BMW"



c1=Car()
c2=Car()

c1.mil=20
c1.com="xyz"
Car.wheel=2

print(c1.mil,c1.com,c1.wheel)
print(c2.mil,c2.com,c2.wheel)
