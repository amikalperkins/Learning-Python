import random
import turtle


t = turtle.Turtle()
wn = turtle.Screen()

def isInScreen(wn, t):
    leftBound = -(wn.window_width() / 2)
    rightBound = wn.window_width() / 2
    topBound = wn.window_height() / 2
    bottomBound = -(wn.window_height() / 2)

    turtleX = t.xcor()
    turtleY = t.ycor()

    stillIn = True

    if turtleX > rightBound or turtleX < leftBound:
        stillIn = False
    if turtleY > topBound or turtleY < bottomBound:
        stillIn = False

    return stillIn

t.shape('turtle')

while isInScreen(wn, t):
    coin = random.randrange(0,2)
    if coin == 0: # heads
        t.left(90)
    else:
        t.right(90)
    
    t.forward(50)

wn.exitonclick()