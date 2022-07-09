# Эта программа наносит звёзды созвездия Ориона,
# названия звёзд и линии созвездия.
import turtle

# Задать размер окна.
turtle.setup(500, 600)

# Установить черепаху.
turtle.penup()
turtle.hideturtle()

# Создать именованные константы для звёздных координат.
LEFT_SHOULDER_X = -70
LEFT_SHOULDER_Y = 200

RIGHT_SHOULDER_X = 80
RIGHT_SHOULDER_Y = 180

LEFT_BELTSTAR_X = -40
LEFT_BELTSTAR_Y = -20

MIDDLE_BELTSTAR_X = 0
MIDDLE_BELTSTAR_Y = 0

RIGHT_BELTSTAR_X = 40
RIGHT_BELTSTAR_Y = 20

LEFT_KNEE_X = -90
LEFT_KNEE_Y = -180

RIGHT_KNEE_X = 120
RIGHT_KNEE_Y = -140

# Нанести звёзды.
turtle.goto(LEFT_SHOULDER_X, LEFT_SHOULDER_Y)  # left shoulder
turtle.dot()
turtle.goto(RIGHT_SHOULDER_X, RIGHT_SHOULDER_Y)  # right shoulder
turtle.dot()
turtle.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y)  # left beltstar
turtle.dot()
turtle.goto(MIDDLE_BELTSTAR_X, MIDDLE_BELTSTAR_Y)  # middle beltstar
turtle.dot()
turtle.goto(RIGHT_BELTSTAR_X, RIGHT_BELTSTAR_Y)  # right beltstar
turtle.dot()
turtle.goto(LEFT_KNEE_X, LEFT_KNEE_Y)  # left knee
turtle.dot()
turtle.goto(RIGHT_KNEE_X, RIGHT_KNEE_Y)  # right knee
turtle.dot()

# Вывести названия звёзд.
turtle.goto(LEFT_SHOULDER_X, LEFT_SHOULDER_Y)  # Left shoulder
turtle.write("Бетельгейзе")
turtle.goto(RIGHT_SHOULDER_X, RIGHT_SHOULDER_Y)  # Right shoulder
turtle.write("Хатиса")
turtle.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y)  # Left beltstar
turtle.write("Альнитак")
turtle.goto(MIDDLE_BELTSTAR_X, MIDDLE_BELTSTAR_Y)  # Middle beltstar
turtle.write("Альнилам")
turtle.goto(RIGHT_BELTSTAR_X, RIGHT_BELTSTAR_Y)  # Right beltstar
turtle.write("Минтака")
turtle.goto(LEFT_KNEE_X, LEFT_KNEE_Y)  # Left knee
turtle.write("Саиф")
turtle.goto(RIGHT_KNEE_X, RIGHT_KNEE_Y)  # Right knee
turtle.write("Ригель")

# Нанести линию из левого плеча в левую звезду пояса.
turtle.goto(LEFT_SHOULDER_X, LEFT_SHOULDER_Y)
turtle.pendown()
turtle.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y)
turtle.penup()
# Нанести линию из правого плеча в правую звезду пояса.
turtle.goto(RIGHT_SHOULDER_X, RIGHT_SHOULDER_Y)
turtle.pendown()
turtle.goto(RIGHT_BELTSTAR_X, RIGHT_BELTSTAR_Y)
turtle.penup()
# Нанести линию из левой звезды пояса в среднюю звезду пояса.
turtle.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y)
turtle.pendown()
turtle.goto(MIDDLE_BELTSTAR_X, MIDDLE_BELTSTAR_Y)
turtle.penup()
# Нанести линию из средней звезды пояса в правую звезду пояса.
turtle.goto(MIDDLE_BELTSTAR_X, MIDDLE_BELTSTAR_Y)
turtle.pendown()
turtle.goto(RIGHT_BELTSTAR_X, RIGHT_BELTSTAR_Y)
turtle.penup()
# Нанести линию из левой звезды пояса в левое колено.
turtle.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y)
turtle.pendown()
turtle.goto(LEFT_KNEE_X, LEFT_KNEE_Y)
turtle.penup()
# Нанести линию из правой звезды пояса в правое колено.
turtle.goto(RIGHT_BELTSTAR_X, RIGHT_BELTSTAR_Y)
turtle.pendown()
turtle.goto(RIGHT_KNEE_X, RIGHT_KNEE_Y)
turtle.penup()

turtle.done()
