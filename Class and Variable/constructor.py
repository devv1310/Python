# class student:
#     x=10
#     y=20
#     def display():
#         print("display fun")
# obj=student
# obj.display()
# print(obj.x)

# note point  :- [constructor call krna ki liya () parathises lagna pdta ha]
# [self can hold rference of current object of current class]
# class student:
#     x=10
#     y=20
#     def __init__(self):
#         print("from constructor")
#     @staticmethod
#     def display():
#         print("display fun")
# obj=student()
# print(obj.x)
# obj.display()
# class student:
#     x=10
#     y=20
#     def __init__(self):
#         print(id(self))
#     @staticmethod
#     def display():
#         print("display fun")
# obj=student()
# print(id(obj))
# obj1=student()
# print(id(obj1))

# const. kitna v ho wo last walo ko hi read krga
# n number of argument pass kr skta hai const. me isme koi limit nahi hoti hai
class student:
    def __init__(self,x):
        print("")
    def __init__(self,x,y):
        print("")
    def __init__(self,x,y,z):
        print("")
obj=student(2,4,3)
   