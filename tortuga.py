import turtle 
# variable para la ventana 
ventana = turtle.Screen()
ventana.title("Juego de Serpiente")
ventana.bgcolor("blue")

# crear el pincel 
pincel = turtle.Turtle("turtle")
pincel.color("green")
pincel.up()
pincel.goto(30, -50)
pincel.shapesize(1.5)

# funciones para moviemientos 
def arriba():
  pincel.setheading(90)
  pincel.forward(40)

def abajo():
  pincel.setheading(270)
  pincel.forward(40)
  
def derecha():
  pincel.setheading(0)
  pincel.forward(40)

def izquierda():
  pincel.setheading(180)
  pincel.forward(40)
  
# escuchar al teclado 
turtle.listen()
# invocando a las funciones 
turtle.onkeypress(arriba, "Up")
turtle.onkeypress(abajo, "Down")
turtle.onkeypress(derecha, "Right")
turtle.onkeypress(izquierda, "Left")


# para no cerrar la ventana 
turtle.done()