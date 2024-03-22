def decorator(func):
    def wrapper():
        print("before")
        func()
        print("after")

    return wrapper


# def say_whee():
#     print("whee")


# say_whee = decorator(say_whee)


@decorator
def say_whee():
    print("Whee!")
