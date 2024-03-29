#static functions are not good enough because they give static values
def add(a,b):
    ans = a+b
    print(ans)
    #functions are independent of the other
    #functions are self contained block of codes bcz variables cant be accessed out of the function
def add1(a,b):
    ans = a+b
    print(ans)  
#print(ans)    
    #print is not able to access the function
    #the variable we put in thr parentheses (a,b) are technically called parameters
    #a dynamic function can also be called  parameterlized functions because it has parameters  
#local can not be accessed outside of the function
age1 = 20
def addd(a,b):
    ans = a+b + age
    age1 = 19
    print(ans)
    print(age1)


# global variable is outside the function but can be accessed within the function 

age = 25
def add2(a,b):
    ans = a+b + age
    print(ans)
add2(20, 20) 
   
   
#how to make functions communicate with one another
# a function sharing a value must return it, in otherwards make it global
def vat(rate, price):
    frate = int((rate/100) * price)
    return frate    
    print(frate)    
vat(18,20000)  

def netPrice():
    vat2 = vat(18,20000)
    netP = vat2 + 20000
    #print(vat2)
    print(netP)
netPrice()     
#the values you pass during the invokation are called arguments e.g (18,20000)
#rate, price are parameters to 18,20000 arguments
#return is the last statement to be executed in a function, it marks the end of a function   
#return shares, gives back or let access



#paste code into the body of the email, by 9pm
#usig parameterlized function create 3 functions that share values..the last function should be the one printing out the last thing
# the 1st function will return to the 2nd function and then to the 3rd
#both 1st and 2nd functions are parameterlized but the 3rd function is not paramenterlized so it uses the value shared    

  