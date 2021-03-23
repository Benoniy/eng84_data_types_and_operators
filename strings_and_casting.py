""" Strings and Casting """


# Industry practises
# Single and double quotes work the same
single_quotes = 'single quotes'
double_quotes = "double quotes"
print(single_quotes)
print(double_quotes)

# Escaping quotes
escape_quotes = 'The boy said \'wow\''


# String Slicing
greetings = "Hello World"
# Indexing starts from 0
# Simple
# H e l l o   W o r l d
# 0 1 2 3 4 5 6 7 8 9 10
print(greetings[0:5])

# Reverse
#   H   e  l  l  o     W  o  r  l  d
# -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
print(greetings[-1])


# String Methods
# len() - total length of a string
print(len(greetings))

# strip() - removes all whitespaces
print(greetings.strip())

# count() - counts the number of substrings in a string
print(greetings.count("l"))

# upper() - makes a string upper case
print(greetings.upper())

# lower() - makes a string lower case
print(greetings.lower())

# capitalize() - Capitalizes the first letter of a string
print(greetings.capitalize())

# replace() - Replaces a substring within a string with another substring
print(greetings.replace("Hello", "World"))


# Concatenation and casting
first_name = "Elon"
last_name = "Musk"
age = 50
wage = 10.9

# To concatenate you can use + or ,
print(first_name, last_name)  # However this automatically converts the arguments to strings
print(first_name + " " + last_name)

# str() - casts an object to a string
print(str(age))

# int() - casts an object to an int it will always round down a float
print(int(wage))

# float() - casts an object to a float
print(float(age))
