# June 06-06-2022
# Python Basics 


addition = 55 + 65
print(addition)

subtraction = 88 - 48

print(subtraction)

multiplication = 15 * 12

print(multiplication)

division = 58 / 10

print(division)
# String is also immutable data_Types
string = 'Ranjith'

print(string)
# Mutable data Type----List:
variable = [12, 21, 43, 34]

print(variable)
 
variable_demo = True

print(variable_demo)

another_demo = False

print(another_demo)
# Immutable data Type----Tuple:
tuple_demo = (2, 3)

print(tuple_demo)

dictionary_demo = {
    "Key1" : "value1",
    "Key2" : "value2",
    "Key3" : "value3",
    "Key4" : "value4"
}

print(dictionary_demo['Key1'])
print(dictionary_demo['Key3'])

# Mutable data Type----Set:
set_demo = {1,1,1,1,1,12,2,2,2,3,3,3,4,4,4,5,5,5}

print(set_demo)

# forzenset is a immutable set

a = 3 + 7j
b = 8 + 9j

print(a+b)

# Type casting 

a = 34
b = 35.4
c = 2 + 5j

m = float(a) #Covert from int to float
n = complex(a) #Convert from int to complex
o = int(b) #Convert from float to int
p = complex(b) #Convert from float to complex
print(m,n,o,p, end= ' ')

string = 'Water_Bottle'
print(string.replace("_","."))