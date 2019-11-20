#First Python Game!
#By: Andrew Ha
#Date Started: 10/3/19

import turtle

gameScreen = turtle.Screen()
gameScreen.title("Pong")
gameScreen.bgcolor("black")
gameScreen.setup(width = 800, height = 600)

#Score
playerOneScore = 0
playerTwoScore = 0

#Stops window from updating
gameScreen.tracer(0)

#Paddle 1(Left Side)
paddleOne = turtle.Turtle()
paddleOne.speed(0)
paddleOne.shape("square")
paddleOne.color("magenta")
paddleOne.shapesize(stretch_wid = 5, stretch_len = 1)
paddleOne.penup()
paddleOne.goto(-350, 0)

#Paddle 2(Right Side)
paddleTwo = turtle.Turtle()
paddleTwo.speed(0)
paddleTwo.shape("square")
paddleTwo.color("magenta")
paddleTwo.shapesize(stretch_wid = 5, stretch_len = 1)
paddleTwo.penup()
paddleTwo.goto(350, 0)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.dx = 5
ball.dy = 5

#Draw
draw = turtle.Turtle()
draw.speed(0)
draw.color("white")
draw.penup()
draw.hideturtle()
draw.goto(0 , 260)
draw.write("Player 1 0  Player 2 0" , align = "center", font= ("Courier", 24, "normal"))

#Movements
def paddleOneUp():
	y = paddleOne.ycor()
	y += 40
	if y > 250:
		y = 250
	paddleOne.sety(y)

def paddleOneDown():
	y = paddleOne.ycor()
	y -= 40
	if y < - 250:
		y = -250
	paddleOne.sety(y)

def paddleTwoUp():
	y = paddleTwo.ycor()
	y += 30
	if y > 250:
		y = 250
	paddleTwo.sety(y)

def paddleTwoDown():
	y = paddleTwo.ycor()
	y -= 30
	if y < - 250:
		y = -250
	paddleTwo.sety(y)

#Keyboard Binding
gameScreen.listen()
gameScreen.onkeypress(paddleOneUp, "w")
gameScreen.onkeypress(paddleOneDown, "s")
gameScreen.onkeypress(paddleTwoUp, "Up")
gameScreen.onkeypress(paddleTwoDown, "Down")


#Main game loop
while True:
	gameScreen.update()

	#Ball Movement
	ball.setx(ball.xcor() + ball.dx)
	ball.sety(ball.ycor() + ball.dy)

	#Check to see if the ball hits the  Upper and Lower Borders
	if ball.ycor() > 290:
		ball.sety(290)
		ball.dy *= -1

	if ball.ycor() < -280:
		ball.sety(-280)
		ball.dy *= -1

	#Check to see if the ball hits the Right and Left Borders
	if ball.xcor() > 390:
		ball.goto(0,0)
		ball.dx *= -1
		playerOneScore += 1 
		draw.clear()
		draw.write("Player 1: {}  Player 2: {}".format(playerOneScore, playerTwoScore), align = "center", font= ("Courier", 24, "normal"))

	if ball.xcor() < -390:
		ball.goto(0,0)
		ball.dx *= -1
		playerTwoScore += 1 
		draw.clear()
		draw.write("Player 1: {}  Player 2: {}".format(playerOneScore, playerTwoScore), align = "center", font= ("Courier", 24, "normal"))

	#Collision with ball and paddle
	if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddleTwo.ycor() + 40 and ball.ycor() > paddleTwo.ycor() - 40):
		ball.setx(340)
		ball.dx *= -1

	if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddleOne.ycor() + 40 and ball.ycor() > paddleOne.ycor() - 40):
		ball.setx(-340)
		ball.dx *= -1
