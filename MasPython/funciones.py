def conversacion(mensaje):
    print("Hola")
    print("Cómo estas")
    print(mensaje)
    print("Adios")

opciones = int(input("elige una opcion (1, 2, 3): "))
if "opcion" == 1:
     conversacion("elegistes la opcion 1")
elif "opcion" == 2:
    conversacion("elegistes la opcion 2")
elif "opcion" == 3:
    conversacion("elegistes la opcion 3")
else:
    print("Escribe una opción correcta")
 