def clasif(a, b, mult, suma, desorden):
    a = int(input("Ingrese el primer número: "))
    b = int(input("Ingrese el segundo número: "))
    mult = a * b
    suma = a + b
    desorden = [a, b, mult, suma]
    # El .sort() ordena los elementos de una lista
    desorden.sort()
    print(desorden)

