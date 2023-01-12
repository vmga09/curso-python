################## LOOP ######################################

# 💻 Exercises: Day 10

# Exercises: Level 1

# 1. Iterate 0 to 10 using for loop, do the same using while loop.

num = 0
while num <= 10:
    print(num)
    num += 1

for i in range(11):
    print(i)

# 2. Iterate 10 to 0 using for loop, do the same using while loop.

new_num = 10
while new_num >= 0:
    print(new_num)
    new_num -= 1


for x in range(10, -1, -1):
    print(x)

# 3. Write a loop that makes seven calls to print(), so we get on the output the following triangle:

#    ```py
#    #
#    ##
#    ###
#    ####
#    #####
#    ######
#    #######
#    ```

alm = '#'
for y in range(7):
    print(alm)
    alm = alm+'#'

# 4. Use nested loops to create the following:

#    ```sh
#    # # # # # # # #
#    # # # # # # # #
#    # # # # # # # #
#    # # # # # # # #
#    # # # # # # # #
#    # # # # # # # #
#    # # # # # # # #
#    # # # # # # # #
#    ```

for z in range(8):
    print('# # # # # # # #')


# 5. Print the following pattern:

#    ```sh
#    0 x 0 = 0
#    1 x 1 = 1
#    2 x 2 = 4
#    3 x 3 = 9
#    4 x 4 = 16
#    5 x 5 = 25
#    6 x 6 = 36
#    7 x 7 = 49
#    8 x 8 = 64
#    9 x 9 = 81
#    10 x 10 = 100
#    ```

for t in range(11):
    product = t*t
    print('{} x {} = {}'.format(t, t, product))


# 6. Iterate through the list, ['Python', 'Numpy', 'Pandas', 'Django', 'Flask'] using a for loop and print out the items.

new_list = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']

for n in new_list:
    print(n)



i=0
while i < len(new_list):
    print(new_list[i])
    i += 1

# 7. Use for loop to iterate from 0 to 100 and print only even numbers

for x in range(101):
    if x%2 == 0:
        print(x)
# 8. Use for loop to iterate from 0 to 100 and print only odd numbers

for x in range(101):
    if x%2 == 1:
        print(x)

# # Exercises: Level 2

# 1.  Use for loop to iterate from 0 to 100 and print the sum of all numbers.

sum = 0
for x in range(101):
    sum += x
    print(sum)

# ```sh
# The sum of all numbers is 5050.
# ```

# 1. Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.

evens = 0
odds = 0

for x in range(101):
    if x%2 == 0:
        evens += x
    else:
        odds += x

print('The sum of all evens is {}. And the sum of all odds is {}.'.format(evens, odds))



# ```sh
# The sum of all evens is 2550. And the sum of all odds is 2500.
# ```

# # Exercises: Level 3

# 1. Go to the data folder and use the[countries.py](https: // github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries.py) file. Loop through the countries and extract all the countries containing the word _land_.
# 1. This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
# 2. Go to the data folder and use the[countries_data.py](https: // github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries-data.py) file.
# 1. What are the total number of languages in the data
# 2. Find the ten most spoken languages from the data
# 3. Find the 10 most populated countries in the world

# 🎉 CONGRATULATIONS ! 🎉
