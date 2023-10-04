class Student:
    school="VP"

    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3

    def avg(self):
        return (self.m1+self.m2+self.m3)/3
    @classmethod
    def getschool(clg):
        return clg.school
    @staticmethod
    def info():
        print("This the static method")

s1=Student(21,22,23)
s2=Student(31,32,33)

print(s1.avg())
print(Student.getschool())

Student.info()
