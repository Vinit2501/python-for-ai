def say_goodbye():
    print("Goodbye!")
    print("See you later!")

# Call it multiple times
say_goodbye()
say_goodbye()
say_goodbye()

# Good names
def calculate_total():
    pass

def send_email():
    pass

def validate_password():
    pass

# Bad names
def func1():  # Not descriptive
    pass

def Calculate():  # Should be lowercase
    pass

# functions without parameters/logic
def check_weather():
    temperature = 25
    if temperature > 30:
        print("It's hot!")
    else:
        print("Nice weather!")

# Use the function
check_weather()

# Function with parameters
def check_weather_with_temp(temperature):
    if temperature > 30:
        print("It's hot!")
    else:
        print("Nice weather!")

check_weather_with_temp(35)
check_weather_with_temp(20)

def greet_user(name):
    print(f"Hello, {name}!")

greet_user(name="Alice")
greet_user("Bob")


# local variables
def calculate_price():
    price = 100
    tax = price * 0.1
    print(f"Total: {price + tax}")

calculate_price()  # Total: 110

# This fails - price doesn't exist outside the function
# if we print "print(price)" --- NameError: name 'price' is not defined

# global variables
discount_rate = 0.15  # Global variable

def apply_discount(price):
    discount = price * discount_rate  # Can read global variable
    return price - discount

result = apply_discount(100)
print(result)  # 85.0



# global variable modification
counter = 0  # Global variable

def increment():
    global counter  # Declare we want to modify the global variable
    counter += 1

increment()
increment()
increment()
print(counter)  # 3



# Bad - using global variable
total = 0

def add_to_total(amount):
    global total
    total += amount

# Good - using parameters and return
def add_amounts(current_total, amount):
    return current_total + amount

total = 0
total = add_amounts(total, 10)
total = add_amounts(total, 20)
print(total)  # 30


# returning values
def add_print(a, b):
    print(a + b)

result = add_print(3, 4)  # Prints 7 but returns None
print(result)

def add_return(a, b):
    return a + b

result = add_return(b=4, a=4)
print(result + 5)

# Use return to send a value back from a function:
def calculate_area(width, height):
    area = width * height
    area_margin = area * 0.1  # Add 10% margin
    return area + area_margin

# Store the returned value
room_area = calculate_area(10, 12)
print(f"Room size: {room_area} sq ft")  # Room size: 132 sq ft



# returned values can be use in many ways
def double(number):
    return number * 2

# Store in variable
print(f"Result: {double(5)}")

# Use in expressions
print(f"Total: {double(5) + double(3)}")  # 10 + 6 = 16

# Pass to other functions
print(f"{double(10)}")  # 20

# Use in conditions
if double(7) > 10:
    print("Big number!")


# Python can return multiple values as a tuple:
def get_min_max(numbers):
    return min(numbers), max(numbers)

# Get both values
minimum, maximum = get_min_max([5, 2, 8, 1, 9])
print(f"Min: {minimum}, Max: {maximum}")  # Min: 1, Max: 9

# Or as a tuple
result = get_min_max([5, 2, 8, 1, 9])
print(result)


# difference between return and print
def get_greeting_print(name):
    print(f"Hello, {name}!")  # Just displays

def get_greeting_return(name):
    return f"Hello, {name}!"  # Gives back value

# Can't use print version's output
message = get_greeting_print("Alice")  # Prints but returns None
print(message)  # None

# Can use return version's output
message = get_greeting_return("Alice")  # Returns the string
print(message.title())  # Hello, Alice!
