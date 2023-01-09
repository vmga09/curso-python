# Declare an empty list

lst = []
new_list = list()

# Declare a list with more than 5 items

new_list = ['lunes', 'martes', 'miercoles', 'jueves', 'viernes']

# Find the length of your list
print(len(new_list))

# Get the first item, the middle item and the last item of the list

first_item = new_list[0]
middle_item = new_list[2]
last_item = new_list[-1]

# Declare a list called mixed_data_types, put your(name, age, height, marital status, address)

mixed_data_types = ['Victor Gonzalez', 45, 85, 'married', {
    "City": "Santiago", "Countrty": "Chile", "address": "Huerfanos 1977", "depto": 305}]

# Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.

it_companies = ['Facebook', 'Google', 'Microsoft',
                'Apple', 'IBM', 'Oracle', 'Amazon']

# Print the list using print()
print(it_companies)

# Print the number of companies in the list
print(len(it_companies))

# Print the first, middle and last company
print(it_companies[0], it_companies[3], it_companies[-1])

# Print the list after modifying one of the companies
it_companies[3] = 'Twitter'
print(it_companies)

# Add an IT company to it_companies

it_companies.append('Meta')
print(it_companies)

# Insert an IT company in the middle of the companies list
it_companies.insert(3, 'Netflix')
print(it_companies)

# Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[3] = it_companies[3].upper()
print(it_companies)

# Join the it_companies with a string '#;  '
print('#'.join(it_companies))

# Check if a certain company exists in the it_companies list.

print('Apple' in it_companies)
print('IBM' in it_companies)

# Sort the list using sort() method

it_companies.sort()
print(it_companies)


# Reverse the list in descending order using reverse() method

it_companies.reverse()
print(it_companies)


# Sort the list in ascending order using sort() method

it_companies.sort(reverse=True)
print(it_companies)

# Slice out the first 3 companies from the list

n_it_com = it_companies[0:3]
print(n_it_com)

# Slice out the last 3 companies from the list
print(it_companies)
n_it_com = it_companies[-3:]
print(n_it_com)

# Slice out the middle IT company or companies from the list
print(it_companies[1:len(it_companies)-1])

# Remove the first IT company from the list
print(it_companies.pop(0))
print(it_companies)

# Remove the last IT company from the list
print(it_companies.pop(-1))
print(it_companies)

# Remove the middle IT company from the list
print(it_companies.pop(3))
print(it_companies)

# Remove all IT companies from the list


print(it_companies.clear())
print(it_companies)
del it_companies


# 26 y 27 Join the following lists:, After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']

# Join list
full_stack = front_end + back_end

full_stack.insert(full_stack.index('Redux')+1, 'Python')
full_stack.insert(full_stack.index('Redux')+2, 'SQL')

print(full_stack)


# LEVEL 2

# The following is a list of 10 students ages:

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Sort the list and find the min and max age
ages.sort()
print(ages)

min_age = ages[0]
max_age = ages[-1]

# Add the min age and the max age again to the list
ages.insert(0, min_age)
ages.insert(-1, max_age)
print(ages)


# Find the median age (one middle item or two middle items divided by two)

median_age = ages[int(len(ages)/2)]
print(median_age)

#
# Find the average age (sum of all items divided by their number )
average_age = sum(ages)/len(ages)
print(average_age)
# Find the range of the ages (max minus min)
range_ages = max_age - min_age
print(range_ages)

# Compare the value of (min - average) and (max - average), use abs() method
comp1 = abs(min_age - average_age)
comp2 = abs(max_age - average_age)

print(comp1 is comp2)

# Divide the countries list into two equal lists if it is even if not one more country for the first half.

countries = [
    'Afghanistan',
    'Albania',
    'Algeria',
    'Andorra',
    'Angola',
    'Antigua and Barbuda',
    'Argentina',
    'Armenia',
    'Australia',
    'Austria',
    'Azerbaijan',
    'Bahamas',
    'Bahrain',
    'Bangladesh',
    'Barbados',
    'Belarus',
    'Belgium',
    'Belize',
    'Benin',
    'Bhutan',
    'Bolivia',
    'Bosnia and Herzegovina',
    'Botswana',
    'Brazil',
    'Brunei',
    'Bulgaria',
    'Burkina Faso',
    'Burundi',
    'Cambodia',
    'Cameroon',
    'Canada',
    'Cape Verde',
    'Central African Republic',
    'Chad',
    'Chile',
    'China',
    'Colombi',
    'Comoros',
    'Congo (Brazzaville)',
    'Congo',
    'Costa Rica',
    "Cote d'Ivoire",
    'Croatia',
    'Cuba',
    'Cyprus',
    'Czech Republic',
    'Denmark',
    'Djibouti',
    'Dominica',
    'Dominican Republic',
    'East Timor (Timor Timur)',
    'Ecuador',
    'Egypt',
    'El Salvador',
    'Equatorial Guinea',
    'Eritrea',
    'Estonia',
    'Ethiopia',
    'Fiji',
    'Finland',
    'France',
    'Gabon',
    'Gambia, The',
    'Georgia',
    'Germany',
    'Ghana',
    'Greece',
    'Grenada',
    'Guatemala',
    'Guinea',
    'Guinea-Bissau',
    'Guyana',
    'Haiti',
    'Honduras',
    'Hungary',
    'Iceland',
    'India',
    'Indonesia',
    'Iran',
    'Iraq',
    'Ireland',
    'Israel',
    'Italy',
    'Jamaica',
    'Japan',
    'Jordan',
    'Kazakhstan',
    'Kenya',
    'Kiribati',
    'Korea, North',
    'Korea, South',
    'Kuwait',
    'Kyrgyzstan',
    'Laos',
    'Latvia',
    'Lebanon',
    'Lesotho',
    'Liberia',
    'Libya',
    'Liechtenstein',
    'Lithuania',
    'Luxembourg',
    'Macedonia',
    'Madagascar',
    'Malawi',
    'Malaysia',
    'Maldives',
    'Mali',
    'Malta',
    'Marshall Islands',
    'Mauritania',
    'Mauritius',
    'Mexico',
    'Micronesia',
    'Moldova',
    'Monaco',
    'Mongolia',
    'Morocco',
    'Mozambique',
    'Myanmar',
    'Namibia',
    'Nauru',
    'Nepal',
    'Netherlands',
    'New Zealand',
    'Nicaragua',
    'Niger',
    'Nigeria',
    'Norway',
    'Oman',
    'Pakistan',
    'Palau',
    'Panama',
    'Papua New Guinea',
    'Paraguay',
    'Peru',
    'Philippines',
    'Poland',
    'Portugal',
    'Qatar',
    'Romania',
    'Russia',
    'Rwanda',
    'Saint Kitts and Nevis',
    'Saint Lucia',
    'Saint Vincent',
    'Samoa',
    'San Marino',
    'Sao Tome and Principe',
    'Saudi Arabia',
    'Senegal',
    'Serbia and Montenegro',
    'Seychelles',
    'Sierra Leone',
    'Singapore',
    'Slovakia',
    'Slovenia',
    'Solomon Islands',
    'Somalia',
    'South Africa',
    'Spain',
    'Sri Lanka',
    'Sudan',
    'Suriname',
    'Swaziland',
    'Sweden',
    'Switzerland',
    'Syria',
    'Taiwan',
    'Tajikistan',
    'Tanzania',
    'Thailand',
    'Togo',
    'Tonga',
    'Trinidad and Tobago',
    'Tunisia',
    'Turkey',
    'Turkmenistan',
    'Tuvalu',
    'Uganda',
    'Ukraine',
    'United Arab Emirates',
    'United Kingdom',
    'United States',
    'Uruguay',
    'Uzbekistan',
    'Vanuatu',
    'Vatican City',
    'Venezuela',
    'Vietnam',
    'Yemen',
    'Zambia',
    'Zimbabwe',
]

len_country = len(countries)
print(len_country)

list_country_1 = countries[0:int(len_country/2)]
list_country_2 = countries[int(len_country/2):]


print(list_country_1, list_country_2)

# ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
paises = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
ch, ru, us, *scandisc = paises

print(ch, ru, us, scandisc)
