#  a statement is an instruction that commands the computer to do somthing
#  a code is a statement identified by :
#  a block of code is a collection of related statements and performs specific tasks
#  a named block of code(group of statements) is called a function
#  a function is a group of code/related statements that perform specific tasks. the building blocks of programming languages


# def---definition
#  a function is identified by the key word def followed by function name and parentheses
# def myfunction():
#     num1, num2 = 20, 40
#     print(num1 + num2)
# myfunction()


# there are 2 types of functions
#  a function that is created without things inside is a static function bcoz the parenthesis is empty
#  a function that is created with things inside is a dynamic function

# def loop1():
#      list = [1,2,3,4,5,6,7,8]
# for i in list:#this is the outter block
#     print(i)#this is the inner block

# def loop2():
#     for i in range(1,10):
#         print(i) 
            
# def loop3():
#     item = 1 
#     for i in range(1,20):
#              print(i)

# def loop4():
#      for i in range(1,20):
#          if i % 2 == 0:
#              print(i)  
                        
# def loop5():
#     for i in range(1,20):
#         if i % 2!= 0:
#             print(i)
            
# def loop6():
#     for i in range(1,20):
#         if i % 2 == 1:
#             print(i)
            
# def loop7():
#     digit = [0,1,2,3]
#     for i in digit:
#         print(i)
#     else:
#         print('no digit')
        
# loop1()  
# loop2()
# loop3()
# loop4()
# loop5()
# loop6()
# loop7()
#a statement that is not part of any code is not indented
#functions are defined, anything indented is a function definition
#create a function called condition
def condition():# watever you put in a function is a function definition
    number = 10
    if number > 0:    
        print('number is positive')
    print('if statement is easy')    
condition()  

#if statement manuplating the above code
number = 10
if number > 0:#this not part of any block
    print('number is positive')   
    
number = 40
if number > 0:
    print('number is your age')   
print('not really')      
condition() 

# in js write a function as
#function condition(){
# number = 10
# if number > 0:    
#     print('number is positive')
# print('if statement is easy')
# }

#running a file is called execute
# the calling of a function is called 'invoke'

def mycondition():
    number = 10
    if number > 0:    
        print('positive number')
    else:     
        print('negative number')
    print('if statement is easy') 

mycondition()       
                      