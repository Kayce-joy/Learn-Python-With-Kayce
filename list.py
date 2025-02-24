"""
Lists
A list is like a container that holds multiple items.
 You can change, add, or remove items. Lists use square brackets [].
"""

fruits = ["apple", "banana", "cherry"]
print(fruits[0])  # Output: apple

fruits.append("orange")  # Adding an item
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'orange']


#Advanced List Operations:
#Slicing (extract part of a list):

numbers = [1, 2, 3, 4, 5]
print(numbers[1:4])  # Output: [2, 3, 4]

#List Comprehension (short way to create lists):

squares = [x**2 for x in range(5)]
print(squares)  # Output: [0, 1, 4, 9, 16]

#Sorting & Reversing:

nums = [5, 2, 9, 1]
nums.sort()  
print(nums)  # Output: [1, 2, 5, 9]

nums.reverse()  
print(nums)  # Output: [9, 5, 2, 1]

"""
Tuples
A tuple is like a list, but cannot be changed. 
Tuples use parentheses () and are useful for storing fixed values.
"""

my_tuple = (1, 2, 3, "apple", True)
print(my_tuple)  # Output: (1, 2, 3, 'apple', True)

#Immutable: Once created, you cannot change tuple elements.

my_tuple[1] = 10  # ❌ This will raise an error

#Tuple with One Item: Use a comma to define a single-item tuple.

single_tuple = (5,)  # ✅ Correct
not_a_tuple = (5)    # ❌ This is just an integer
print(type(single_tuple))  # Output: <class 'tuple'>
print(type(not_a_tuple))   # Output: <class 'int'>


