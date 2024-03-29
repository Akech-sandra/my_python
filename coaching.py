"""
#abstraction
class Arsenal:
    def ordegard(self):
        print("Ordegard")        
#polymorphism 
#in tis example, . is used and it takes on 3 forms with different attributes
class Color:
    def __init__(self, color):
        self.color = color     
class Car:
    def benz(self):
        bens = 100 * 0.06
        return bens
value = Car()
print (value.benz())
"""
#inheritance
class Animal:
    name = ""
    def eat(self):
        print('I can eat')
class Dog(Animal):# this shows that a dog is subclass Animal. Dog is a child/drived class of Animal parent/base/superclass 
    def display(self):#display defines the method of a dog class
        print('My name is', self.name)  
        print(f'My name is {self.name}')
gshep = Dog()
gshep.name = 'police'
print(gshep.name)
print(gshep.display())
print(gshep.eat()) 


#assignment 
#create 3 superclasses with corresponding at least 2 subclasses and create 3 objects from them   
    
            
            
class Shape:
    name = ''
    width = ''
    height = ''
    def area(self):
        print('every shape takes an area space')
        
class Square(Shape):
    def total_area(self):
        print('my name is', self.name)
        print('My square has a height of', self.height)
        print('My square has a width of', self.width)
         
        
dice = Square() 
dice.name = 'Dice'
print(dice.name)
dice.name = 'Ludo'
dice.height = '50cm'
dice.width = '50cm'
print(dice.total_area())
print(dice.area())
      
           
class Rectangle(Shape):
    def parameter(self):
        print('my name is', self.name)
        print('My rectangle has a height of', self.height)
        print('My rectangle has a width of', self.width) 
    
door = Rectangle()
door.name = 'Door'
print(door.name)
door.name = 'wooden door'
door.height = '200m'
door.width = '100m'
print(door.parameter())
print(door.area())

              
class Employee:
    position = ''
    role = ''
    responsibility = ''
    def salary(self):
        print('always paid daily')
    
class Engineer(Employee):
    def engineering(self):    
        print('My positions is', self.position)
        print('My role is to', self.role)
        print('My responsibilities are', self.responsibility) 
        
software_engineer = Engineer()  

software_engineer.position = 'Leader'
print(software_engineer.position)
software_engineer.position = 'Team lead'
software_engineer.role = 'Mobilize'
software_engineer.responsibility = 'to always do the technical work'
print(software_engineer.engineering())
print(software_engineer.salary()) 

     
        
class Developer(Employee):
    def develops_systems(self):    
        print('My positions is', self.position)
        print('My role is to', self.role)
        print('My responsibilities are', self.responsibility) 
        
full_stack = Developer()
full_stack.position = 'manager'
print(full_stack.position)
full_stack.position = 'project manager'
full_stack.role = 'coordinate'
full_stack.responsibility = 'Design and develop systems'
print(full_stack.develops_systems())
print(full_stack.salary())                
    
class Fruit:   
    name = ''
    sweetness = ''
    color = ''
    def deliciousness(self):
        print('all fruits are delicious and healthy')
        
class Citrus(Fruit):
    def juicy(self):
        print('My lemon is called', self.name)
        print('My lemon is', self.sweetness)
        print('My lemon is', self.color) 
         

lemon   = Citrus()
lemon.name = 'lemon'
print(lemon.name)
lemon.name = 'nimu'
lemon.sweetness = 'so fresh and juicy'
lemon.color = 'green'
print(lemon.juicy())
print(lemon.deliciousness()) 

   
    
class Berry(Fruit): 
    def sweet(self): 
        print('My blueberry is called', self.name)
        print('My blueberry is', self.sweetness)
        print('My blueberry is', self.color) 
    
blueberry =Berry()

blueberry.name = 'Blueberry'
print(blueberry.name)
blueberry.name = 'Berry'
blueberry.sweetness = 'so yummy'
blueberry.color = 'blue'
print(blueberry.sweet())
print(blueberry.deliciousness())
          
        
        
        
        
                           