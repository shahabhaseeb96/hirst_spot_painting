# import colorgram
# colors = colorgram.extract("hirst.jpg", 20)
#
# rgb_color = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_color.append(new_color)
#
# print(rgb_color)
import turtle as t
import random

list_colors = [(221, 231, 236), (237, 34, 109), (147, 26, 66), (240, 73, 34), (10, 146, 90), (226, 168, 40), (179, 159, 45), (27, 125, 192), (249, 221, 26), (43, 192, 234), (83, 21, 78), (126, 193, 73), (182, 35, 98), (38, 170, 114), (252, 224, 0), (194, 70, 31), (28, 178, 216)]
t.colormode(255)
timmy = t.Turtle()
timmy.speed("fastest")
timmy.setheading(225)
timmy.penup()
timmy.forward(300)
timmy.setheading(0)
timmy.hideturtle()
for _ in range(5):
    for _ in range(10):

        timmy.dot(20, random.choice(list_colors))
        timmy.penup()
        timmy.forward(50)
        timmy.pendown()
        timmy.dot(20, random.choice(list_colors))

    timmy.setheading(90)
    timmy.penup()
    timmy.forward(50)
    timmy.setheading(180)
    for _ in range(10):

        timmy.dot(20, random.choice(list_colors))
        timmy.penup()
        timmy.forward(50)
        timmy.pendown()
        timmy.dot(20, random.choice(list_colors))

    timmy.setheading(90)
    timmy.penup()
    timmy.forward(50)
    timmy.setheading(0)



screen = t.Screen()
screen.exitonclick()
