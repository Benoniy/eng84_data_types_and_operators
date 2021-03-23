# Introduction to Data Types and Operators  


## Operators
### Arithmetic Operators  
  ***These can be used to perform mathmatical operations on ints, floats and longs.***
* Addition  
  `print(a+b)`
* Subtraction  
  `print(a-b)`
* Division  
  `print(a/b)`
* Multiplication  
  `print(a*b)`
* Modulus  
  `print(a%b)`  

### Comparison Operators  
  ***These can be used to compare two more values and return a boolean.***  
* Equal to  
  `print(a==b)`  
* Not Equal to  
  `print(a!=b)`  
* Greater than  
  `print(a>b)`  
* Less than  
  `print(a<b)`  
* Greater than or Equal to  
  `print(a>=b)`  
* Less than or Equal to  
  `print(a<=b)`  
  
## Strings and Casting  
### Single or double quotes?  
  ***Both single quotes and double quotes can be used to define a string, which one is used is often defined***  
  ***by the specific situation and the developer's preference.***  
* Single quotes  
  `greeting = 'Hello World'`
* Double quotes  
  `greeting = "Hello World"`
* In some cases you may have to "escape" these characters to use them in a string, to do this use \\.  
  `example = 'The boy said \'wow\''`  
### String Slicing  
  ***String slicing is a useful method for extracting substrings from a main string***  
* Simple slice - In a simple slice you specify the start point and the end point in this format (the end point is not included)
```python
greetings = "Hello World"
# Indexing starts from 0
# H e l l o   W o r l d
# 0 1 2 3 4 5 6 7 8 9 10
print(greetings[0:5])
```  
* Reverse Slice - A reverse slice works in much the same way as a simple slice but simply reverses the indexing
```python
greetings = "Hello World"
#   H   e  l  l  o     W  o  r  l  d
# -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
print(greetings[-1])
```  

### String Methods  
  ***These methods can be used to manipulate a string or identify information about it***  
* len() - returns the total length of a string  
  `print(len(greetings))`  
* .count() - counts the number of substrings in a string  
  `print(greetings.count("l"))`  
* .strip() - removes all the whitespaces from a string  
  `print(greetings.strip())`  
* .upper() - makes a string upper case  
  `print(greetings.upper())`  
* .lower() - makes a string lower case  
  `print(greetings.lower())`  
* .capitalize() - Capitalizes the first letter of a string  
  `print(greetings.capitalize())`  
* .replace() - Replaces a substring within a string with another substring  
  `print(greetings.replace("Hello", "World"))`  

### Concatenation  
  ***Concatenation is used to combine strings for convenience***
* Using +  
`print(first_name + " " + last_name)`
  
### Casting  
  ***Casting can be used to explicitly convert data to a specific data type, this will throw an error if provided incorrect data***  
* str() - Converts the data provided into a string  
  `print(str(age))`
* int() - Converts the data provided into an integer  
  `print(int(wage))`
* float() - Converts the data provided into a float  
  `print(float(wage))`

### Format string  
  ***f can be used as an argument to indicate that you are formatting string, this is useful for inserting variables into a string***  
  ***in a simple and effective manner***  
```python
first_name = "Elon"
last_name = "Musk"
age = 50
print(f"first name: {first_name},  Last name: {last_name}, Age: {age}")
print(f"{first_name=},  {last_name=}, {age=}")
```

