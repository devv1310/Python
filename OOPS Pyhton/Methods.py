# methods:-
    # 1. instance Method
    # 2. class Method
    # 3. static Method /static methods class methods or class variable se kuch leyna deyna nahi rkhta / @staticmethod use krke call krta h
    
#STATIC METHOD:-  
# class Student:
#     def display(self):
#         print("hello")
#     def show(): /static methods
#         print("welcome")
# obj=Student()
# obj.display()
# obj.show()

# class Student:
#     def display(self):
#         print("hello")
#     @staticmethod
#     def show(): /static method call
#         print("welcome")
# obj=Student()
# obj.display()
# obj.show()

# class Student:
#     def display():
#         print("hello")
#     def show(): 
#         print("welcome")
# print(dir(Student)) #  kis v class ki method ye detial jana ki leya DIR use krta hai 

class Student:
    x=10
    y=20
    def display():
        print("hello")
    def show(): 
        print("welcome")
print(__dict__(Student)) 
