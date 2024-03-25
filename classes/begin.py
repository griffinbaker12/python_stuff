# class as piece of code that specifies data and behavior that represent and model a particular type of object

# attributes -> variables defined inside a class with the purpose of storing all the required data for the class to work
# method -> different behaviors the objects will show; typically operate on or with the attributes of the underlying instance or class
# together, referred to as members of a class or object


# without mangling
class BaseClass:
    def __init__(self):
        # mangled
        self.__private_attr = "base"
        # will get overwritten
        self.private_attr = "base"


class SubClass(BaseClass):
    def __init__(self):
        super().__init__()
        self.private_attr = "sub"


# Creating an instance of SubClass
base = BaseClass()
sub_instance = SubClass()
print(base._BaseClass__private_attr)  # type: ignore
print(sub_instance.private_attr)  # Output: Base class attribute


# # with mangling
# class BaseClass:
#     def __init__(self):
#         self.__private_attr = "Base class attribute"


# class SubClass(BaseClass):
#     def __init__(self):
#         super().__init__()
#         self.__private_attr = "Subclass attribute"


# # Creating an instance of SubClass
# sub_instance = SubClass()
# print(sub_instance._BaseClass__private_attr)  # Output: Base class attribute
# print(sub_instance._SubClass__private_attr)  # Output: Subclass attribute


class C1:
    def __init__(self) -> None:
        self.x = "hey"


class C2(C1):
    def __init__(self) -> None:
        super().__init__()


c2 = C2()
print(c2.x)


class ObjectCounter:
    count = 0

    def __init__(self) -> None:
        # ObjectCounter.count += 1
        print(ObjectCounter == type(self))
        type(self).count += 1


ObjectCounter()
ObjectCounter()
ObjectCounter()
x = ObjectCounter()
# access can be done by the class itself or one of its instances
print(ObjectCounter.count, x.count)
x.count = 0
print(ObjectCounter.count, x.count)


class Record:
    """
    Hold a record of data
    """


john = {
    "name": "John Doe",
    "position": "Python Developer",
    "department": "Engineering",
    "salary": 80000,
    "hire_date": "2020-01-01",
    "is_manager": False,
}

john_record = Record()

for f, v in john.items():
    setattr(john_record, f, v)

print(john_record.__dict__)
