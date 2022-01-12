from turtle import *
recuadro = 1   #número de cuadrado
for fila in range(3):
    for columna in range(3):
        begin_fill()   #lo que quiero pintar es lo que se dibuja a continuación: un cuadrado
        for cuadrado in range(4):
            forward(50)
            right(90)
        if recuadro % 2 == 0:   #si el número es par
                fillcolor('red')   #pinto de rojo
        else:   #si el número no es par
                fillcolor('blue')  #pinto de verde
        end_fill()   #terminé de dibujar un cuadrado, entonces lo pinto
        recuadro += 1;   #paso a contabilizar el siguiente cuadrado
        forward(50)
    backward(150)
    right(90)
    forward(50)
    left(90)        