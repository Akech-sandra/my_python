#use 'import' to import functions e.g 
   #given a function below
"""  
def sub_fruits(apples1, oranges1):
    fresh1 = apples1 + oranges1   
    print(fresh1)
    return(fresh1)
""" 
#creat another file.py, in it write the syntax for importing the function  
# this is how to import function sub_fruits 
""" 
    import func
print("this is the result of the function from the module", func.fruits(55,20))
 """

#object oriented programming is an idea that avocates for developing of software based on real world objects.

#principles of oop
#polymorphism
#inheritance
#abstraction
#encapsulation

#a class is a group of objects.
#e.g class car has objects such as benz, toyota, range rovers etc.
#class phone has objects such as itel, nokia, etc.
#objects take on all features of a class but each object has different attributes/characteristics

#an object is an instance of a class
#attributes of a class animal are, name, color, number of legs

#the key words 'is a' is used to identify a class of an object.
#e.g a cat 'is a' animal. therefore animal is a class while cat is an object of class animal.
#lake Victoria 'is a' lake

#abstraction refers to ability to ignore other details and concenrate on the highest level of representation
#e.g when registering a student for a course, details such as the student's name, course name, level of qualification, gender, age among others while ignoring other details such as number of friends, favorite colors, hobbies etc. 
#class name must be singular e.g class car not cars then the objects of class car are cars

#inheritance here we have the concept of parent and child
#toyota is a child of a car. class car is a parent of toyota
#sumsange is a child of a phone
#inheritance is the ability for an object to take on different attributes of a class
#e.g toyota wish belongs to class toyota and yet toyota belongs to class car

#polymorphism refers to the ability to take on different attributes of a class
#e.g class animal has objects such as dog, cat these bear the class attributes as well as own attributes such sound produced by both the animals are different, method of eating and what they eat are different too 

#encapsulation is the ability to have what to share and what not to share
#e.g class car encapsulates the attributes brand, model, year of manufacture.

#defining an object in python
#def a class use a keyword 'class' followed by the name of the class and ending with : and the class name starts with a capital leter.
#accessing objects using a '.' is called access identifier
#only concatenate(join or connect) things of the same type. e.g strings and strings
#a function of a class is called a method and then statements in that method are functions
# a complete fulfillment of a class attribute gives an object. e.g below

#this class car is not yet a certified because it is empty
"""
class Car:
    color = ''
    size = ''
    name = ''
"""    
#an object mercedes of class 'car'
"""
mercedes = Car()   
mercedes.name = 'benz' 
mercedes.color = 'white'
mercedes.size = 'large'
"""
