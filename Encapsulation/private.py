class student:
    school = "LSSMS"
    def __init__(self,name,age):
        self.__name = name
        self.__age = age
    def deatils(self):
        print("Name=",self.__name)
        print("Age=",self.__age)
        print("School=",student.school)
class Marks(student):
    def marks(self,hindi,maths):
        self.hindi = hindi
        self.maths = maths
    def complete_details(self):
        print("Name=",self.__name)
        print("Age=",self.__age)
        print("School=",student.school)
        print("Hindi=",self.hindi)
        print("Maths=",self.maths)
obj = Marks("Dev",65)
obj.__name ="Prashu"
obj.marks(84,78)
student.school = "Little Star Sheilesh Memorial Shool"
obj.complete_details()
