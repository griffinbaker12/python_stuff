import json


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed


# def serialize_object(obj):
#     """
#     Serialize an object to a dictionary, including its attributes using introspection.
#     """
#     serialized_obj = {}
#     # Using introspection to iterate over all attributes of an object
#     attributes = dir(obj)
#     print(attributes)
#     for attribute in attributes:
#         if attribute.startswith("__"):
#             continue
#         value = getattr(obj, attribute)
#         print(attribute, value)
#         serialized_obj[attribute] = value
#     return serialized_obj


def serialize_object(obj):
    # Using introspection to dynamically access object attributes
    return {
        attr: getattr(obj, attr)
        for attr in dir(obj)
        if not attr.startswith("__") and not callable(getattr(obj, attr))
    }


person = Person("John Doe", 30)
dog = Dog("Roofus", "Golden Retriever")

serialized_person = serialize_object(person)
serialized_dog = serialize_object(dog)

json_person = json.dumps(serialized_person)
json_dog = json.dumps(serialized_dog)

print(json_person)  # Output: {"name": "John Doe", "age": 30}
print(json_dog)  # Output: {"name": "Fido", "breed": "Labrador"}
