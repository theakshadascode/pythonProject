class Pycharam:
    def execute(self):
        print("compile")
        print("execute")
class myeditor:
    def execute(self):
        print("spell check")

class Laptop:

    def code(self,ide):  #ide type is not fixed we can add another class as well

        ide.execute()


#ide=Pycharam()
ide=myeditor()

lap1=Laptop()
lap1.code(ide)
