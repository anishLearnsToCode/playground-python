import datetime
import pprint


class Employee:
    raise_amount = 1.05

    def __init__(self, first_name: str, last_name: str, age: int):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.salary = 1000

    def increase_salary(self):
        self.salary *= Employee.raise_amount

    def full_name(self) -> str:
        return f'{self.first_name} {self.last_name}'

    # decorator
    @classmethod
    def set_raise_amount(cls, amount: float):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, string: str):
        first_name, last_name, age = string.split('-')
        return Employee(first_name, last_name, age)

    @staticmethod
    def is_work_day(day):
        if day.weekday() in (5, 6):
            return False
        return True

    @property
    def fullname(self):
        return f'{self.first_name} {self.last_name}'

    @fullname.setter
    def fullname(self, value: str):
        self.first_name, self.last_name = value.split()

    def __repr__(self):
        return f'Employee(first={self.first_name}, last={self.last_name}, age={self.age}, salary={self.salary})'

    def __add__(self, other):
        print('hey i am adding employees together')
        return 'hello'


class Developer(Employee):
    def __init__(self, first_name, last_name, age, language):
        super().__init__(first_name, last_name, age)
        self.language = language

    # for developers
    def __repr__(self):
        return 'hello'

    # for customers
    def __str__(self):
        return 'hey'


john = Employee(first_name='john', last_name='doe', age=30)
print(john)
Employee.set_raise_amount(1.10)
print(john.raise_amount)
print(Employee.raise_amount)
john.increase_salary()
print(john)

# Factory pattern object creation
ada = Employee.from_string('Ada-Lovelace-22')
print(ada)
ada.increase_salary()
ada.increase_salary()
print(ada)

some_day = datetime.datetime(2021, 1, 15)
print(Employee.is_work_day(some_day))

print(john + ada)

# anish = Developer(first_name='Anish', last_name='Sachdeva', age=22, language='Java')
# ada = Developer(first_name='Ada', last_name='Lovelace', age=30, language='Python')

# print(ada)
# pprint.pprint(ada)
