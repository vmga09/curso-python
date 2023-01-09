# Create an empty tuple

nueva_tuple = ()

new_tuple = tuple()
print(new_tuple)


# Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)

sisters = ('Javiera', 'Carla', 'Heilyn', 'Matilde')
brothers = ('Juan', 'Pedro', 'Mario', 'Carlos')

all_brothers = brothers + sisters

print(all_brothers)
# How many siblings do you have?
print(len(all_brothers))


# Modify the siblings tuple and add the name of your father and mother and assign it to family_members
parents = ('Juan carlos', 'Miriam')
family = all_brothers + parents
print(family)
# How many siblings do you have?

########### LEVEL 2 #####################
# Unpack siblings and parents from family_members
ju, pe, ma, ca, ja, car, he, ma, *parents = family

print(ju, pe, ma, ca, ja, car, he, ma, parents)

# Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot')
animals = ('dog', 'cat', 'snake', 'lion')
food_stuff_tp = fruits + vegetables + animals


# Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)

# Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
print(food_stuff_lt[int(len(food_stuff_lt)/2)])


# Slice out the first three items and the last three items from food_staff_lt list
print(food_stuff_lt[0:3], food_stuff_tp[-3:])

# Delete the food_staff_tp tuple completely

del food_stuff_tp

# Check if an item exists in tuple:

nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')

print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)
