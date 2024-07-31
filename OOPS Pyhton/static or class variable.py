# static/class variable outside of method and inside the class declear kr skta hai
# static/class variable ki value change nai hoti hai
class Student:
    school="LSSMS" # 1st Static variable outside methodes
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
        Student.centercode=110 # 2st Static variable inside Constractor
    def display(self):
        Student.grade='10th' # 3st Static variable inside the instance methods
        print('Name=',self.name)
        print('Roll no=',self.roll)
        print('School=',Student.school)
        print('Center=',Student.centercode)
        print('Grade=',Student.grade)
        
obj=Student('Devanshu',113)
Student.city='Sagar'# 4th Static variable
obj.display()
print("school",Student.school)
print('City=',Student.city)
