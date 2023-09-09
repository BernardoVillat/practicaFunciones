def suma():
    n = int(input("Cuantos números deseas sumar: "))
    if n <= 2:
        num = int(input("Por favor ingrese el primer número: ")) 
        num2 = int(input("Por favor ingrese el segundo número: "))
        print(f"La suma de {num} + {num2} es igual a: {num + num2}")
    elif n > 2:
        listaSuma = []
        contador = 1
        cantidad = int(input("Cantidad de números que desea ingresar: "))
        while contador <= cantidad:
            n = int(input("Por favor ingresa el valor: "))
            listaSuma.append(n)
            contador += 1
        suma = 0
        x = 0
        while x < len(listaSuma):
            suma = suma + listaSuma[x]
            x += 1
        print(f"La suma de esos números es: {suma}")
suma()