class A:

    def __init__(self):
        print("init is in A")
    def feature1(self):
        print("Feature1 working")

    def feature2(self):
        print("Feature2 working")
class B(A):
        def __init__(self):
            super().__init__()  ##call for super class constructor
            print("init is in B")

        def feature3(self):
            print("Feature3 working")

        def feature4(self):
            print("Feature4 working")


#a=A()
b=B()

#a.feature1()
#a.feature2()

b.feature1()
b.feature2()
b.feature3()
b.feature4()
