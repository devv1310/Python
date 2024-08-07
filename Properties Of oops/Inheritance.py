# Inheritance :-
            # 1. Single Level Inheritance       | father -> Son
            # 2. Multi level Inheritance        | grandfather -> father -> Son
            # 3. Multipe Inheritance            | father -> Son <- Mother

#  1. Single level Inheritance.......................................................
# class p:
#     city = 'bhopal'
#     def display(self):
#         print("this is from display")
# class c(p):
#     def show(self):
#         print("from show")
#         print("City=",p.city)
# obj=c()
# obj.show()
# obj.display()
# print(obj.city)


# 2. Multi level inheritance...........................................
# class p:
#     city = 'bhopal'
#     def display(self):
#         print("this is from display")
# class c(p):
#     def show(self):
#         print("from show")
#         print("City=",p.city)
# class c1(c):
#     city1 = p.city
#     def show1(self):
#         self.display()
#         self.show()  
# obj=c1()
# print(obj.city1)
# obj.show1()
# obj.show()
# obj.display()
# print(obj.city)

# 3. Multiple Inheritance...........................................................................
class P1:
    def display(self):
        print("P1 of Display")
class P2:
    def display(self):
        print("P2 of Display")
class C(P1,P2):
    def show(self):
        self.display()
        # self.display()
obj=C()
obj.show()


