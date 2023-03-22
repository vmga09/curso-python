import statistics
# class Person:
#     def __init__(self, name='Victor'):
#         self.name = name


# p = Person()
# print(p.name)


# class Person:
#     def __init__(self, firstname, lastname, age, country, city):
#         self.firstname = firstname
#         self.lastname = lastname
#         self.age = age
#         self.country = country
#         self.city = city

#     def personal_info(self):
#         return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}'


# p = Person('Victor', 'Gonzalez', 46, 'Chile', 'Santiago')

# print(p.age)
# print(p.firstname)
# print(p.personal_info())


class Persons:
    def __init__(self, firstname='Asabeneh', lastname='Yetayeh', age=250, country='Finland', city='Helsinki'):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city
        self.skills = []

    def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}.'

    def add_skill(self, skill):
        self.skills.append(skill)


p1 = Persons()
print(p1.person_info())
p1.add_skill('HTML')
p1.add_skill('CSS')
p1.add_skill('JavaScript')
p2 = Persons('John', 'Doe', 30, 'Nomanland', 'Noman city')
print(p2.person_info())
print(p1.skills)
print(p2.skills)


class Statistics:
    def __init__(self, arr):
        self.name = arr

    def count(self):
        return len(self.name)

    def sum(self):
        return sum(self.name)

    def min(self):
        return min(self.name)

    def max(self):
        return max(self.name)

    def range(self):
        return max(self.name)-min(self.name)

    def mean(self):
        return statistics.mean(self.name)

    def median(self):
        return statistics.median(self.name)

    def mode(self):
        return statistics.mode(self.name)

    def std(self):
        return statistics.stdev(self.name)

    def var(self):
        return statistics.variance(self.name)

    def describe(self):
        return f'''Count: {len(self.name)}
                Sum:  {sum(self.name)}
                Min:  {min(self.name)}
                Max:  {max(self.name)}
                Range:  {max(self.name)-min(self.name)}
                Mean:  {statistics.mean(self.name)}
                Median:  {statistics.median(self.name)}
                Mode:  {statistics.mode(self.name)}
                Variance:  {statistics.variance(self.name)}
                Standard Deviation:  {statistics.variance(self.name)}   '''


data = Statistics([31, 26, 34, 37, 27, 26, 32, 32, 26, 27,
                  27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26])


print(data.std())
print(data.describe())
