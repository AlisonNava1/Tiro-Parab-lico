#Modificado por:
#Autor: Alison Daniela Nava Bravo
#Autor: Eduardo Aguilar Chías

from random import randrange
from turtle import *
from freegames import vector
from random import *

ball = vector(-200, -200)
speed = vector(0, 0)
targets = []

def tap(x, y):
    "Responde al tap de la pantalla"
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = (x + 200) / 25
        speed.y = (y + 200) / 25

def inside(xy):
    "Regresa True si xy estan dentro de la pantalla."
    return -200 < xy.x < 200 and -200 < xy.y < 200

def draw():
    "Dibuja la pelota y los objetivos"
    crayola = ["DeepPink","DeepSkyBlue","Lime","Crimson","Fuchsia","Aquamarine"]  # Lista de posibles colores para los objetivos.
    clear()

    for target in targets:
        goto(target.x, target.y)
        dot(20, choice(crayola))

    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'Black')

    update()

def move():
    "Mueve la pelota y los objetivos"
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    for target in targets:
        target.x -= 1.5

    if inside(ball):
        speed.y -= 0.1
        ball.move(speed)

    dupe = targets.copy()
    targets.clear()

    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)

    draw()

    ontimer(move, 50)

setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()
