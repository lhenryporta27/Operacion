def sumar_numeros():
    numeros = input("Ingresa los números separados por espacios: ")
    lista = numeros.split()
    suma = sum(float(num) for num in lista)
    print(f"La suma es: {suma}")

if __name__ == "__main__":
    sumar_numeros()
