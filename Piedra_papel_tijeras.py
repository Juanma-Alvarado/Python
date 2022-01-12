import time
from time import sleep
import random

op = ['piedra','papel','tijeras']
sep = '-' * 15

while True:
    user = input('''Bienvenido al juego de ✊✋✌

1 - Piedra
2 - Papel
3 - Tijeras

Elige una opción: ''').lower()
    sleep(0.7)
    if user not in op:
        print('\nMovimiento no valido')
        continue
    pc = random.choice(op)
    sleep(0.7)
    print(f'\nLa PC ha seleccionado {pc}')
    sleep(0.7)
    if user == pc:
        print(f'\nEmpate!, ambos eligieron {user}')
    elif user == 'piedra' and pc == 'tijeras':
        print(f'\nGanastes!, {user} ganas en contra de {pc}')
    elif user == 'tijeras' and pc == 'papel':
        print(f'\nGanastes!, {user} ganas en contra de {pc}')
    elif user == 'papel' and pc == 'piedra':
        print(f'\nGanastes!, {user} ganas en contra de {pc}')
    else:
        print(f'\nPerdistes!{user} pierde contra {pc}') 
    print (f'{sep}Fin del juego{sep}')   

# Resuelvve numero divicivles por 7 
# Pero no son multiplos de 5
# Del 2000 a el 3200

l=[]
for i in range(2000, 3201):
    if (i%7==0) and (i%5!=0):
        l.append(str(i))
print(','.join(l))