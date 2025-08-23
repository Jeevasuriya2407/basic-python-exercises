def my_decorator(func):
    def wrapper():
        print("prints before the execution of a function")
        func()
        print("prints after the execution of a function")
    return wrapper

@my_decorator
def hello():
    print("hello world")
hello()
