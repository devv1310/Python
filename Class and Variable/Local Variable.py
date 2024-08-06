#  local variable kisi v fun ki andar agar diclear kra jana wala variable local variable hota hai
# note :- we cant access local variable outside of the define block
class student:
    def display(self,name,age):
        x=10 # Local Variable
        print('Name=',name)
        print('Age=',age)
        print('X=',x)
obj=student()
obj.display('dev',23)
# print(obj.x)