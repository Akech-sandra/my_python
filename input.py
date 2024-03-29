#promt user to input data
name = input('please enter here your name')
print('your name is:', name )

age = input('please enter here your age')
print('your age is:', age )

#name, email, contact, location, gender, age, program, course
# """ this is also a python comment """

name = input('type from here your details')
email = input('type from here your details')
contact = input('type from here your details')
location = input('type from here your details')
gender = input('type from here your details')
age = input('type from here your details')
program = input('type from here your details')
course = input('type from here your details')

#a code which tells a computer to count up to the range of our choice

my_input = int(input('please enter the range of numbers to count'))
for i in range(my_input):
    print(i)
    
#write 2 dynamic functions, 1st one prompts a user to input name, age, email and gender and it prints them.
#2nd function should promt the user to input the rate of paye always 30%, NSSF rate is 11%, gross income/salary and calculate the netpay
#by Sunday 9am. 24th March 2024


# 1st function
def user_info(name, age, email, gender):
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    email = input("Enter your email: ")
    gender = input("Enter your gender: ")
    
    print("User Information:")
    print("Name:", name)
    print("Age:", age)
    print("Email:", email)
    print("Gender:", gender)

user_info("name", "age"," email", "gender")

#2nd function
def salary_info(paye, nssf, gross_income):
    gross_income = int(input("Enter your gross income: "))
    paye = int(input("Enter your paye rate: "))
    nssf = int(input("Enter your NSSF rate: "))
    netpay = gross_income - (int(paye/100 * gross_income) - int(nssf/100 * gross_income))
    print(netpay)
    
    print("Salary Details:")
    print("Gross Income: $", gross_income)
    print("PAYE: $", paye)
    print("NSSF: $", nssf)
    print("Net Pay: $", netpay)
    
salary_info("paye", "nssf", "gross_income")      