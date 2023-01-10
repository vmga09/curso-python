############### SET################

# sets
it_companies = {'Facebook', 'Google', 'Microsoft',
                'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]


# Find the length of the set it_companies
print(len(it_companies))

# Add 'Twitter' to it_companies
it_companies.add('Twitter')

# Insert multiple IT companies at once to the set it_companies
it_companies.update(['Netflix', 'Blizard'])
oher_companies = ['Redhat', 'ELK']
it_companies.update(oher_companies)


print(it_companies)

# Remove one of the companies from the set it_companies
it_companies.remove('Apple')
print(it_companies)

# Remove all the companies from the set it_companies
it_companies.clear()
print(it_companies)


################ LEVEL2 ######################

# Join A and B

C = A.union(B)
# C2 = A.update(B)
print(C,  A)


# Find A intersection B
print(B.intersection(A))


# Is A subset of B
print(A.issubset(B))

# Are A and B disjoint sets

print(A.isdisjoint(B))


# Join A with B and B with A

D = A.union(B)
E = B.union(A)
print(D, E)


# What is the symmetric difference between A and B

print(A.symmetric_difference(B))

# Delete the sets completely

del A, B, C, D, E


############  LEVEL 3  ################

# Convert the ages to a set and compare the length of the list and the set, which one is bigger?
ages = set(age)
print(len(ages), len(age))

print(len(ages) is len(age))


# I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.


new_array = 'I am a teacher and I love to inspire and teach people'.split(' ')
new_set = set(new_array)
print(new_array, new_set)
