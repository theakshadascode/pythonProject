class Student:

    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        self.lap=self.Laptop()

    def show(self):
        print(self.name,self.marks)
        self.lap.show()

    class Laptop:  #Inner class

        def __init__(self):
            self.brand='HP'
            self.model='i5'

        def show(self):
            print(self.brand,self.model)

s1=Student('Akshada',89)
s2=Student('Jenny',88)

s1.show()

lap1=s1.lap
print(s1.lap)

