def addmultiplenumbers(numeros): #suma
    total = 0
    for n in numeros:
        total = total + n
    return total


def multiplymultiplenumbers(numeros): #multiplicación
    total = 1
    for n in numeros:
        total = total * n
    return total


def isiteven(numero): #par o impar
    return numero % 2 == 0


def isitaninteger(numero): #entero o no
    return isinstance(numero, int)


def main():
    print("¡Hola 🫡!")
    

    numeros = [1, 10, 25, 4]
    
    print("Suma:", addmultiplenumbers(numeros))
    print("Multiplicación:", multiplymultiplenumbers(numeros))
    print("¿Es par 10?:", isiteven(10))
    print("¿Es entero 24.5?:", isitaninteger(24.5))





if __name__ == "__main__":
    main()

