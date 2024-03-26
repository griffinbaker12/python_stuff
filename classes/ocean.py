class Ocean:
    def __init__(self, sea_creature_name, sea_creature_age):
        self.name = sea_creature_name
        self.age = sea_creature_age

    # without implementing str or repr dunder methods, both return a string with the class and the object id in hex

    def __str__(self) -> str:
        return f"The creatures name is {self.name} and its age is {self.age}."

    def __repr__(self) -> str:
        return f"Ocean('{self.name}', {self.age})"

    # doesn't really make sense, but
    # generator function that returns an iterator
    # resulting iterator yields the name and age on demand
    # the call to list() iterates over the attributes
    # we don't call .__iter__() directly, Py will call automatically when we use instance on an iteration
    def __iter__(self):
        yield from (self.name, self.age)

    @classmethod
    def from_seq(cls, seq):
        return cls(*seq)

    def iter_over_seq(self, a, b, c):
        print(a, b, c)

    @staticmethod
    def show_message(name):
        return f"Hey {name}, this is a static method"


c = Ocean("Jellyfish", 5)
print(str(c))
print(repr(c))
