# NumPy: A library for numerical computing in Python
# How to import numpy
import numpy as np

print("numpy:", np.__version__)  # How to check the version of the numpy package
print(dir(np))  # Checking the available methods

# NumPy Arrays: Creating and manipulating arrays
# Int Numpy arrays
# Creating python List
python_list = [1, 2, 3, 4, 5]
# Checking data types
print("Type:", type(python_list))  # <class 'list'>
print(python_list)  # [1, 2, 3, 4, 5]
two_dimensional_list = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
print(two_dimensional_list)  # [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
# Creating Numpy(Numerical Python) array from python list
numpy_array_from_list = np.array(python_list)
print(type(numpy_array_from_list))  # <class 'numpy.ndarray'>
print(numpy_array_from_list)  # array([1, 2, 3, 4, 5])

# Creating Float Numpy arrays
# Python list
python_list = [1, 2, 3, 4, 5]

numpy_array_from_list2 = np.array(python_list, dtype=float)
print(numpy_array_from_list2)  # array([1., 2., 3., 4., 5.])

# Crating a Boolean Numpy array
numpy_bool_array = np.array([0, 1, -1, 0, 0], dtype=bool)
print(numpy_bool_array)  # array([False,  True,  True, False, False])

# Creating a Multi-dimensional Numpy array
two_dimensional_list = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
numpy_two_dimensional_list = np.array(two_dimensional_list)
print(type(numpy_two_dimensional_list))
print(numpy_two_dimensional_list)
# [[0 1 2]
# [3 4 5]
# [6 7 8]]

# Converting a Numpy array to a Python list
# We can always convert an array back to a python list using tolist().
np_to_list = numpy_array_from_list.tolist()
print(type(np_to_list))
print("one dimensional array:", np_to_list)
print("two dimensional array: ", numpy_two_dimensional_list.tolist())

# Creating Numpy Array from tuple
# Creating tuple in Python
python_tuple = (1, 2, 3, 4, 5)
print(type(python_tuple))  # <class 'tuple'>
print("python_tuple: ", python_tuple)  # python_tuple:  (1, 2, 3, 4, 5)

numpy_array_from_tuple = np.array(python_tuple)
print(type(numpy_array_from_tuple))  # <class 'numpy.ndarray'>
print(
    "numpy_array_from_tuple: ", numpy_array_from_tuple
)  # numpy_array_from_tuple:  [1 2 3 4 5]

# Shape of Numpy Arrays
# The shape of an array is the number of elements in each dimension.
nums = np.array([1, 2, 3, 4, 5])
print(nums)
print("shape of nums: ", nums.shape)  # shape of nums:  (5,)
numpy_two_dimensional_list = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
print(numpy_two_dimensional_list)
print(
    "shape of numpy_two_dimensional_list: ", numpy_two_dimensional_list.shape
)  # shape of numpy_two_dimensional_list:  (3, 3)
three_by_four_array = np.array([[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]])
print(three_by_four_array)
print(
    "shape of three_by_four_array: ", three_by_four_array.shape
)  # shape of three_by_four_array:  (3, 4)

# Data Type of Numpy Arrays
int_lists = [-3, -2, -1, 0, 1, 2, 3]
int_array = np.array(int_lists)
float_array = np.array(int_lists, dtype=float)

print(int_array)
print(int_array.dtype)
print(float_array)
print(float_array.dtype)

# Size of Numpy Arrays
# The size of an array is the total number of elements in the array.
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
two_dimensional_list = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])

print("The size:", numpy_array_from_list.size)  # 5
print("The size:", two_dimensional_list.size)  # 9

# Mathematical Operations Using Numpy

# Addition
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('original array: ', numpy_array_from_list)
ten_plus_original = numpy_array_from_list  + 10
print(ten_plus_original) #  [11 12 13 14 15]

# Subtraction
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('original array: ', numpy_array_from_list)
ten_minus_original = numpy_array_from_list  - 10
print(ten_minus_original) #  [-9 -8 -7 -6 -5]

# Multiplication
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('original array: ', numpy_array_from_list)
ten_times_original = numpy_array_from_list  * 10
print(ten_times_original) #  [10 20 30 40 50]

# Division
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('original array: ', numpy_array_from_list)
ten_divided_original = numpy_array_from_list  / 10
print(ten_divided_original) #  [0.1 0.2 0.3 0.4 0.5]

# Modulus
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('original array: ', numpy_array_from_list)
ten_modulus_original = numpy_array_from_list  % 10
print(ten_modulus_original) #  [1 2 3 4 5]

# Floor Division (division result without the remainder)
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('original array: ', numpy_array_from_list)
ten_floor_divided_original = numpy_array_from_list  // 10
print(ten_floor_divided_original) #  [0 0 0 0 0]

# Exponentiation
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('original array: ', numpy_array_from_list)
ten_exponentiation_original = numpy_array_from_list  ** 2
print(ten_exponentiation_original) #  [ 1  4  9 16 25]

# Checking data types
#Int,  Float numbers
numpy_int_arr = np.array([1,2,3,4])
numpy_float_arr = np.array([1.1, 2.0,3.2])
numpy_bool_arr = np.array([-3, -2, 0, 1,2,3], dtype='bool')

print(numpy_int_arr.dtype) # int64
print(numpy_float_arr.dtype) # float64
print(numpy_bool_arr.dtype) # bool

# To convert the data type of an array, we can use dtype.
numpy_int_arr = np.array([1,2,3,4], dtype = 'float')
print(numpy_int_arr.dtype) # float64

numpy_float_arr = np.array([1.1, 2.0,3.2], dtype = 'int')
print(numpy_float_arr.dtype) # int64

# Using astype() method to convert the data type of an array
numpy_int_arr = np.array([1,2,3,4])
numpy_int_arr = numpy_int_arr.astype('float')
print(numpy_int_arr.dtype) # float64

# Multi-Dimensional Arrays
# 2 Dimension Array
two_dimension_array = np.array([(1,2,3),(4,5,6), (7,8,9)])
print(type (two_dimension_array))
print(two_dimension_array)
print('Shape: ', two_dimension_array.shape)
print('Size:', two_dimension_array.size)
print('Data type:', two_dimension_array.dtype)

# Getting Items from a numpy array
# 2 Dimension Array
two_dimension_array = np.array([[1,2,3],[4,5,6], [7,8,9]])
first_row = two_dimension_array[0]
second_row = two_dimension_array[1]
third_row = two_dimension_array[2]
print('First row:', first_row)
print('Second row:', second_row)
print('Third row: ', third_row)

first_column= two_dimension_array[:,0]
second_column = two_dimension_array[:,1]
third_column = two_dimension_array[:,2]
print('First column:', first_column)
print('Second column:', second_column)
print('Third column: ', third_column)
print(two_dimension_array)

# Slicing a numpy array
two_dimension_array = np.array([[1,2,3],[4,5,6], [7,8,9]])
first_two_rows_and_columns = two_dimension_array[0:2, 0:2] # rows, columns
print(first_two_rows_and_columns)

# Reversing the rows and columns of a numpy array
two_dimension_array = np.array([[1,2,3],[4,5,6], [7,8,9]])
two_dimension_array[::-1,::-1]
print(two_dimension_array)

# Representing missing values in a numpy array
print(two_dimension_array)
two_dimension_array[1,1] = 55
two_dimension_array[1,2] =44
print(two_dimension_array)

# Numpy zeroes and ones
# numpy.zeros(shape, dtype=float, order='C')
numpy_zeroes = np.zeros((3,3),dtype=int,order='C')
print(numpy_zeroes)

# numpy.ones(shape, dtype=float, order='C')
numpy_ones = np.ones((3,3),dtype=int,order='C')
print(numpy_ones)

# Reshaping a numpy array
# Reshape
# numpy.reshape(), numpy.flatten()
first_shape  = np.array([(1,2,3), (4,5,6)])
print(first_shape)
reshaped = first_shape.reshape(3,2) # rows, columns
print(reshaped)

# Flattening a numpy array
flattened = first_shape.flatten()
print(flattened)

# Horizontally stacking numpy arrays
array1 = np.array([[1, 2], [3, 4]])
array2 = np.array([[5, 6], [7, 8]])
stacked = np.hstack((array1, array2))
print(stacked)

# Vertically stacking numpy arrays
array1 = np.array([[1, 2], [3, 4]])
array2 = np.array([[5, 6], [7, 8]])
stacked = np.vstack((array1, array2))
print(stacked)

# Generating random numbers using numpy
# numpy.random.rand(d0, d1, ..., dn)
# Generate a random float  number
random_floats = np.random.random(5)
print(random_floats)

# Generate a random integer number
random_integers = np.random.randint(0, 11)
print(random_integers)

# Generating a random integers between 2 and 11, and creating a one row array
random_int = np.random.randint(2,10, size=4)
print(random_int)

# np.random.normal(mu, sigma, size)
normal_array = np.random.normal(79, 15, 80) # mean=79, std=15, size=80
print(normal_array)

# Numpy and Statistics
import matplotlib.pyplot as plt
import seaborn as sns
sns.set() # Set the style of the plots
plt.hist(normal_array, color="grey", bins=50) # Plotting the histogram of the normal distribution

# Matrix in numpy
four_by_four_matrix = np.matrix(np.ones((4,4), dtype=float))
print(four_by_four_matrix)

np.asarray(four_by_four_matrix)[2] = 2
four_by_four_matrix

# numpy.arange(start, stop, step)
# arrange is used to create an array with evenly spaced values within a given interval.
whole_numbers = np.arange(0, 10, 1) # start=0, stop=10, step=1
print(whole_numbers) # [0 1 2 3 4 5 6 7 8 9]

odd_numbers = np.arange(1, 10, 2) # start=1, stop=10, step=2
print(odd_numbers) # [1 3 5 7 9]

# Sequence of numbers using numpy.linspace(start, stop, num)
# numpy.linspace()
# numpy.logspace() in Python with Example
# For instance, it can be used to create 10 values from 1 to 5 evenly spaced.
np.linspace(1.0, 5.0, num=10)
# not to include the last value in the interval
np.linspace(1.0, 5.0, num=5, endpoint=False)

# logspace() is used to create an array of numbers that are evenly spaced on a log scale.
# For instance, it can be used to create 10 values from 10^1 to 10^5 evenly spaced on a log scale.
np.logspace(1.0, 5.0, num=10)

# Indexing and Slicing in Numpy
# indexing and Slicing NumPy Arrays in Python
np_list = np.array([(1,2,3), (4,5,6)])
print(np_list)
print('First row: ', np_list[0])
print('Second row: ', np_list[1])
print('First column: ', np_list[:,0])
print('Second column: ', np_list[:,1])
print('Third column: ', np_list[:,2])

# Numpy Statistical Functions

# np.min() and np.max() in Python with Example
# np.min() is used to find the minimum value in an array.
# np.max() is used to find the maximum value in an array.
print('Minimum value: ', np.min(np_list))
print('Maximum value: ', np.max(np_list))

# np.mean() is used to find the mean value of an array.
print('Mean value: ', np.mean(np_list))

# np.std() is used to find the standard deviation of an array.
print('Standard deviation: ', np.std(np_list))

# np.var() is used to find the variance of an array.
print('Variance: ', np.var(np_list))

# np.median() is used to find the median value of an array.
print('Median value: ', np.median(np_list))

# Creating repeating sequences
a = [1,2,3]
# Repeat whole of 'a' two times
print('Tile:   ', np.tile(a, 2))
# Repeat each element of 'a' two times
print('Repeat: ', np.repeat(a, 2))

# Generating random numbers using numpy
# One random number between [0,1)
one_random_num = np.random.random()
one_random_in = np.random
print(one_random_num)
print(one_random_in)

print(np.random.choice(['apple', 'banana', 'cherry'])) # Randomly choose one of the fruits

rand_int = np.random.randint(0, 10, size=[5,3]) # Randomly choose 5 integers between 0 and 10
print(rand_int)


from scipy import stats
np_normal_dis = np.random.normal(5, 0.5, 1000) # mean, standard deviation, number of samples
np_normal_dis
## min, max, mean, median, sd
print('min: ', np.min(np_normal_dis)) # min: 3.187
print('max: ', np.max(np_normal_dis)) # max: 6.812
print('mean: ', np.mean(np_normal_dis)) # mean: 4.999
print('median: ', np.median(np_normal_dis)) # median: 4.999
print('mode: ', stats.mode(np_normal_dis)) # mode: ModeResult(mode=array([3.187]), count=array([1]))
print('sd: ', np.std(np_normal_dis)) # sd: 0.498

plt.hist(np_normal_dis, bins=30, color='grey') # Plotting the histogram of the normal distribution
plt.title('Normal Distribution')
plt.show()


# Linear ALgebra in Numpy

# Dot Product of two vectors
vector1 = np.array([1, 2, 3])
vector2 = np.array([4, 5, 6])
print('Dot Product: ', np.dot(vector1, vector2)) # Dot Product:  32

# Matrix Multiplication of two matrices
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])
print('Matrix Multiplication: ', np.matmul(matrix1, matrix2)) # Matrix Multiplication:  [[19 22] [43 50]]

# Determinant of a matrix
matrix = np.array([[1, 2], [3, 4]])
print('Determinant: ', np.linalg.det(matrix)) # Determinant:  -2.0

# Temperature Exemple
temp = np.array([1,2,3,4,5])
pressure = temp * 2 + 5
print('Pressure: ', pressure) # Pressure:  [ 7  9 11 13 15]

plt.plot(temp,pressure)
plt.xlabel('Temperature in oC')
plt.ylabel('Pressure in atm')
plt.title('Temperature vs Pressure')
plt.xticks(np.arange(0, 6, step=0.5))
plt.show()

# Gaussian Normal Distribution
mu = 28
sigma = 15
samples = 100000

x = np.random.normal(mu, sigma, samples)
ax = sns.distplot(x);
ax.set(xlabel="x", ylabel='y')
plt.show()

