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

# class Student:
#     x=10
#     y=20
#     def display(self):
#         print("hello")
#     @staticmethod
#     def show(): 
#         print("welcome")
# obj=Student()
# obj.display()
# obj.show()
# print(__dict__(Student)) 

# Class Methods :-
class Book:
    price=1000
    def details(self,author_name,author_city):
        print('Name=',author_name)
        print('City=',author_city)
        print('Price=',Book.price)
    @classmethod
    def update_price(cls,update_price):
        cls.price = update_price
obj=Book()
obj.details('Dev','Sagar')
obj.update_price(15000)
obj.details('Dev','Sagar')


