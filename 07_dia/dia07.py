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
