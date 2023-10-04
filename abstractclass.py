from abc import ABC,abstractmethod


class Stud(ABC):  #ABC we need use to make class abstract
    @abstractmethod  #shown abstract methods
    def show(self):
        pass

class Laptop(Stud):
    def show(self):
        print("its running")

#s1=Stud()
l1=Laptop()
l1.show()
