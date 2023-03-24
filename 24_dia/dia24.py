import numpy as np

# Creating python List
python_list = [1, 2, 3, 4, 5]

# Checking data types
print('Type:', type(python_list))  # <class 'list'>
#
print(python_list)  # [1, 2, 3, 4, 5]

two_dimensional_list = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

print(two_dimensional_list)  # [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

# Creating Numpy(Numerical Python) array from python list

numpy_array_from_list = np.array(python_list)

# Tipo Float
numpy_array_from_list2 = np.array(python_list, dtype=float)
print(type(numpy_array_from_list))   # <class 'numpy.ndarray'>
print(numpy_array_from_list)  # array([1, 2, 3, 4, 5])
print(numpy_array_from_list2)

# Boolean numpy
numpy_bool_array = np.array([0, 1, -1, 0, 0], dtype=bool)
print(numpy_bool_array)  # array([False,  True,  True, False, False])


# Multidimensional numpy array
two_dimensional_list = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
numpy_two_dimensional_list = np.array(two_dimensional_list)
print(numpy_two_dimensional_list)


# We can always convert an array back to a python list using tolist().
np_to_list = numpy_array_from_list.tolist()
print(type(np_to_list))
print('one dimensional array:', np_to_list)
print('two dimensional array: ', numpy_two_dimensional_list.tolist())


python_tuple = (1, 2, 3, 4, 5)
numpy_array_from_tuple = np.array(python_tuple)
print('numpy_array_from_tuple: ', numpy_array_from_tuple)


# Shape method  return dimensional arrays

nums = np.array([1, 2, 3, 4, 5])
print('nums: ', nums)
print('shape of nums: ', nums.shape)
print(numpy_two_dimensional_list.shape)

three_by_four_array = np.array([[0, 1, 2, 3],
                                [4, 5, 6, 7],
                                [8, 9, 10, 11]])

print(three_by_four_array.shape)

# Size of a numpy array
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
two_dimensional_list = np.array([[0, 1, 2],
                                 [3, 4, 5],
                                 [6, 7, 8]])

print('The size:', numpy_array_from_list.size)  # 5
print('The size:', two_dimensional_list.size)  # 3

# Addition
numppy_array_list = np.array([10, 20, 30, 40, 50])
sum_array = numppy_array_list + 10
rest_array = numppy_array_list - 10
mult_array = numppy_array_list * 10
div_array = numppy_array_list / 10
ten_times_original = numppy_array_list % 3
exp_array = numppy_array_list ** 2
print(sum_array)
print(rest_array)
print(mult_array)
print(div_array)
print(ten_times_original)
print(exp_array)


two_dimension_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
first_row = two_dimension_array[0]
second_row = two_dimension_array[1]
third_row = two_dimension_array[2]
print('First row:', first_row)
print('Second row:', second_row)
print('Third row: ', third_row)

first_column = two_dimension_array[:, 0]
second_column = two_dimension_array[:, 1]
third_column = two_dimension_array[:, 2]
print('First column:', first_column)
print('Second column:', second_column)
print('Third column: ', third_column)
print(two_dimension_array)


two_dimension_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
first_two_rows_and_columns = two_dimension_array[1:3, 1:2]
print(first_two_rows_and_columns)

print(two_dimension_array[::])
print(two_dimension_array[::-1, ::-1])

print(two_dimension_array)
two_dimension_array[0, 0] = 5567
two_dimension_array[1, 2] = 44
print(two_dimension_array)

# Generating a random integers between 0 and 10
random_int = np.random.randint(0, 10, size=(50, 50))
print(random_int)

# np.random.normal(mu, sigma, size)
normal_array = np.random.normal(79, 15, 80)
print(normal_array)
