def tests(test1, test2):
    #.checks if test1 is equvalent to test2
    if test1 == test2:
        #send or share the value of test1 to a function that calls it
        return test1
    else:
        #else share the value of test2 to a function that calls it if test1 !== test2
        return test2
#will display on the screen requesting for user input and converts it to an integer data type. test2 is a variable assigned to a value attained from user's input

test2 = int(input('Please enter Marks for test two: '))

'''
this multiline comment which defines of a dynamic function courseWrk, calls global variable test3 and test4 which requests for user input, calculates avgtestsCswork and fnltestsCswork then prints the fnltestsCswork and requests for user input cswrk



'''

test4 = int(input('please enter mark for test4: '))  
test3 = int(input('Please enter marks for test3: '))          
            
def courseWrk(cswork, test4, test3):
    #testsMark is assigned to function tests that has arguments (cswork, test4, test3)
    testsMark = tests(test4,test3)
    #calculate the average of cswork and testsMark by summing them up and the dividing by 2
    avgtestsCswork = (cswork + testsMark)/2
    #calculate the fnltestsCswork by multiplying avgtestsCswork by (40/100)
    fnltestsCswork = avgtestsCswork * (40/100)
    #a print statement that prints .........
    print('.........................')
    #output your final coursework marks is: ', fnltestsCswork
    print('your final coursework marks is: ', fnltestsCswork)
    
    print('........................')
#request for user input
cswork = int(input('Please enter your course work Marks: '))
#invoke the function courseWrk
courseWrk(cswork, test4, test3)