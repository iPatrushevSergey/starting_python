import turtle

# Нарисовать два квадрата с заливкой красного цвета.
turtle.setup(1000, 700)
turtle.showturtle()
turtle.speed(0)
turtle.penup()
turtle.goto(-300, 230)
turtle.pendown()
turtle.fillcolor('green')
turtle.begin_fill()
turtle.left(135)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(200)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.end_fill()
turtle.setheading(0)
turtle.penup()

# Нарисовать прямоугольник с заливкой красного цвета внутри друго треугольника.
turtle.goto(20, 230)
turtle.pendown()
print(turtle.pos(), 'Центр треугольника')
turtle.fillcolor('red')
turtle.begin_fill()
turtle.right(45)
turtle.forward(100)
print(turtle.pos())
turtle.goto(20, 159.29)
print(turtle.pos())
turtle.goto(-50.71, 159.29)
turtle.goto(20, 230)
turtle.end_fill()
turtle.penup()
turtle.goto(-50.71, 159.29)
turtle.pendown()
turtle.goto(20, 300)
turtle.goto(90.71, 159.29)
turtle.penup()

# Нарисовать параллелепид.
turtle.goto(300, 230)
turtle.pendown()
turtle.left(135)
turtle.forward(80)
print(turtle.pos(), 'B')
turtle.left(90)
turtle.forward(80)
print(turtle.pos(), 'A')
turtle.left(90)
turtle.forward(80)
print(turtle.pos(), 'F')
turtle.left(90)
turtle.forward(80)
print(turtle.pos(), 'Центр фигуры')
turtle.goto(220, 310)
turtle.penup()
turtle.goto(300, 230)
turtle.pendown()
turtle.forward(80)
print(turtle.pos(), 'C')
turtle.right(90)
turtle.forward(80)
print(turtle.pos(), 'D')
turtle.right(90)
turtle.forward(80)
print(turtle.pos(), 'E')
turtle.right(90)
turtle.forward(80)
turtle.goto(380, 150)
turtle.penup()
turtle.goto(300, 150)
turtle.pendown()
turtle.goto(220, 230)
turtle.penup()
turtle.goto(300, 310)
turtle.pendown()
turtle.goto(380, 230)
turtle.penup()

# Нарисовать пять симметричных кругов.
turtle.goto(-330, -50)
turtle.pendown()
turtle.circle(40)
turtle.penup()
turtle.goto(-240, -50)
turtle.pendown()
turtle.circle(40)
turtle.penup()
turtle.goto(-150, -50)
turtle.pendown()
turtle.circle(40)
turtle.penup()
turtle.goto(-195, -90)
turtle.pendown()
turtle.circle(40)
turtle.penup()
turtle.goto(-285, -90)
turtle.pendown()
turtle.circle(40)
turtle.penup()

# Нарисовать компас.
turtle.goto(-50, -50)
turtle.write('West')
turtle.goto(-20, -45)
turtle.pendown()
turtle.goto(120, -45)
turtle.penup()
turtle.goto(127, -50)
turtle.write('East')
turtle.goto(50, -45)
turtle.pendown()
turtle.goto(50, 25)
turtle.penup()
turtle.goto(40, 25)
turtle.write('North')
turtle.goto(50, -45)
turtle.pendown()
turtle.goto(50, -115)
turtle.penup()
turtle.goto(38, -128)
turtle.write('South')
turtle.goto(70, -45)
turtle.pendown()
turtle.circle(20)
turtle.penup()

# Нарисовать квадрат с точками.
turtle.goto(300, -45)
turtle.pendown()
turtle.dot()
turtle.left(45)
turtle.forward(100)
print(turtle.pos(), 'A')
turtle.dot()
turtle.right(180)
turtle.forward(200)
print(turtle.pos(), 'C')
turtle.dot()
turtle.goto(300, -45)
turtle.left(90)
turtle.forward(100)
print(turtle.pos(), 'B')
turtle.dot()
turtle.right(180)
turtle.forward(200)
print(turtle.pos(), 'D')
turtle.dot()
turtle.goto(229.29, 25.71)
turtle.left(135)
turtle.forward(15)
turtle.penup()
turtle.forward(15)
turtle.pendown()
turtle.forward(33)
turtle.penup()
turtle.forward(15)
turtle.pendown()
turtle.forward(33)
turtle.penup()
turtle.forward(15)
turtle.pendown()
turtle.goto(370.71, 25.71)
turtle.goto(370.71, -115.71)
turtle.penup()
turtle.goto(229.29, -115.71)
turtle.pendown()
turtle.forward(15)
turtle.penup()
turtle.forward(15)
turtle.pendown()
turtle.forward(33)
turtle.penup()
turtle.forward(15)
turtle.pendown()
turtle.forward(33)
turtle.penup()
turtle.forward(15)
turtle.pendown()
turtle.goto(370.71, -115.71)

turtle.done()
