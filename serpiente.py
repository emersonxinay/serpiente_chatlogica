import turtle
import time
import random

# Configuración de la ventana
ventana = turtle.Screen()
puntaje = 0
ventana.title("Juego de Serpiente")
ventana.bgcolor("blue")
ventana.setup(width=600, height=600)
ventana.tracer(0)

# Serpiente
serpiente = turtle.Turtle()
serpiente.speed(0)
serpiente.color("green")
serpiente.shape("turtle")
serpiente.penup()
serpiente.goto(0, 0)
serpiente.direction = "stop"

# Comida
comida = turtle.Turtle()
comida.speed(0)
comida.color("red")
comida.shape("circle")
comida.penup()
comida.goto(0, 100)

# Segmentos del cuerpo de la serpiente
segmentos = []

# Funciones de movimiento
def mover():
    if serpiente.direction == "up":
        y = serpiente.ycor()
        serpiente.sety(y + 20)
    if serpiente.direction == "down":
        y = serpiente.ycor()
        serpiente.sety(y - 20)
    if serpiente.direction == "right":
        x = serpiente.xcor()
        serpiente.setx(x + 20)
    if serpiente.direction == "left":
        x = serpiente.xcor()
        serpiente.setx(x - 20)

def ir_arriba():
    serpiente.setheading(90)
    if serpiente.direction != "down":
        serpiente.direction = "up"

def ir_abajo():
    serpiente.setheading(270)
    if serpiente.direction != "up":
        serpiente.direction = "down"

def ir_derecha():
    serpiente.setheading(0)
    if serpiente.direction != "left":
        serpiente.direction = "right"

def ir_izquierda():
    serpiente.setheading(180)
    if serpiente.direction != "right":
        serpiente.direction = "left"

# Teclado
ventana.listen()
ventana.onkeypress(ir_arriba, "Up")
ventana.onkeypress(ir_abajo, "Down")
ventana.onkeypress(ir_derecha, "Right")
ventana.onkeypress(ir_izquierda, "Left")

# Función para mover la comida a una ubicación aleatoria
def mover_comida():
    x = random.randint(-280, 280)
    y = random.randint(-280, 280)
    comida.goto(x, y)

# Colisiones
def colision_comida():
    if serpiente.distance(comida) < 20:
        mover_comida()
        # Agregar un segmento a la serpiente
        nuevo_segmento = turtle.Turtle()
        nuevo_segmento.speed(0)
        nuevo_segmento.color("green")
        nuevo_segmento.shape("square")
        nuevo_segmento.penup()
        segmentos.append(nuevo_segmento)

# Actualizar la pantalla
def actualizar_pantalla():
    ventana.update()

# Inicializar el juego
while True:
    ventana.update()

    # Mover la serpiente
    mover()

    # Colisiones con la comida
    colision_comida()

    # Mover los segmentos del cuerpo de la serpiente
    for i in range(len(segmentos) - 1, 0, -1):
        x = segmentos[i - 1].xcor()
        y = segmentos[i - 1].ycor()
        segmentos[i].goto(x, y)

    if len(segmentos) > 0:
        x = serpiente.xcor()
        y = serpiente.ycor()
        segmentos[0].goto(x, y)

    # Detectar colisiones con el borde de la pantalla
    if (serpiente.xcor() > 290 or serpiente.xcor() < -290 or
        serpiente.ycor() > 290 or serpiente.ycor() < -290):
        serpiente.goto(0, 0)
        serpiente.direction = "stop"

        # Esconder los segmentos del cuerpo
        for segmento in segmentos:
            segmento.goto(1000, 1000)

        # Limpiar la lista de segmentos
        segmentos.clear()

        # Resetea el ventana
        ventana.clear()
        ventana.write("Puntaje: {}".format(puntaje), align="center", font=("Courier", 24, "normal"))

    time.sleep(0.1)

ventana.done()
ventana.mainloop()
