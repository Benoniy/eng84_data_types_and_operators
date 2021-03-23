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
