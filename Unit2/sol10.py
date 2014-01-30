# prob10: TurtleGraphicsPolygon
import turtle
import time
import os
import math
print 'Drawing a filled polygon with turtle'
print 'Enter colour values [0 - 1]'
r = 1.0 - float(raw_input('enter red: '))
g = 1.0 - float(raw_input('enter green: '))
b = 1.0 - float(raw_input('enter blue: '))
edge = int(raw_input('enter edge length: '))
angle = 360/5

label = "(" + str(r) + ", " + str(g) + ", " + str(b) + ")"
turtle.clear()

turtle.fillcolor(r, g, b)
turtle.goto(0,0)
turtle.up()
h = edge*0.5/math.cos(54*math.pi/180)
p = h*math.sin(54*math.pi/180)
turtle.forward(p)
turtle.right(90)
turtle.backward(edge*0.5)
turtle.down()
turtle.begin_fill()
for i in range(5):
	turtle.forward(edge)
	turtle.right(angle)
turtle.end_fill()
turtle.done()
time.sleep(1)
os._exit(1)

