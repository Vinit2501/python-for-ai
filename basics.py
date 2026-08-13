name = "Vinit"
print(name)
Age = 24
Age
10 + 5
10 - 5
10 * 5
10 / 5
10 ** 5
Addition = 10 + 5
Addition

string = "My name is Vinit"

long_string = """
This is a long string that spans multiple lines.
It can be used to include line breaks and other formatting in the string.
"""
print(long_string)

first_name = "Vinit"
last_name = "Kurhade"

full_name = first_name + " " + last_name
print(full_name)

full_name = first_name + ' ' + last_name
full_name

long_dash = "-" * 15

print(full_name)
print(long_dash)

len(full_name)
len(long_dash)

Age = 16
checking = Age == 16

age = 25
has_license = True

# and - both must be true
can_drive = age >= 16 and has_license
print(can_drive)

# or - at least one must be true
can_drive = age >= 16 or has_license
print(can_drive)

# not - reverses the boolean value
can_drive = not has_license
print(can_drive)

drunk = False
can_drive = age >= 16 and has_license and not drunk
print(can_drive)

score = 10
score = score + 5
score += 5

# Using +
full_name = first_name + " " + last_name  # "Jane Doe"

# Using f-strings (modern Python way!)
greeting = f"Hello, {first_name}!"  # "Hello, Jane!"

# Multiple variables
age = 25
intro = f"I'm {first_name} and I'm {age} years old"

first_name.lower()
first_name.upper()
first_name.title()

string.title()
long_string.title()

"Breaks" in long_string
"breaks" in long_string

new_long_string = long_string.replace("line breaks", "new lines")
long_string
long_string.replace("line breaks", "new lines")
print(long_string)
string.replace("Vinit", "John")
print(string)

# if else statements

temperature = 31

if temperature > 30:
    print("It's a very hot day")
elif temperature > 25:
    print("It's a hot day")
elif temperature > 20:
    print("It's a nice day")
else:
    print("It's not a hot day")

# multiple conditions

age = 25
has_license = True

if age >= 18 and has_license:   # Both must be True
    print("You can drive!")

if age >= 26 or not has_license:          # At least one must be True
    print("It's okay to drive but you should be careful.")

raining = True
if not raining:                 # Reverse the condition
    print("Let's go outside!")
else:
    print("Better stay inside.")


# nested if statements

has_ticket = False
age = 17

if has_ticket:
    if age >= 18:
        print("You can enter the concert!")
    else:
        print("You cannot enter the concert. You are underage.")
else:
    print("You cannot enter the concert. You don't have a ticket." \
    "Please buy a ticket first.")

# loops (in python the counts start from 0)

for age in range(5):
    print(f"{age}")

# Option 1: Modify age
age = 17
for i in range(5):
    print(f"{age}")
    age += 1  # Now prints 17, 18, 19, 20, 21

# Option 3: Use both
age = 17
for i in range(5):
    print(f"{age + i}")

# count from 1-5

for i in range(1, 6):
    print(i)

# count by 2's

for i in range(0,10,2):
    print(i)

# loop through text

name = "Python"
for letter in name:
    print(letter)

for letter in first_name:
    print(letter)

# loop through a list

colors = ["red", "blue", "green"]
for color in colors:
    print(f"I like {color}, which is a beautiful color.")



