def palidromo(palabra):
    palabra = palabra.replace(" ","")
    palabra = palabra.lower()
    palabra_invertidda = palabra[::-1]
    if palabra == palabra_invertidda:
            return True
    else:
        return False



def run():
    palabra = input("Escribe una palabra:  ")
    es_palindromo = palidromo(palabra)
    if es_palindromo == True:
        print("Es palídromo")
    else:
        print('No es palíndromo')


if __name__ == "__name__":
    run()
