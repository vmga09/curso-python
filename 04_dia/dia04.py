# Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.

print("Thirty "+"Days "+"of "+"Python")

# Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.

print("Coding "+"For " + "All")

# Declare a variable named company and assign it to an initial value "Coding For All".

company = "Coding For All"

# Print the variable company using print().
print(company)

# Print the length of the company string using len() method and print().

print(len(company))


# Change all the characters to uppercase letters using upper() method.

new_company = "Coding For All"
print(new_company.upper())


# Change all the characters to lowercase letters using lower() method.

old_company = "Coding For All"
print(old_company.lower())

# Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.

nombre_completo = 'victor manuel gonzalez araya'
print(nombre_completo.capitalize())
print(nombre_completo.title())
print(nombre_completo.swapcase())


# Cut(slice) out the first word of Coding For All string.
print(old_company[0:6])

# Check if Coding For All string contains a word Coding using the method index, find or other methods.
print(old_company.find('Coding') != -1)
print(old_company.index('Coding'))

# Replace the word coding in the string 'Coding For All' to Python.

print(old_company.replace('Coding', 'Python'))

# Replace the word coding in the string 'Coding For All' to 'Coding For All Python'.

print(old_company.replace('Coding For All', 'Coding For All Python'))

# Change Python for Everyone to Python for All using the replace method or other methods.

new_var = 'Python for Everyone'
print(new_var.replace('Everyone', 'All'))

# Split the string 'Coding For All' using space as the separator (split()) .

print(old_company.split(" "))

# "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"

print(companies.split(","))

# What is the character at index 0 in the string Coding For All.
print(old_company[0])

# What is the last index of the string Coding For All.
print(old_company[len(old_company)-1])

# What character is at index 10 in "Coding For All" string.
print(old_company[10])


# Create an acronym or an abbreviation for the name 'Python For Everyone'.
new_leter = "Python For Everyone"
letra4 = new_leter.split()[0][0]
letra5 = new_leter.split()[1][0]
letra6 = new_leter.split()[2][0]
print(letra4+letra5+letra6)


# Create an acronym or an abbreviation for the name 'Coding For All'.
letra1 = old_company.split()[0][0]
letra2 = old_company.split()[1][0]
letra3 = old_company.split()[2][0]
print(letra1+letra2+letra3)


# Use index to determine the position of the first occurrence of C in Coding For All.

print(old_company.index('C'))

# Use index to determine the position of the first occurrence of F in Coding For All.
print(old_company.index('F'))

# Use rfind to determine the position of the last occurrence of l in Coding For All People.
print(old_company.find('l'))
print(old_company.rfind('l'))

# Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
new_text = 'You cannot end a sentence with because because because is a conjunction'
print(new_text.find('because'))

# Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(new_text.rindex('because'))
print(new_text.rfind('because'))

# Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
largo = len('because because because')
inicio = new_text.find('because because because')

extarc = new_text[inicio:(inicio + largo)]
print(extarc)

# Does ''Coding For All' start with a substring Coding?

print(old_company.startswith('Coding'))

# Does 'Coding For All' end with a substring coding?
print(old_company.endswith('coding'))

# '   Coding For All      '  , remove the left and right trailing spaces in the given string.
new_texto = '   Coding For All      '

print(new_texto.strip(' '))

# Which one of the following variables return True when we use the method isidentifier():

#    30DaysOfPython
#    thirty_days_of_python

print('30DaysOfPython'.isidentifier())
print('thirty_days_of_python'.isidentifier())

# The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.

libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(' '.join(libraries))

# Use the new line escape sequence to separate the following sentences.
print('I am enjoying this challenge.\n')
print('I just wonder what is next.\n')

# Use a tab escape sequence to write the following lines.
print('Name\t Age\t Country\t City\t')
print('Asabeneh\t 250\t Finland\t Helsinki\t')


# Use the string formatting method to display the following:

radius = 10
area = 3.14 * radius ** 2
print('The area of a circle with radius {} is {}'.format(str(radius), str(area)))

# Make the following using string formatting methods:

print('{} + {} = {}'.format(str(8), str(6), str(14)))
print('{} - {} = {}'.format(str(8), str(6), str(2)))
print('{} * {} = {}'.format(str(8), str(6), str(48)))
print('{} / {} = {}'.format(str(8), str(6), str(1.33)))
print('{} % {} = {}'.format(str(8), str(6), str(2)))
print('{} // {} = {}'.format(str(8), str(6), str(1)))
print('{} ** {} = {}'.format(str(8), str(6), str(262144)))
