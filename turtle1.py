import turtle
move =  turtle.Turtle()
s = turtle.Screen()
s.bgcolor('black')
move.pencolor('white')
a = 0
b = 0
move.speed(0)
move.penup()
move.goto(0, 200)
move.pendown()

while True:
	move.forward(a)
	move.right(b)
	a+=3
	b+=1
	if b == 210:
		break
	move.hideturtle()

turtle.done()