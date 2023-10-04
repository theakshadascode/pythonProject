class A:
    def show(self):
        print("Show in A")

class B(A):
   def show(self):
        print("Show in B")

a1=B()
a1.show()
