#create a file, call it mypython.py within it, write comments that reflect whatever that you have learnt from the python class since day one using examples if any.

# I got to know that programming is the art and science of writing computer instructions
#HTML Hypertext Markup Language (hypertext are text links that link to webpages), this is an interpreted language
#CSS Cascading stylesheet (ehances the appearance of a web page)
#css and html are the backbone of webpages.

#memories of a computer; the main memory-Primary(internal memory of a computer) and secondary memory (external memory of a computer) 
#Hard disk drive is read and written using electro magnetic fields(this is a primary memory storage device)
#DVD/CD is read and written using light(this is a secondary memory storage device)
#flash information is got using copying method(this is a secondary memory storage device)

#Cache stores frequently opened files
#RAM is Random Access Memory. it is a temporarily brain of the computer.
#when a computer is off, the Ram is empty. when a computer is on, the Ram keeps the reference to the opened files so that the cpu can work on them
#Buffer stores temporary data which is being modified or active
#the cpu manages computer memory but can not directly communicate with the computer memory without the RAM
#I saw the structure of a hard disk and learnt how it works.
#when a hard disk is new, it is partitioned to effectively manage stored content in an organized way
#each partition or stored content has a unique id which is its memory address
#the RAM loads the memory address in use to the cpu when that particular file is opened
#a memory address is a physical address of an id in a hard disk drive
#ROM Read Only Memory never parmanetly stores data

#C is the mother of all languages, a 1st generation language and javascript is a compiled language
#python is a 4th generation language, it is interpreted and easy to understand by humans
#formally python was called AB language before being named python, a name inspired by the monte python comedy show.
# The rules that govern the use of programming languages is called syntax
#a statement is a complete instruction to a computer
#2 or more statements makes a code

# use the # symbol to write a comment in python
#a variable is a name given to a memory space
#print is a specialized command used to output values on a screen
#variable names should not start with special characters(e.g #,$,@,%,*--num=10)
#variable names should not start with a numerical digit. (e.g 7num, 2num is invalid but num7 or num2 is valid
#a variable name should not have spaces, use underscore or use camel-case method (e.g my age is invalid but my_age,myAge is correct)
#names should not start with capital letters unless they are functional or classes(My_age or MyAge is invalid)
#use relatable names(e.g when dealing with customer use myCustomer)
#use short, simple, relatable names(e.g num instead of number)
#variable names should not be repeated in different forms because python is case sensitive(Name and name are different)

#example
# age=26
# myName='Sandra'   anything in quoted is a string
# print(age)
# print(myName)

#datatypes in python..data defines the size of a memory(helps in managing memory)
#examples of data types in python
#numeric type
#string
#sequence
#mapping
#boolean
#set

#Numeric datatype include integers (int), floats (float), and complex numbers(complex)
#examples
#10 is an integer and 10.0 is a float
#to check for a data type of a given value use num10 = 5.0 print(num10, 'is of a type', type(num10))

#string datatype
#a string is a group of characters, e.g name = 'Akech' or name = "Akech"

#sequence data type include lists, tuples, and range
#a list is a variable that can store more than one value
#However we can have an empty variable list and can store values in later on
#myList = [] how to declear a list. This is an empty list
#e.g a list; cakes = [['butter cake', 'fruit cake', 'opera cake', 'chocolate cake'], 'Red velvet cake', 'sponge cake',['vanilla cake']]
#indexing of the values in the list starts from 0
#to display chocolate cake on the screen instruct the computer to print(cakes[3]) or print(cakes[-1])
#to display sponge cake on the screen instruct the computer to print(cakes[2]) or print(cakes[-2])
#myList.append('Akech') append is a specialized command that is used to add values to a list
#print(myList) to remove an append use pop attribute

#dictionary is a combination of key and value
#mapping is identified by dictionary data type
# uganda={"name":"Uganda", "popn":"45", "location":"E.A"}
# print(type(uganda))
# print(uganda.keys())
# print(uganda.values())

# #sets are unordered collections of unique values e.g
# student_id={100,200,200}
# print(student_id)

#operators tell a computer to do something with the a variable value
# myName = "Sanny"
#operators symbols and their meaning
#arithmetic operators perform arithmetic operations on numbers e.g + adds, - subtracts, * multiplies, / divides

#addition
#sum = num1 + num2

#subtraction
#sub = num1 - num2

#division 
#div = num1 / num2

#multiplication 
#multi= num1 * num2

#modulus (%) returns the remainder got by dividing 2 values
#mod = num1 % num2

#floor division(changes a value from a float to an integer )
#fl_div = num2 // num1

#assignment operators is used to give value to a variable
#addition assignment operator e.g num1 += 2 this is same as num1 = num1 + 2

#subtraction assignment operator num1 -= 2 e.g num1 -= 2 this is same as num1 = num1 - 2

#division assignment operator num1 /= 2 e.g num1 /= 2 this is same as num1 = num1 / 2

#multiplication assignment operator num1 *= 2 e.g num1 *= 2 this is same as num1 = num1*+ 2

#modulus assignment operator num1 %= 2 e.g num1 %= 2 this is same as num1 = num1 % 2

#"solve a lot of problems if you want to be a good problem solver"