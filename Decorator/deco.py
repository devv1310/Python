def decorator(fun):
    def wrapper():
        print("start work")
        fun()
        print("stop work")
    return wrapper
@decorator
def original_fun():
    print("this is original funtions")
original_fun()