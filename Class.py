class Computer:
    def __init__(self,cpu,ram):
        self.cpu=cpu
        self.ram=ram
        print("in init methods")

    def config(self):
        print("config is",self.cpu,self.ram)

comp1=Computer('i5',16)
comp2=Computer('ryzen ',15)

Computer.config(comp1)  #1st way to call
Computer.config(comp2)  #1st way to call


comp1.config() #2nd way to call
comp2.config()#2nd way to call

