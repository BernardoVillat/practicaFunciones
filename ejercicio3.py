def div():
    n1 = int(input("Ingrese un número: "))
    n2 = int(input("Ingrese el siguiente número: "))
    if n2 == 0:
        print("La división entre cero no está definida")
    else:
        resultado = n1 / n2
        print(f"El resultado de la división {n1}/{n2} es igual a: {resultado}")
div()