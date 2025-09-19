# memory.py — versión estable para la tarea:
# 1) Contador de taps
# 2) Detección de victoria
# 3) Texto centrado en cuadros
# 4) Letras/símbolos en vez de dígitos

from turtle import Screen, Turtle
from random import shuffle

# ----------------- utilidades -----------------
def to_index(x, y):
    col = int((x + 200) // 50)
    row = int((y + 200) // 50)
    if 0 <= col < 8 and 0 <= row < 8:
        return row * 8 + col
    return None

def to_xy(idx):
    return (-200 + (idx % 8) * 50, -200 + (idx // 8) * 50)

# ----------------- estado -----------------
state = {"mark": None}
symbols = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*")
tiles = symbols * 2
shuffle(tiles)
hide = [True] * 64
taps = 0

# ----------------- tortugas -----------------
board = Turtle(visible=False)
text  = Turtle(visible=False)
board.speed(0); text.speed(0)
board.penup(); text.penup()

def draw_square(x, y):
    board.goto(x, y)
    board.pendown()
    board.color("black", "lightgray")
    board.begin_fill()
    for _ in range(4):
        board.forward(50); board.left(90)
    board.end_fill()
    board.penup()

def draw():
    screen.tracer(0)
    board.clear(); text.clear()
    screen.bgcolor("white")

    # 1. dibujar casillas ocultas
    for i in range(64):
        if hide[i]:
            x, y = to_xy(i)
            draw_square(x, y)

    # 2. mostrar ficha marcada (centrada)
    mark = state["mark"]
    if mark is not None and hide[mark]:
        x, y = to_xy(mark)
        text.goto(x + 25, y + 8)
        text.color("black")
        text.write(tiles[mark], align="center", font=("Arial", 24, "normal"))

    # 3. contador de taps
    text.goto(-190, 190)
    text.color("black")
    text.write(f"Taps: {taps}", font=("Arial", 14, "normal"))

    # 4. victoria
    if all(not h for h in hide):
        text.goto(0, 0)
        text.color("darkgreen")
        text.write("¡Ganaste! 🎉", align="center", font=("Arial", 28, "bold"))

    screen.tracer(1)

def on_tap(x, y):
    global taps
    idx = to_index(x, y)
    if idx is None:
        return
    taps += 1

    mark = state["mark"]
    if mark is None or mark == idx or tiles[mark] != tiles[idx]:
        state["mark"] = idx
    else:
        hide[idx] = hide[mark] = False
        state["mark"] = None
    draw()

# ----------------- setup -----------------
screen = Screen()
screen.setup(420, 420)
screen.title("Memory – TEC")

screen.onclick(on_tap)
draw()
screen.mainloop()
