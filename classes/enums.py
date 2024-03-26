from enum import Enum


# we define weekday by subclassing Enum
class WeekDay(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

    # make use of generator to yield tuple of the enum member names and corresponding values
    #  When you call WeekDay.iterate(), it returns a generator object that yields these name-value pairs one at a time. You can loop over this generator as you would with any iterable, allowing you to destructure the name and value directly into two variables (n, v in your loop).
    @staticmethod
    def iterate():
        for member in WeekDay:
            yield member.name, member.value


for day in WeekDay:
    print(day.name, "->", day.value)

for n, v in WeekDay.iterate():
    print(n, "->", v)

w = WeekDay.FRIDAY
print(w)


def print_name(self):
    return f"Current day: {self.name}"


# dynamic extension
WeekDay.__str__ = print_name
print(w)
