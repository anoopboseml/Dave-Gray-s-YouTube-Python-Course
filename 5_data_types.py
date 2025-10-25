import math

# Data Types

# String Data Type

# Literal Assignment


first = "Anoop"  # this is literal assignment

last = "Bose"

# print(type(first))
# print(type(first) == str)
# print(isinstance(first, str))  # isinstance is a built-in python function
# it checks whether a variable is of a particular data type

# another way to assign a value is with a constructor function

# Constructor Function

# pizza = str("Pepperoni")
# print(pizza)
# print(type(pizza))
# print(type(pizza) == str)
# print(isinstance(pizza, str))

#################################################

# CONCATENATION
fullname = first + " " + last

print(fullname)

fullname += "!"

print(fullname)

###########################################################

# CASTING (Converting one data type to another)

decade = str(1980)
print(type(decade))
print(decade)

statement = "I like rock music from the " + decade + "s."
print(statement)


# Multiple lines

multiline = '''
Hey, how are you?

I was just checking in.                                                           
                                All good?  
                                
'''

print(multiline)

# Escaping special characters (ALL special characters can be escaped by prefixing \)
# \t for tab and \n for new line

sentence = 'I\'m back at work!\tHey!\n\nWhere\'s this at\\ located?'
print(sentence)

############################################################

# STRING METHODS

print(first)
print(first.lower())
print(first.upper())
print(first)
# note that the above string methods do not effect the value stored in the variable "first"

print(multiline)
print(multiline.title())
# what happens if replace can not find the word in the first arg?
print(multiline.replace("good", "ok"))
print(multiline)


print(len(multiline))
multiline += "                                                                    "
multiline = "                                         " + multiline
print(len(multiline))

# string methods that remove unnecessary whitespaces

# there are 3 primary methods to remove whitespaces
test_str = "My name is \tAnoop. I\'m from India! \nHow about you? \n                                          "
print(test_str)
print(len(test_str))
print(len(test_str.strip()))
print(len(test_str.lstrip()))
print(len(test_str.rstrip()))


print(" ")


# Build a menu
# Note that str methods can be called directly on the string values as well

title = "menu".upper()
print(title.center(20, "="))

print("Coffee".ljust(16, ".") + "$1".rjust(4))
print("Muffin".ljust(16, ".") + "$2".rjust(4))
print("Cheesecake".ljust(16, ".") + "$3".rjust(4))


#####################################################################
# STRING INDEX VALUES
print(first[0])  # value at index 0
print(first[-1])  # value at index -1
print(first[1:-1])  # range of values starting at index 1 and ending at -1
print(first[1:])  # range of values from index 1 to end of the string

######################################################################
# SOME METHODS RETURN BOOLEAN DATA
print(first.endswith("p"))
print(first.startswith("A"))


####################################################################
# BOOLEAN DATA TYPE
myvalue = True
x = bool(False)  # this is a constructor function

print(type(x))
print(isinstance(x, bool))

#####################################################################
# NUMERIC DATA TYPES (because there are more than 1 numeric data type)

# INTEGER
price = 100
best_price = int(80)
print(type(price))
print(isinstance(best_price, int))

# FLOAT (numbers with decimals (example 1.010))
gpa = 3.28
y = float(1.14)
print(type(gpa))
print(isinstance(gpa, float))

# COMPLEX TYPE
comp_value = 5+3j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)


# BUILT IN FUNCTIONS FOR NUMBERS
print(abs(gpa))  # absolute value


print(round(gpa))  # this will round to the nearest integer

# this will round to the nearest decimal with the precision that we specify
print(round(gpa, 1))


##########################################################################################
# We can utilize a lot more math functionalities with the MATH module
# we need to import it first

print(math.pi)
print(math.sqrt(64))
print(math.ceil(gpa))
print(math.floor(gpa))


# CASTING A STRING TO A NUMBER
zipcode = "110001"
print(zipcode)
zip_val = int(zipcode)
print(zip_val)
print(type(zip_val))

# We will get ERROR if we attempt to cast incorrect data
# zip_value = int("Delhi")
