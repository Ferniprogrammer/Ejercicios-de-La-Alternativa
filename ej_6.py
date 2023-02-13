def descuentos(cantidad, COMMAQ, BEL, descuento, final, compañia):
    cantidad = int(input("Ingrese la cantidad de productos: "))
    if cantidad < 0:
        print("No puede haber productos negativos")
        cantidad = int(input("Ingrese la cantidad de productos: "))
    elif 10000 <= cantidad <= 20000:
        descuento = 0.10
    elif 20000 < cantidad <= 40000:
        descuento = 0.15
    elif 40000 < cantidad:
        descuento = 0.20
    else:
        descuento = 0
    compañia = input("Ingrese la compañia: ")
    if descuento > 0:
        if compañia == "COMMAQ":
                 descuento -= 0.02
        elif compañia == "BEL":
                 descuento += 0.01
        else:
                   descuento = descuento
    else:
         descuento = descuento
    final = cantidad - (cantidad * descuento)
