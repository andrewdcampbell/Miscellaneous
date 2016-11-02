from turtle import *
showturtle()

bgcolor('black')
speed(0)

up()
goto(-50,70)
down()

def polyspi(angle,inc,side,times,line_color):
    if times > 0:
        speed(0)
        color(line_color)
        fd(side)
        rt(angle)
        polyspi(angle,inc, (side + inc),(times - 1),line_color)

polyspi(117,4,25,40,'yellow')

up()
goto(0,-50)
down()

for n in range(16):
	pencolor('red')
	circle(120,213)
	right(45)

up()
goto(-80,265)
down()

for n in range(16):
	pencolor('blue')
	circle(220,213)
	right(45)

exitonclick()