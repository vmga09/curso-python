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
