#dont create more than one function with the same name
def add():
    num1, num2 = 20, 40
    sum = num1 + num2
    print(sum)
add()
#creating a dynamic fuction 
def add1(num1, num2):
    sum = num1 + num2
    print(sum)
    
add1(100,50)
add1(200,45)
add1 = (45, 75,90)  

def sub1(num1, num2):
    sub = num1 - num2
    print(sub)
sub1(96,60)  
  
def mul1(num1, num2):
    mul = num1 * num2
    print(mul)
sub1(12,10)    
  
def div1(num1, num2):
    div = num1 / num2
    print(div)
sub1(120,12)  

def mod1(num1, num2):
    mod = num1 % num2
    print(mod)
sub1(155,10)    

def exp1(num1, num2):
    exp = num1 ** num2
    print(exp)
sub1(12,10)  

def fdiv1(num1, num2):
    fdiv = num1 // num2
    print(fdiv)
sub1(100,3)  

# add1(12,10)
sub1(50,15)
div1(24,12)
exp1(2,2)

def multdata(num1, num2, name, flt):
    print(num1)
    print(num2)
    print(name)
    print(flt)
multdata(2, 20, 'Sann', 5.5)

def myinfo(color, fruit, team_num, born_timeth):   
    print(color)
    print(fruit)
    print(team_num)
    print(born_timeth)
myinfo('blue', 'wmelon', 1, '6th')

def hack(name, yob, district):
    print(name)
    print(yob)
    print(district)
    currentYear = 2024
    age = currentYear - yob
    print(name, 'is', age)
hack('akespeare', 2000, 'Oyam')        
    
