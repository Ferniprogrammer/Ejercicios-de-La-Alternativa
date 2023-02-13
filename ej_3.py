def compra(total, descuento, gastos):
    gastos = int(input("Ingrese los gastos: "))
    if 100 <= gastos <= 500:
        descuento = 0.05
    elif 501 <= gastos :
        descuent0 = 0.08
    else:
        descuento = 0
    total = gastos - (gastos * descuento)
    print("El total a pagar es: ", total)
