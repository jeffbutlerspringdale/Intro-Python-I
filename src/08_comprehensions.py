"""
List comprehensions are one cool and unique feature of Python.
They essentially act as a terse and concise way of initializing
and populating a list given some expression that specifies how
the list should be populated. 

Take a look at https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
for more info regarding list comprehensions.
"""

# Write a list comprehension to produce the array [1, 2, 3, 4, 5]

y = []
for x in range(5):
    y.append(x + 1)
print("first y", y)

# Write a list comprehension to produce the cubes of the numbers 0-9:
# [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]
y = []

y.append(0)
for x in range(9):
    y.append((x + 1) ** 3)
print("second y", y)

# Write a list comprehension to produce the uppercase version of all the
# elements in array a. Hint: "foo".upper() is "FOO".
y = []

a = ["foo", "bar", "baz"]
# y = [a[0].upper(), a[1].upper(), a[2].upper()]
# for x in range(len(a)):
#     y.append((a[0]).upper())
# for x in a:
#     y.append(str.upper(a[0]))

y = [w.upper() for w in a]
print("third y", y)

# Use a list comprehension to create a list containing only the _even_ elements
# the user entered into list x.

# x = input("Enter comma-separated numbers: ").split(',')
# # What do you need between the square brackets to make it work?
# y = []
#
# # import numpy as np
# #
# # x = np.array(x, dtype=np.float64)
#
# y = [num for num in x if num % 2 == 0]
#
# print("fourth y", y)


# Use a list comprehension to create a list containing only the _even_ elements
# the user entered into list x.

x = input("Enter comma-separated numbers: ").split(',')

# What do you need between the square brackets to make it work?
y = []
for x in range(len(x)):
    if x % 2 == 0:
        y.append(x)
print(y)
