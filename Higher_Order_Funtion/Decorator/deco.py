# def decorator(fun):
#     def wrapper():
#         print("start work")
#         fun()
#         print("stop work")
#     return wrapper
# @decorator
# def original_fun():
#     print("this is original funtions")
# original_fun()
def outer_fun(fun):
    def inner_fun(x,y):
        x=x+5
        y=y+5
        print("main function called")
        return fun(x,y)
    return inner_fun
@outer_fun
def main_fun(x,y):
    return x+y
a=main_fun(5,5)
print(a)
basics of decoratores:

 # nested_function....
def fun1(x):
    def fun2(y):
        return x+y
    return fun2
var1 = fun1(5)
var2 = var1(5)
print(var2)

# function pass as a argument....
def add(x,y):
    return x+y

def cal(func,x,y):
    return func(x,y)

var1 = cal(add,4,5)
print(var1)

# function that returns a function.......
def fun1(num):
    def fun2(x):
        x=num+x
        return x
    return fun2

var1 = fun1(5)
var2 = var1(10)

print(var2)
