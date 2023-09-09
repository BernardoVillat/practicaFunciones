lista = []
def menu():
    print("Menú de Opciones: \n 1- Ingresar n datos a una lista \n 2- Ordenar lista de menor a mayor \n 3- Calcular la sumatoria de la lista \n 4- Calcular la media de datos \n 5- Calcular la mediana \n 6- Calcular la moda \n 7- Calcular desviación tipica o estandar \n 8- Salir")
def opcion1():
    contador = 1
    cantidad = int(input("Cuantos datos deseas ingresar a la lista: "))
    while contador <= cantidad:
        n = int(input(f"Por favor ingresa el valor {contador}: "))
        lista.append(n)
        contador += 1
    print(f"Lista Actualizada: {lista}")
def opcion2():
    for i in range(len(lista)-1): 
        for j in range(len(lista)-1 - i): 
            if lista[j] > lista[j + 1]: 
                lista[j], lista[j + 1] = lista[j + 1], lista [j]
    print(lista)
def opcion3():
        suma = 0
        x = 0
        while x < len(lista):
            suma = suma + lista[x]
            x += 1
        print(f"La sumatoria de esta lista {lista} es: {suma}")
def opcion4():
        suma = 0
        x = 0
        while x < len(lista):
            suma = suma + lista[x]
            x += 1
        media = suma / len(lista)
        print(f"La media de la lista {lista} es: {media}")
def opcion5():
    for i in range(len(lista)-1): 
        for j in range(len(lista)-1 - i): 
            if lista[j] > lista[j + 1]: 
                lista[j], lista[j + 1] = lista[j + 1], lista [j]
    mitad = int(len(lista) / 2)
    if len(lista) % 2 == 0:
        mediana = (lista[mitad - 1] + lista[mitad]) / 2
    else:
        mediana = lista[mitad]
    print(f"La mediana de la lista {lista} es {mediana}")
def opcion6():
    dicc_conteo = {}
    for num in lista:
        clave = str(num)
        if clave not in dicc_conteo:
            dicc_conteo[clave] = 1
        else:
            dicc_conteo[clave] += 1
    frec_mayor = 0
    num_mas_repet = lista[0]
    for num in dicc_conteo:
        if dicc_conteo[num] > frec_mayor:
            num_mas_repet = num
            frec_mayor = dicc_conteo[num]
        conteo = dicc_conteo[num_mas_repet]
    print(f"La moda es el número {num_mas_repet} que aparece en {conteo} ocasiones")
def opcion7():
    suma = 0
    x = 0
    while x < len(lista):
        suma = suma + lista[x]
        x += 1
    media = suma / len(lista)
    suma_cuadra = 0
    for i in lista:
        suma_cuadra += i**2
    desv = (suma_cuadra / len(lista) - media ** 2) ** (0.5)
    print(f"La desviación típica o estandar es: {round(desv, 2)}")

menu()
while True:
    opcion = int(input("Por favor, ingrese una opción: "))
    if opcion == 1:
        opcion1()
    elif opcion == 2:
        opcion2()
    elif opcion == 3:
        opcion3()
    elif opcion == 4:
        opcion4()
    elif opcion == 5:
        opcion5()
    elif opcion == 6:
        opcion6()
    elif opcion == 7:
        opcion7()
    elif opcion == 8:
        print("¡¡Gracias por usar nuestros servicios!!")
        break
    else:
        print("Por favor, ingrese una opción válida")
