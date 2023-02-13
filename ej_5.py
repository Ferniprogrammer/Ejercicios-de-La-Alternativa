def descuentos(pequeño, mediano, grande, niños, precio, final):
    precio = int(input("Ingrese el precio de la entrada: "))
    while precio < 0:
        print("No puede haber precios negativos")
        precio = int(input("Ingrese el precio de la entrada: "))
    niños = int(input("Ingrese la cantidad de niños: "))
    while niños < 0:
        print("No puede haber niños negativos")
        niños = int(input("Ingrese la cantidad de niños: "))
    pequeño = 0.1
    mediano = 0.15
    grande = 0.18
    if niños == 2:
        final = precio - (precio * pequeño)
    elif niños == 3:
        final = precio - (precio * mediano)
    elif niños == 4:
        final = precio - (precio * grande)
    elif niños > 4:
        final = precio - (precio * (grande + 0.01 * (niños - 4)))
    else:
        final = precio
    print("El precio final es: ", final)
    