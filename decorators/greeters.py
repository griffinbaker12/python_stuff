# globally defined functions are accessible from any part of the program and remain availabe for the entire lifecycle of the program or web page


def say_hello(name):
    return f"Hello {name}"


def be_awesome(name):
    return f"Hey {name}, you are the awesomest!"


def greet_someone(name, greeter_func):
    return greeter_func(name)
