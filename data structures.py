

                                                # lists


age = 24
has_license = True

fruits = ["apple", "banana", "cherry"]
numbers = [3,1,4,1,5,9]
mixed = ["Vinit", 24, age, has_license, 3.14, True]

# Accessing elements in a list
print(fruits[0])  # first element in the list
print(fruits[-1]) # last element in the list

# slicing
print(fruits[0:2])  # first two elements
print(fruits[1:3])  # second and third elements
print(fruits[:2])   # first two elements
print(fruits[1:])   # all elements from the second to the end

# change an item
fruits[0] = "mango"      # change the first item in the list
fruits.append("orange")  # add an item to the end of the list
fruits.remove("banana")  # remove an item from the list
fruits.insert(1, "kiwi") # add an item at a specific index
last = fruits.pop()      # remove and return the last item in the list
last
fruits.sort()         # sort the list in ascending order
fruits.reverse()      # reverse the order of the list
del fruits[0]         # delete the first item in the list

# information
print(len(numbers))      # length of the list
print(min(numbers))      # minimum value in the list
print(max(numbers))      # maximum value in the list\
print(sum(numbers))      # sum of all values in the list
print(numbers.count(1))  # 2 (how many times no. 1 has occured in the list)
print(numbers.index(4))  # 2 (at what index the number 4 is present in the list)

# Sorting
numbers.sort()              # Sort in place
print(numbers)              # [1, 1, 3, 4, 5, 9]

numbers.reverse()           # Reverse order
print(numbers)              # [9, 5, 4, 3, 1, 1]

# Copy
new_list = numbers.copy()   # Create a copy

# Check if item exists
if "apple" in fruits:
    print("Found apple!")

# Check if list is empty
if fruits:
    print("List has items")
else:
    print("List is empty")


                                                # Dictionaries

person = {
    "name": "Vinit",
    "age": 24,
    "has_license": True
}

# another way to create a dictionary
person = dict(name="Vinit", age=24, has_license=True)  # mostly used when no spaces or spl characters in the keys are required or converting other data types to dictionary

person["age"]                 # access value by key
person["age"] = 25            # change value by key
person["city"] = "Kopargaon"  # add new key-value pair
del person["has_license"]     # delete key-value pair
age = person.pop("age")       # Remove and return
person.clear()                # Remove all items

# Get all keys, values, or items
print(person.keys())    # dict_keys(['name', 'age', 'city'])
print(person.values())  # dict_values(['Alice', 30, 'New York'])
print(person.items())   # dict_items([('name', 'Alice'), ...])

# Check if key exists
if "name" in person:
    print("Name found!")

# Update multiple values
person.update({"age": 31, "job": "Engineer"})

# Dictionary of dictionaries
students = {
    "alice": {"age": 20, "grade": "A"},
    "bob": {"age": 21, "grade": "B"},
    "charlie": {"age": 19, "grade": "A"}
}

# Access nested data
print(students["alice"]["grade"])  # "A"


                                                # Tuples


# Empty tuple
empty = ()

# Tuple with items
point = (3, 5)
colors = ("red", "green", "blue")

# Single item tuple needs comma!
single = (42,)    # Note the comma
not_tuple = (42)  # This is just 42 in parentheses

# Without parentheses (implicit)
coordinates = 10, 20

# Get items
print(point[0])      # 3
print(colors[-1])    # "blue"

# Slicing works too
print(colors[0:2])   # ("red", "green")

# Unpack values
point = (3, 5)
x, y = point  # x = 3, y = 5

# Multiple assignment
a, b, c = 1, 2, 3  # Same as (1, 2, 3)

# Swap variables elegantly
x, y = y, x  # Swaps values!


                                                # Sets


# Empty set
empty_set = set()  # NOT {} - that's a dict!

# Set with values - both ways work
numbers = {1, 2, 3, 4, 5}
fruits = set(["apple", "banana", "orange", "banana"])  # Duplicates are removed

# From a list (removes duplicates)
scores = [85, 90, 85, 92, 90]
unique_scores = set(scores)  # {85, 90, 92}

# Add items
fruits.add("kiwi")
print(fruits)

# Remove items
fruits.remove("kiwi")    # Error if not found
fruits.discard("kiwi") # No error if not found

# Check membership
if "kiwi" in fruits:
    print("Kiwi is available")
else:
    print("Kiwi is not available")