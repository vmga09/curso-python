class Person:
    def __init__(self, name='Victor'):
        self.name = name


p = Person()
print(p.name)


class Person:
    def __init__(self, firstname, lastname, age, country, city):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city

    def personal_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}'


p = Person('Victor', 'Gonzalez', 46, 'Chile', 'Santiago')

print(p.age)
print(p.firstname)
print(p.personal_info())
