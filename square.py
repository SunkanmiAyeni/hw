import turtle
turtle.Screen().bgcolor("Green")
turtle.Screen().setup(500,750)
square=turtle.Turtle()
num_sides=4
len_sides=70
angl=360.0/num_sides
for i in range(num_sides):
    square. forward(len_sides )
    square.right(angl)
turtle.done()