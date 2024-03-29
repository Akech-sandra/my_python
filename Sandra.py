# a variable some_string is assigned string value of Python is fun
some_string = 'Python is fun' 
# variable a holds an integer data type value of 5, b holds a float data type of 3.2 and c holds a string data type of Hello 
a, b, c = 5, 3.2, 'Hello'

print(a)  # 5
print(b)  # 3.2
print(c)  # Hello

#a variable num1 is assigned an integer value of 5
num1 = 5
#output the value of num1,'is of type',indicates the data type of num1 as an integer (int)
print(num1, 'is of type', type(num1))
#a variable num2 is assigned a float value of 2.0
num2 = 2.0
#output the value of num2, 'is of type', indicates the data type of num2 as a float
print(num2, 'is of type', type(num2))
#a variable num3 is assigned a complex number value 1+2j. 
num3 = 1+2j
#output the value of num3, 'is of type', indicates the data type of num3 as a complex number
print(num3, 'is of type', type(num3))
#a list called languages containing three strings: "Swift", "Java", and "Python". 
languages = ["Swift", "Java", "Python"]

# output the first element of the languages list.
print(languages[0])   # display Swift on the screen

# output the third element of the languages list
print(languages[2])   # display Python on the screen

# a tuple named product containing three elements: a string 'Microsoft', a string 'Xbox', and a float 499.99.
product = ('Microsoft', 'Xbox', 499.99)

# output the first element of the product tuple.
print(product[0])   # Microsoft

# output the second element of the product tuple.
print(product[1])   # Xbox


# a dictionary with keys and values. Each key-value pair represents a country and its capital city
capital_city = {'Nepal': 'Kathmandu', 'Italy': 'Rome', 'England': 'London'}
# display all key-value pairs in the dictionary
print(capital_city)


# a set named student_id containing unordered collections of unique elements
student_id = {112, 114, 116, 118, 115}

#  display all unique elements in the set
print(student_id)

# output the type of student_id variable
print(type(student_id))

# a list named fruits containing three strings: "apple", "mango", and "orange"
fruits = ["apple", "mango", "orange"] 
#display all elements in the fruits list
print(fruits)

# a tuple named numbers containing three elements: 1, 2, and 3
numbers = (1, 2, 3) 
# display all elements in the numbers tuple
print(numbers)

# a dictionary named alphabets with keys and values
alphabets = {'a':'apple', 'b':'ball', 'c':'cat'} 
#display all key-value pairs in the alphabets dictionary
print(alphabets)

#a set named vowels containing five elements: 'a', 'e', 'i', 'o', and 'u' and then display all unique elements in the set
vowels = {'a', 'e', 'i' , 'o', 'u'} 
print(vowels) 


# a set named student_id containing five elements: 112, 114, 116, 118, and 115
student_id = {112, 114, 116, 118, 115}

#  display all unique elements in the student_id set
print(student_id)

# display type of student_id
print(type(student_id))
#  a tuple named product containing three elements: the string 'Microsoft', the string 'Xbox', and the float 499.99.
product = ('Microsoft', 'Xbox', 499.99)

#output the first element of the product tuple
print(product[0])   # Microsoft

# output the second element of the product tuple
print(product[1])   # Xbox




#assigns the value 7 to the variable a and the value 2 to the variable b
a = 7
b = 2

# output the sum of the variable values of a and b
print ('Sum: ', a + b)  

# output the subtracted value from subtracting b from a
print ('Subtraction: ', a - b)   

# output the multiplied value from multiplying a and b
print ('Multiplication: ', a * b)  

# output the divided value after dividing a by b
print ('Division: ', a / b) 

# output an integer value from floor division of a by b
print ('Floor Division: ', a // b)

# output the reminder of the modulo operation of a by b.
print ('Modulo: ', a % b)  

# output the exponential value of raising a to the power of b
print ('Power: ', a ** b)   


# assign a value 10 to the variable a
a = 10

# assign a value 5 to the variable b
b = 5 

# sum up a and b and then assign the sum to a to output the new value of a
a += b      # a = a + b
print(a)
# Output: 15


# checks if a and b are equal and outputs the respective boolean value of the comparison.
print('a == b =', a == b)

#checks if a and b are not equal then outputs the respective boolean value of the comparison.
print('a != b =', a != b)

# checks if a is greater than b then outputs the respective boolean value of the comparison
print('a > b =', a > b)

# checks if a is less than b then outputs the respective boolean value of the comparison
print('a < b =', a < b)

# checks if a is greater than or equal to b then outputs the respective boolean value of the comparison
print('a >= b =', a >= b)

# checks if a is less than or equal to b then outputs the respective boolean value of the comparison
print('a <= b =', a <= b)
#the and logical operator combines two conditions then outputs the respective boolean value of the operation.
print((a > 2) and (b >= 6)) 

# logical AND operator 
print(True and True)     # True
print(True and False)    # False

# logical OR
print(True or False)     # True

# logical not operation
print(not True)          # False

# variables assigned values, x1 and y1 assigned the integer 5, x2 and y2 assigned string 'Hello', x3 and y3 assigned lists [1, 2, 3]
x1 = 5
y1 = 5
x2 = 'Hello'
y2 = 'Hello'
x3 = [1,2,3]
y3 = [1,2,3]
#is not operator checks if x1 is not the same as y1 and prints a cooresponding boolean value
print(x1 is not y1)  # False
#is operator checks if x2 is the same object as y2 and prints a respective boolean value
print(x2 is y2)  # True
#is operator to check if x3 is the same as y3 and prints a respective boolean value
print(x3 is y3)  # False
# assign the string 'Hello world' to the variable named message
message = 'Hello world'
#a dictionary named dict1 assigned two key-value pairs
dict1 = {1:'a', 2:'b'}
# checks if the character 'H' is a member in the string 'Hello world' and print the respective boolean value
print('H' in message)  # True

# check if the string 'hello' is not a member in the string 'Hello world' and print the respective boolean value
print('hello' not in message)  # True

# check if 1 is a member in the dictionary dict1 and printzs the respective boolean value
print(1 in dict1)  # True

# check if 'a' is a member in the dictionary dict1 and print the cooresponding boolean value
print('a' in dict1)  # False