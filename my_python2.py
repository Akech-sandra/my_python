#  a statement is an instruction that commands the computer to do something
#  a code is a statement identified by :
#  block of code is identified by indentation 
#  a block of code is a collection of related statements and performs specific tasks
#  a named block of code(group of statements) is called a function

# this is a block of code
"""
for i in range(1,20):
   if i % 2 == 1:
       print(i)
"""        
 
# a loop is an instruction that repeatedly(iterate or continue) does an activity until a certain condition is met or fulfilled
# for loop and while loops are used in python
#A for loop repeatedly executes a block of code a specific number of times. 
#The basic syntax of a for loop typically includes;
#1. Initialization: Setting the initial value of a variable (the loop variable).
#2. Condition: Specifying a condition that, when true, allows the loop to continue.
#3. Iteration: Updating the loop variable after each iteration.
#e.g below, range(5) generates a sequence of numbers from 0 to 4 which the loop iterates over:   
# On each iteration, the loop variable `i` takes the next value in the sequence, and the `print(i)` statement prints out its values.
"""
for i in range(5):
   print(i)
"""

#a while loop repeatedly executes a block of code as long as a specified condition remains true
#If the condition is true, the code block inside the loop is executed. If the condition is false, the loop is exited
#e.g below, i is initially set to 0. The while i < 5: condition checks if i is less than 5. 
# If it is true, the loop body is executed, which prints the current value of i and then increments i by 1 using the i += 1 statement. 
# This process continues until i is no longer less than 5
"""
i = 0
while i < 5:
    print(i)
    i += 1
"""

#break allows you to exit a loop when an external condition is met.
# break is used to exit the loop prematurely e.g below
"""
for i in range(5):
    if i == 3:
       break
    print(i)
"""

#continue is used within loops to skip the rest of the code inside the loop for the current iteration and continue to the next iteration.
#it allows you to skip certain iterations of a loop based on a condition, without exiting the loop entirely. e.g below
"""
for i in range(5):
    if i == 2:
        continue
    print(i)
"""    

# def--->definition
# functions are defined, anything indented is a function definition
# a function is identified by the key word def followed by function name and parentheses then statements e.g below
"""
def myfunction():
     num1, num2 = 20, 40
     print(num1 + num2)
myfunction()
"""

# running a file is to execute
# the calling of a function is to invoke
#dont create more than one function with the same name within the same py file

# there are 2 types of functions
#  a static function has an empty parenthesis e.g below
"""
def add():
    num1, num2 = 20, 40
    sum = num1 + num2
    print(sum)
add()
"""
#  a dynamic function has parameters(num1, num2) inside its parenthesis. e.g below
"""
def sub1(num1, num2):
    sub = num1 - num2
    print(sub)
sub1(96,60)  
"""
#the values passed during the invokation are called arguments e.g (96,60) 

#return is the last statement to be executed in a function, it marks the end of a function   
#return shares, gives back or lets access to a function
#return makes functions communicate with one another
#functions are independent of the other
#functions are self contained block of codes because variables cant be accessed out of the function
#a local variable can not be accessed outside of the function
#a global variable is outside the function but can be accessed within the function e.g below age = 25 is a global variable
"""
age = 25
def add2(a,b):
    ans = a+b + age
    print(ans)
add2(20, 20) 
"""