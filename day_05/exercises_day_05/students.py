ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Sorting and finding the minimum and maximum age
print(ages)
ages.sort()
print(f'The minimum age is {ages[0]}, and the maximum age is {ages[-1]}')

# Finding the median age
median_index = len(ages) // 2 # can do this because the list is sorted, so the median is the middle value
print(ages[median_index])

#Finding the average age
average_age = sum(ages) / len(ages) #discovered that the sum() function can be used to find the sum of all items in a list
print(f'The average age is {average_age}')

# Finding the range of ages
range_of_ages = ages[-1] - ages[0]
print(f'The range of ages is {range_of_ages}')

# Comparing the value of (min - average) and (max - average), using the abs() function to get the absolute value
min_average_difference = abs(ages[0] - average_age)
max_average_difference = abs(ages[-1] - average_age)
print(f'The absolute difference between the minimum age and the average age is {min_average_difference}')
print(f'The absolute difference between the maximum age and the average age is {max_average_difference}')

