#datatypes in python..data defines the size of a memory(helps in managing memory)
#numeric type
#string
#sequence
#mapping
#boolean
#set

#Numeric:we have integers (int), floats (float), and complex numbers(complex)
#examples:
num1 = 10
print(num1, 'is of a type', type(num1))
num10 = 5.0
print(num10, 'is of a type', type(num10))
num11 = 1+2j
print(num11, 'is of a type', type(num11))
# num12 =1+2l
print(num1, 'is of a type', type(num1)) 

#strings
#a string is a group of characters
name = 'Akech' 
print(name, 'is of a type', type(name))
#semantics is the meaning of what you have written
#typecasting is changing the data type of a variable value
#example 0f typecasting
numx = '20'
print(numx, 'is of a type', type(numx))
numy = int(numx)#conversion of the value of numx into integer and store it in a variable numy
print(numy, 'is of a type', type(numy))
numy = str(numx)
print(numy, 'is of a type', type(numy))
numy = float(numx)
print(numy, 'is of a type', type(numy))
#sequence data type
#under sequence, we have lists, tuples, and range
#a list is a variable that can store more than one value
#However we can have an empty variable list and we can store values later on
myList = []# how to declear a list
myList.append('Akech')#append is a specialized command that is used to add values to a list
print(myList)#to rmove an append use popattribute

myList.append(15)# appends or adds the next value to the list
print(myList)
Languages = ['python', 'javascript', 'c', 'c++', 'swift', 'julia', 'ruby', 'cobol']
print(Languages[5])
print(Languages[3])
print(Languages[0])
print(Languages[2], Languages[1])
print(Languages[-8])

country = ['Uganda', 'Kenya', 'Tanzania', ['Egypt', 'Somalia', ['Sudan']]]
print(country[3][2])
print(country[-1][-1])
print(country[3][2][0])
print(country[-1][-1][-1])
#assignment
country = ['Uganda', 'Kenya', 'Tanzania', ['Egypt', 'Somalia', ['Sudan', ['Burundi']]]]
print(country[3][2][1][0])
print(country[-1][-1][-1][-1])
#dictionary is a combination of key and value
#mapping is identified by dictionary data type
uganda={"name":"Uganda", "popn":"45", "location":"E.A"}
print(type(uganda))
print(uganda.keys())
print(uganda.values())
#sets are unordered collections of unique values
student_id={100,200,200}
print(student_id)
my_numbers = {10,20,30,40,50}
print(my_numbers)

fruits = ['apples', 'mangos', 'oranges',['pawpaws', 'pears']]
print(fruits[0])
print(fruits[3][0])
fruits.append('pineapple')
print(fruits)


cakes = ['butter cake', 'fruit cake', 'opera cake', 'chocolate cake']
print(cakes[3])
print(cakes[-1])

cakes = [['butter cake', 'fruit cake', 'opera cake', 'chocolate cake'], 'Red velvet cake', 'sponge cake',['vanilla cake']]
print(cakes[2]) 
print(cakes[-2])