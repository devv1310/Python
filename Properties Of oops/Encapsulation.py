# Access Modifier :-
                # Public
                # protected( _ )
                # private( _ _ )
# Protected.....................................................
# class p1:
#     _name = 'Devanshu'
#     def display(self):
#         print(p1._name)
    
# class c1(p1):
#     name= p1._name
#     def show(self):
#         print('Name=',c1.name)
# obj=c1()
# obj.show()
# print(obj._name)

# Private........................................................
class p1:
    __name = 'Devanshu'
    def display(self):
        print(p1.__name)
obj=p1()
obj.display()
