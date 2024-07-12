# def add(x,y,z):
#     # print(x+y+z)
#     return x+y+z
# p=int(input("enter no"))
# q=int(input("enter no"))
# r=int(input("enter no"))
# x=add(p,q,r)
# print(x)
# # x=x+100
# # print(x)


def add(x,y):
    return x+y,x-y,x*y,x/y,x%y
p=int(input("enter no"))
q=int(input("enter no"))
a,b,c,d,e=add(p,q)
print(a,b,c,d,e) 