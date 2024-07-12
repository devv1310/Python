# function(function)
#             | .............function as a argument
#   |.......................higher order function
# 1. map()----------------no. of input object == no. of output object 10=10
# 2.Filter()----------------no. of input object >= no. of output object 10>5
# 3.reduce()---------------- no. of output object == 1 
#WAP to find any collection of Square
# 1. map()...................
# my_list1=[1,2,3,4,5,]
# my_list2=[5,4,3,2,1]
# def square(n):
#     return n**2
# new_list=list(map(square,my_list))
# print(new_list)
# def add(x,y):
#     return x+y
# new_list=list(map(add,my_list1,my_list2))
# print(new_list)
# def divide(x,y):
#     return x/y
# new_list=list(map(divide,my_list1,my_list2))
# print(new_list)
# x=lambda a,b : a+b
# print(list(map(x,[1,2,3,4],[3,4,5,6])))
