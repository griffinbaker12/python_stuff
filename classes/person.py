class Person:
    def __init__(self, name):
        self.name = name

    # these getter and setter methods get called automatically when you access or update the attribute's values

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value.upper()
