import turtle as _t
# Esto lo hice para que no confunda al programa cuando ocupe la función de circle
# que tiene turtle por que si no se vería como circle circle.
from turtle import *
from freegames import vector

def line(start, end):
    "Draw line from start to end."
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)

def square(start, end):
    "Draw square from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()

def circle(start, end):
    # Aquí implemente el círculo y las variables nuevas fueron para establecer
    # la distancia vertical y horizontal entre el punto incial y el punto final
    # la ecuación nos da la distancia entre ambos puntos y también el down me sirve
    # porque turtle hace los circulos al borde y no al centro y con esto eso se corrige
    "Draw circle from start to end."
    dx = end.x - start.x
    dy = end.y - start.y
    radius = (dx * dx + dy * dy) ** 0.5
    up()
    goto(start.x, start.y - radius)
    down()
    begin_fill()
    _t.circle(radius)
    end_fill()

def rectangle(start, end):
    "Draw rectangle from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    width = end.x - start.x
    height = end.y - start.y

    #calculé las medidas del rectangulo y les puse su ancho y alto
    #ahora el patrón se repite 2 veces para lograr que la figura se ciere por completo

    for count in range (2):
        forward(width)
        left(90)
        forward(height)
        left(90)
    end_fill()

def triangle(start, end):

    #Aquí empieza a dibujarse la figura así que con esto me posiciono
    "Draw triangle from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    
    #lo de aqui es para definir la distancia entre dos puntos como el lado del triangulo
    side = end.x - start.x

    #ahora avanzaré a un lado y daré tres giros de 120 grados para que la suma de todos los angulos sea 180 
        for count in range (3):
        forward(side)
        left(120)
    end_fill() 

def tap(x, y):
    "Store starting point or draw shape."
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None

def store(key, value):
    "Store value in state at key."
    state[key] = value

state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
#Agregué el color naranja
onkey(lambda: color('orange'), 'O')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()