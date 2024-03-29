# import turtle
# tr = turtle.Turtle()
# tr.pensize(5)
# tr.color('blue')
# tr.penup()
# tr.goto(-110, -25)#looks at the position of your graphics
# tr.pendown()
# tr.circle(45)
# tr.color('black')
# tr.penup()
# tr.goto(0, -25)
# tr.pendown()
# tr.circle(45)
# tr.color('red')
# tr.penup()
# tr.goto(110, -25)
# tr.pendown()
# tr.circle(45)
# tr.color('yellow')
# tr.penup()
# tr.goto(-55, -75)
# tr.pendown()
# tr.circle(45)
# tr.color('green')
# tr.penup()
# tr.goto(55, -75)
# tr.pendown()
# tr.circle(45)

#define a dynamic function that takes on colors that can draw an olympics logo



import turtle
def colors(blue2,black2,red2,green2,yellow2):
    tr = turtle.Turtle()
    tr.pensize(10)
    tr.color(blue2)
    tr.penup()
    tr.goto(-110, -25)
    tr.pendown()
    tr.circle(45)

    tr.color(black2)
    tr.penup()
    tr.goto(0, -25)
    tr.pendown()
    tr.circle(45)
    
    tr.color(red2)
    tr.penup()
    tr.goto(110, -25)
    tr.pendown()
    tr.circle(45)
    
    tr.color(green2)
    tr.penup()
    tr.goto(-55, -75)
    tr.pendown()
    tr.circle(45) 
    
    tr.color(yellow2)
    tr.penup()
    tr.goto(55, -75)
    tr.pendown()
    tr.circle(45) 
    
#colors('blue', 'black', 'red', 'green', 'yellow')  

    

    
    
