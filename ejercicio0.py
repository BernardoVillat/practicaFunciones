lista = []

def menu():
    print("Menú para Mantenimiento de Lista: \n 1- Agregar un valor: \n 2- Modificar un valor \n 3- Eliminar un valor \n 4- Salir")
def opcion1():
    contador = 1
    cantidad = int(input("Cuantos números desea agregar: "))
    while contador <= cantidad:
        num = int(input(f"Por favor ingrese el valor {contador}: "))
        lista.append(num)
        contador += 1
    print(f"Lista Actualizada: {lista}")
def opcion2():
    print(f"Lista: {lista}")
    indi = int(input("En que indice esta el número que quieres modificar? "))
    i = int(input("Que nuevo dato deseas colocar: "))
    lista[indi] = i
    print(f"Lista Actualizada: {lista}")
def opcion3():
    print(f"Lista: {lista}")
    n = int(input("En que indice esta el número que desea eliminar: "))
    del lista[n]
    print(f"Lista Actualizada: {lista}")

menu()
while True:
    opcion = int(input("Elije una opción: "))
    if opcion == 1:
        opcion1()
    elif opcion == 2:
        opcion2()
    elif opcion == 3:
        opcion3()
    elif opcion == 4:
        print("Gracias por utilizar nuestros servicios!!")
        break
    else:
        print("Elija una opción válida")



