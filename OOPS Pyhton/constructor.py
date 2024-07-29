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
class student:
    x=10
    y=20
    def __init__(self):
        print(id(self))
    @staticmethod
    def display():
        print("display fun")
obj=student()
print(id(obj))
obj1=student()
print(id(obj1))