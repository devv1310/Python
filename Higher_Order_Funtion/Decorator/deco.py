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
