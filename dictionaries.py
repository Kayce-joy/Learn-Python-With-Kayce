"""
. Dictionaries:
A dictionary is like a collection of key-value pairs. Each value is associated with a
unique key. You can use the key to access the value.
"""

person = {"name": "Alice", "age": 25}
print(person["name"]) 




# Creating a dictionary
student = {
    "name": "Alice",
    "age": 20,
    "grade": "A"
}

# Accessing values using keys
print(student["name"])  # Output: Alice
print(student["age"])   # Output: 20

# Adding a new key-value pair
student["city"] = "Nairobi"
print(student)  
# Output: {'name': 'Alice', 'age': 20, 'grade': 'A', 'city': 'Nairobi'}

# Updating a value
student["grade"] = "A+"

# Removing a key-value pair
del student["age"]

print(student)  
# Output: {'name': 'Alice', 'grade': 'A+', 'city': 'Nairobi'}
