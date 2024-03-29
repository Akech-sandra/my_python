#for loop
#full colon is
list = [10, 20, 30, 40, 50, 60, 70, 80]
# a loop is a mechanism of writing instruction to repeatedly(iterate or continue) do an activity until it finds a certain condition is met or fulfilled
# i represents all the elements in the list  
for i in list:
    print(i)
    
for item in range(10):
    print(item) 
    
item = 1
# 1 represents the start point and 10 is the end point
for item in range(1,10):
    print(item)
#loops can slow down the computer in places where you have many iterations

for i in range(1,20):
    if i % 2 == 0:
        print(i)

for i in range(1,20):
    if i % 2 != 0:
        print(i)   
 # this is a block of code---a collection of related statements
 #block of code is identified by indentation       
for i in range(1,20):
    if i % 2 == 1:
        print(i)      
        
digits = [24,25,26,27,28,29,30]   
for i in digits:
    print(i)
else:
    print("no more digits")    
     
# create a dictionary of lakes you know and use a loop to loop through them and their values                
    lake_Malawi = {"country:": "Tanzania","location:":"East_Africa", "area:":"2600 sq km" }
    for keys, values in lake_Malawi.items():
        print(keys, values)
        