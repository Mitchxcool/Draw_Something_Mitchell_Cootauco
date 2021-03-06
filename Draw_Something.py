import turtle
import os
a = turtle.Turtle()
b = turtle.Turtle()
c = turtle.Turtle()
d = turtle.Turtle()
e = turtle.Turtle()
f = turtle.Turtle()
g = turtle.Turtle()
h = turtle.Turtle()
i = turtle.Turtle()
j = turtle.Turtle()
k = turtle.Turtle()
l = turtle.Turtle()
m = turtle.Turtle()
a.hideturtle()
b.hideturtle()
c.hideturtle()
d.hideturtle()
e.hideturtle()
f.hideturtle()
g.hideturtle()
h.hideturtle()
i.hideturtle()
j.hideturtle()
k.hideturtle()
l.hideturtle()
m.hideturtle()
RED = (245, 9, 9)
LIGHT_BLACK = (65, 50, 40)
DARK_BROWN = (133, 70, 25)
BROWN = (152, 90, 44)
LIGHT_BLUE = (64, 183, 245)
DARK_BLUE = (58, 97, 242)
SKIN_COLOR = (240, 191, 154)
x = int(90)
wn = turtle.Screen()
wn.colormode(255)
wn.bgcolor(LIGHT_BLUE)

#table
e.tracer(10)
e.color("black", BROWN)
e.pensize(5)
e.right(x)
e.forward(150)
e.left(x)
e.begin_fill()
e.forward(1000)
e.left(x)
e.forward(500)
e.left(x)
e.forward(2000)
e.left(x)
e.forward(500)
e.left(x)
e.forward(1000)
e.end_fill()

#computer
f.color("black", LIGHT_BLACK)
f.pensize(5)
f.tracer(5)
f.penup()
f.right(x)
f.forward(100)
f.left(x)
f.forward(300)
f.pendown()
f.begin_fill()
f.left(x)
f.forward(150)
f.right(x)
f.forward(50)
f.right(x)
f.forward(150)
f.right(x)
f.forward(50)
f.end_fill()
f.begin_fill()
f.right(45)
f.forward(125)
f.right(45)
f.forward(150)
f.right(x)
f.forward(50)
f.right(45)
f.forward(125)
f.end_fill()
f.right(135)
f.forward(50)
f.right(45)
f.forward(125)
f.right(180)
f.forward(125)
f.right(45)
f.forward(150)
f.right(180)
f.forward(150)
f.right(90)
f.forward(50)

f.color("gray")
f.penup()
f.right(180)
f.forward(50)
f.left(x)
f.forward(30)
f.right(135)
f.forward(30)
f.pendown()
f.begin_fill()
f.forward(70)
f.left(135)
f.forward(100)
f.left(45)
f.forward(70)
f.left(135)
f.forward(100)
f.end_fill()

f.color("black")
f.penup()
f.right(180)
f.forward(100)
f.right(135)
f.forward(100)
f.left(45)
f.pendown()
f.forward(111)
f.right(90)

wn.addshape(os.path.expanduser("victory.gif"))
g.shape(os.path.expanduser("victory.gif"))
g.pensize(-1)
g.penup()
g.goto(0,50)
g.stamp()

#monitor
a.tracer(4)
a.color("black")
a.pensize(10)
a.forward(90)
a.left(x)
a.forward(100)
a.left(x)
a.forward(180)
a.left(x)
a.forward(100)
a.left(x)
a.forward(90)

#mouse
i.tracer(3)
i.color("black")
i.penup()
i.forward(150)
i.right(x)
i.forward(115)
i.left(x)
i.pendown()
i.pensize(5)
i.begin_fill()
for a in range(3):
   i.left(45)
   i.forward(20)
i.left(45)
i.forward(15)
for a in range(3):
   i.left(45)
   i.forward(20)
i.left(45)
i.forward(15)
i.end_fill()
i.left(180)
i.forward(15/2)
i.right(x)
i.forward(110)
i.right(x)
i.forward(70)

#keyboard
j.tracer(2)
j.color("black")
j.penup()
j.right(x)
j.forward(110)
j.right(x)
j.forward(190)
j.pendown()
j.pensize(5)
j.begin_fill()
for i in range(2):
   j.right(x)
   j.forward(60)
   j.right(x)
   j.forward(250)
j.end_fill()
j.right(x)
j.forward(120)
j.right(x)
j.forward(101)

#head
b.color(SKIN_COLOR)
b.tracer(5)
b.penup()
b.forward(10)
b.right(x)
b.forward(50)
b.left(x)
b.pendown()
b.pensize(10)
b.begin_fill()
for i in range(15):
  b.left(25)
  b.forward(20)
b.end_fill()

#hair
k.color("black")
k.tracer(5)
k.penup()
k.forward(10)
k.right(x)
k.forward(50)
k.left(x)
k.left(25)
k.forward(20)
k.left(25)
k.forward(20)
k.pendown()
k.pensize(10)
k.begin_fill()
for i in range(10):
  k.left(25)
  k.forward(20)
k.end_fill()

#headset
l.tracer(2)
l.penup()
l.color(RED)
l.forward(10)
l.right(x)
l.forward(50)
l.left(x)
for i in range(3):
   l.left(25)
   l.forward(20)
l.pendown()
l.pensize(5)
l.begin_fill()
l.color("black", RED)
for i in range(6):
  l.right(60)
  l.forward(15)
l.end_fill()
l.color(RED)
for i in range(8):
  l.left(25)
  l.forward(20)
l.right(x)
l.color("black", RED)
l.begin_fill()
for i in range(6):
  l.left(60)
  l.forward(15)
l.end_fill()
l.color(RED)
l.forward(25)
l.right(110)
l.forward(35)

#shirt
c.color(DARK_BLUE)
c.tracer(5)
c.penup()
c.right(x)
c.forward(50)
c.left(x)
c.pendown()
c.begin_fill()
c.pensize(4)
c.forward(25)
for i in range(30):
   c.right(3)
   c.forward(3)
c.right(x)
c.forward(25)
c.left(x)
c.forward(150)
c.right(x)
c.forward(100)
c.right(x)
c.forward(150)
c.left(x)
c.forward(25)
c.right(x)
for i in range(30):
   c.right(3)
   c.forward(3)
c.forward(25)
c.end_fill()

#arm
d.color(SKIN_COLOR)
d.tracer(4)
d.penup()
d.forward(60)
d.right(x)
d.forward(110)
d.pendown()
d.begin_fill()
d.left(30)
d.forward(75)
d.left(110)
d.forward(100)
d.left(40)
for i in range(4):
    d.forward(20)
    d.left(x)
    d.forward(2)
    d.left(x)
    d.forward(20)
    d.right(x)
    d.forward(2)
    d.right(x)
d.left(x)
d.forward(15)
d.left(x)
d.forward(2)
d.left(x)
d.forward(15)
d.right(270)
d.right(220)
d.forward(65)
d.right(110)
d.forward(45)
d.left(60)
d.forward(25)
d.end_fill()

#arm 2
h.color(SKIN_COLOR)
h.tracer(4)
h.penup()
h.right(180)
h.forward(50)
h.left(x)
h.forward(110)
h.pendown()
h.begin_fill()
h.right(30)
h.forward(75)
h.right(110)
h.forward(100)
h.right(40)
for i in range(4):
    h.forward(20)
    h.right(x)
    h.forward(2)
    h.right(x)
    h.forward(20)
    h.left(x)
    h.forward(2)
    h.left(x)
h.right(x)
h.forward(15)
h.right(x)
h.forward(2)
h.right(x)
h.forward(15)
h.left(270)
h.left(220)
h.forward(65)
h.left(110)
h.forward(45)
h.right(60)
h.forward(25)
h.end_fill()

#chair
m.color("black", DARK_BROWN)
m.pensize(5)
m.tracer(4)
m.right(x)
m.penup()
m.forward(300)
m.pendown()
m.begin_fill()
m.right(x)
m.forward(50)
m.right(80)
m.forward(150)
m.right(90)
m.left(30)
m.forward(30)
for i in range(3):
    m.right(10)
    m.forward(15)
m.right(10)
m.forward(50)
m.right(10)
for i in range(4):
    m.right(10)
    m.forward(15)
m.right(45)
m.forward(152)
m.right(87)
m.forward(80)
m.end_fill()
m.begin_fill()
m.forward(45)
m.left(x)
m.forward(100)
m.left(x)
m.forward(20)
m.left(x)
m.forward(100)
m.end_fill()
m.begin_fill()
m.right(x)
m.forward(85)
m.right(x)
m.forward(100)
m.left(x)
m.forward(20)
m.left(x)
m.forward(100)
m.end_fill()

wn.exitonclick()