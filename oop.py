#OOP-Object Oriented Programming
#oop is an idea that avocates for developing of software based on real world objects.
#classes vs objects

#principles of oop
#polymorphism
#inheritance
#abstraction
#encapsulation

#a class is a group of objects
#a class is a blueprint of an object(original copy of something)
#e.g class car has objects such as benz, toyota, range rovers etc.
#class phone has objects such as itel, nokia, etc.
#objects take on all features of a class but each object has different attributes/characteristics

#an object is an instance of a class
#attributes of a class animal are, name, color, number of legs
#an object should have one or more attributes of a given class

#how to identify a class of an object, use a phase 'is a'
#e.g a cat 'is a' animal. therefore animal is a class while cat is an object of class animal.
#lake Victoria 'is a' lake

#abstraction refers to ability to ignore other details and concenrate on the highest level of representation
#abstract helps in identifying classes.
#class name must be singular e.g class car not cars then the objects of class car are cars

#inheritance here we have the concept of parent and child
#toyota is a child of a car. class car is a parent of toyota
#sumsange is a child of a phone
#inheritance is the ability for an object to take on different attributes of a class
#e.g toyota wish belongs to class toyota and yet toyota belongs to class car

#polymorphism refers to the ability to take on different attributes or forms
#encapsulation is the ability to have what to share and what not to share



#defining an object in python
#def a class use a keyword class followed by the name of the class and ending with : and the class name starts with a capital leter. this also creates a function.
# a complete fulfillment of a class attribute gives an object

#this class is not yet a certified object
class Animal:
    color = ''
    size = ''
    gender = ''
    name = ''
    age = ''
    sound = ''
    species = ''
    def feed(self):# this is a method
        #print('by chewing')
        return 'by chewing'  
#creating an object of class 'animal'
cat = Animal()   
cat.name = 'pus' 
cat.gender = 'male'
cat.sound = 'meow'
cat.species = 'felime'
cat.age = 2
cat.color = 'white'
cat.size = 'small'
#accessing objects using a . it is also called access identifier
# f tells a computer to be extra careful to unpack strings
print(f'{cat.name} is {cat.age} years old')
print(cat.name  +  'does'  +  cat.sound)
print(f'{cat.feed()}')
#only concatenate(join or connect) things of the same type. e.g strings and strings

class Animal:
    color = ''
    size = ''
    gender = ''
    name = ''
    age = ''
    sound = ''
    species = ''  
#creating another object bird of class 'animal'
    bird = Animal()
    bird.color = 'white'
    bird.size = 'medium'
    bird.gender = 'female'
    bird.name = 'flamingo'
    bird.age = '5'
    bird.sound = 'honking'
    bird.species = 'lesser'
    
#creating another object fish of class 'animal'
    fish = Animal()
    fish.color = 'gery'
    fish.size = 'big'
    fish.gender = 'male'
    fish.name = 'Tilapia'
    fish.age = '8 months'
    fish.species = 'Blue tilapia'  
    
#creating another object fish of class 'animal'
    insect = Animal()
    insect.color = 'yellowish'
    insect.size = 'tiny'
    insect.gender = 'male'
    insect.name = 'bee'
    insect.age = '1 months'
    insect.species = 'worker bee'    
    
#things that animal does is a method, these are called behaviors 
#a function of a class is called a method and then statements in that method are functions

#takeaways
#in oop, we define methods not functions

class Lake:
    def __init__(self, name, location, depth, width, size, types):
        self.name = name
        self.location = location
        self.depth = depth
        self.width = width
        self.size = size
        self.types = types
#shish method (__init__) is a special method used to identify properties of a class
#the first parameter in the shish parenthesis(self) refers to an individual class and not an attribute
class River:
     def __init__(ozzy, name, location, length):
         ozzy.name = name
         ozzy.location = location
         ozzy.length = length
         
#any method of a class should take a parameter 'self'
#creating objects of a class lake

lake = Lake('lake Victoria', 'central', '1200ft', '400m', '500km', 'satly')# this invokes a method of a function
print(lake.name)
print(lake.location)
print(lake.depth)
print(lake.width)


#oop exercise, define 5 classes with atleast shish method taking atleast 5 parameters and create aleast 3 objects
class lake:
    def __init__(self, location, name, depth, width, height):
        self.location = location
        self.name = name
        self.length = depth
        self.width = width
        self.height = height
Albert = lake ('Western Ug', 'L.Albert', '35000ft', '100m', '2000m') 

class Student:
    def __init__(self, name, age, height, gender, course):
        self.name = name
        self.age = age
        self.height = height
        self.gender = gender
        self.course = course
person = Student ('sandra', 23, '7ft', 'female', 'software engineer', )       

class Carbohydrates:
    def __init__(self, name, color, size, shape, weight):
       self.name = name
       self.color = color
       self.size = size
       self.shape = shape
       self.weight = weight
food = Carbohydrates ('rice', 'white', 'small', 'oval', '1gm') 

class Fish:
    def __intit__(self, size, color, name, texture, weight):
        self.size = size
        self.color = color
        self.name = name
        self.texture = texture
        self.weight = weight 

class Car:
    def __init__(self, name, brand, model, color, size):
       self.name = name
       self.brand = brand
       self.model = model
       self.color = color
       self.size = size
       
#a shish function or method represents a constructor . it is used to give value of an object      

#it is used to initialize an instantiated object is an instance of a class in oop.

#self is not a constant or keyword, any name can be used

   


        