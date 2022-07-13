# Игра "Порази цель"
import turtle

# Именованные константы
SCREEN_WIDTH = 600  # Ширина экрана.
SCREEN_HEIGHT = 600  # Высота экрана.
TARGET_LLEFT_X = 100  # Левая нижняя координата Х цели.
TARGET_LLEFT_Y = 250  # Левая нижняя координата Y цели.
TARGET_WIDTH = 25  # Ширина цели.
FORCE_FACTOR = 30  # Фактор произвольной силы.
PROJECTILE_SPEED = 1  # Скорость анимации снаряда.
NORTH = 90  # Угол северного направления.
SOUTH = 270  # Угол южного направления.
EAST = 0  # Угол восточного направления.
WEST = 180  # Угол западного направления.
TARGET_ANGLE = 68  # Угол для попадения в цель.
FORCE = 9  # Сила удара.

# Настроить окно.
turtle.setup(SCREEN_WIDTH, SCREEN_HEIGHT)

# Нарисовать цель.
turtle.hideturtle()
turtle.speed(0)
turtle.penup()
turtle.goto(TARGET_LLEFT_X, TARGET_LLEFT_Y)
turtle.pendown()
turtle.setheading(EAST)
turtle.forward(TARGET_WIDTH)
turtle.setheading(NORTH)
turtle.forward(TARGET_WIDTH)
turtle.setheading(WEST)
turtle.forward(TARGET_WIDTH)
turtle.setheading(SOUTH)
turtle.forward(TARGET_WIDTH)
turtle.penup()

# Центрировать черепаху.
turtle.goto(0, 0)
turtle.setheading(EAST)
turtle.showturtle()
turtle.speed(PROJECTILE_SPEED)

# Получить угол выстрела и силу от пользователя.
angle = float(input("Введите угол выстрела снаряда: "))
force = float(input("Введите пусковую силу (1-10): "))

# Расчитать расстояние.
distance = force * FORCE_FACTOR

# Задать направление.
turtle.setheading(angle)

# Запустить снаряд.
turtle.pendown()
turtle.forward(distance)

# Снаряд поразил цель?
if (turtle.xcor() >= TARGET_LLEFT_X
    and turtle.xcor() <= (TARGET_LLEFT_X + TARGET_WIDTH)
    and turtle.ycor() >= TARGET_LLEFT_Y
        and turtle.ycor() <= (TARGET_LLEFT_Y + TARGET_WIDTH)):
    print('Цель поражена!')
else:
    print('Вы промахнулись.')
    if turtle.heading() < TARGET_ANGLE:
        print('Возьмите угол побольше!')
    elif turtle.heading() > TARGET_ANGLE:
        print('Возьмите угол поменьше!')
    elif force < FORCE:
        print('Увеличьте силу удара!')
    elif force > FORCE:
        print('Уменьшите силу удара!')
