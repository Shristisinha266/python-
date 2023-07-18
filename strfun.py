
#isalpha
"""str = "gahdadsg823473"
print(str.isalpha())"""


#isalpha
"""str = "jhasdh \n t"
print(str.isprintable())

str = " "
print(str.isprintable())
"""


#join
"""
str  = "adhaksdja hfgsjfh kjsfhkhf jksfish"
x = ",".join(str)
print(x)
"""


#clear
"""
str = ["sjahq", "ajkduqad", "kdujads", "akdaiud"]
b = str
str[1] = "hello"

print(b.clear())"""



# str = ["sjahq", "ajkduqad", "kdujads", "akdaiud", "hello", "hello"]
# print(str.count("hello"))

"""
from turtle import *
color('blue', 'black')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()

"""

"""
import turtle  
# Creating turtle  
t = turtle.Turtle()  
  
turtle.bgcolor("black")  
turtle.pensize(2)  
turtle.speed(0)  
  
while (True):  
    for i in range(6):  
        for colors in ["red", "blue", "magenta", "green", "yellow", "white"]:  
            turtle.color(colors)  
            turtle.circle(100)  
            turtle.left(10)  
  
  
turtle.hideturtle()  
turtle.mainloop()  


"""


# Import turtle package

import turtle

pen = turtle.Turtle()

def curve():
	for i in range(200):

		pen.right(1)
		pen.forward(1)

def heart():

	pen.fillcolor('red')

	pen.begin_fill()

	pen.left(140)
	pen.forward(113)

	curve()
	pen.left(120)

	curve()

	pen.forward(112)

	pen.end_fill()

def txt():

	pen.up()

	pen.setpos(-68, 95)

	pen.down()

	pen.color('white')

	pen.write("will u be my forever?", font=(
	"Verdana", 10, "bold"))


heart()

txt()

# To hide turtle
pen.ht()

    
    
    
