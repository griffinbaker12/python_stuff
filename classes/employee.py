from datetime import datetime


class Employee:
    # shared by all employees
    company = "OpenMat Inc."

    def __init__(self, name, birth_date) -> None:
        self.name = name
        self.birth_date = birth_date

    @property
    def birth_date(self):
        return self._birth_date

    @birth_date.setter
    def birth_date(self, value):
        try:
            parsed_date = datetime.fromisoformat(value)
            if parsed_date > datetime.now():
                raise ValueError("Birth date cannot be in the future")
            self._birth_date = parsed_date
        except ValueError as e:
            print(f"Invalid date: {e}")

    def compute_age(self):
        today = datetime.today()
        age = today.year - self.birth_date.year
        upcoming_birthday = datetime(
            today.year,
            self.birth_date.month,
            self.birth_date.day,
        )
        if today < upcoming_birthday:
            age -= 1
        return age

    @classmethod
    def from_dict(cls, data_dict):
        return cls(**data_dict)

    def __str__(self):
        return f"{self.name} is {self.compute_age()} years old"

    def __repr__(self):
        return (
            f"{type(self).__name__}("
            f"name='{self.name}', "
            f"birth_date='{self.birth_date.strftime('%Y-%m-%d')}')"
        )


e = Employee(name="Joe", birth_date="2020-03-10")
