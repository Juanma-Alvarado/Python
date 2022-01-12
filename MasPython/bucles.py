def run():
    LIMITE = 100000000000000

    contador = 0
    potecia_2 = 2**contador
    while potecia_2 < LIMITE:
        print("2 elevado a " + str(contador) + "es igual a: " + str(potecia_2))
        contador = contador + 1
        potecia_2 = 2**contador

if __name__ == "__main__":
    run()