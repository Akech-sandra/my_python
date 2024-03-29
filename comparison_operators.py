#compares 2 values and returns a true or false
#Boolean responds with either a true or false
com1 = 100
com2 = 'akesandra'
print(com1==com2)
# == create a comparison operator
# = to assign
# != not equal to
print(com1 != com2)
# <> less than or greater than
num1 = 100
num2 = 50
print(num1 < num2)
print(num1 > num2)
# <= and >= greater than or equal to
print(num2 <= num1)
print(num2 >= num1)

#logical AND
print(True and True)
print(True and False)

#logical OR
print(True or True)
print(True or False)

#logical NOT
print( not True)
print(not False)

#logical MEMBERSHIP
myList = [10, 20, 30]
#checking if a given value is in the provided list 
print(10 in myList)
print(50 in myList)

print(80 not in myList)

#identity operators
myList1 = [10, 20, 30]
print(myList is not myList1)
print(myList is myList1)

myList2 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(myList is not myList2)

#assignment, read about bit-wise operator   
#a value in programing is called an operand
# an operator acts upon an operand
# a loop is an instruction that enables a computer to repeatedly perform a task
#loop tells the computer to continue untill a certain condition is met
#loops & conditions