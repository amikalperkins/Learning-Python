# for loop_var [sequence] : 
#   indented statement block
#   python uses indentions instead of curly braces

import turtle

ws = turtle.Screen()
mikey = turtle.Turtle()

# for iterator in [0,1,2,3]:
#     mikey.forward(50)
#     mikey.left(90)

# for iterator in ['yellow', 'blue', 'red']:
#     mikey.color(iterator)
#     mikey.forward(50)
#     mikey.left(90)

for iterator in range(4): 
    mikey.forward(50)
    mikey.left(90)