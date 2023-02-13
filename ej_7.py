def viaje(alumnos, coste_alum, coste_tot, coste_tot_alum, coste_comida, coste_alojam, tiempo):
    alumnos = int(input("Introduce el número de alumnos: "))
    while alumnos < 0:
            print("No puede haber alumnos negativos")
            alumnos = int(input("Introduce el número de alumnos: "))
    tiempo = int(input("Introduce el tiempo de viaje en dias: "))
    while tiempo < 0:
            print("No puede haber tiempo negativo")
            tiempo = int(input("Introduce el tiempo de viaje: "))
    coste_comida = 3.50 * tiempo
    if alumnos <= 25:
        coste_alojam = 4.75 * tiempo
        coste_alum = 67.30
    elif 25 < alumnos < 30:
        coste_alojam = 4.75 * tiempo
        coste_alum = 61
    elif 30 <= alumnos <= 35:
        coste_alojam = 4 * tiempo
        coste_alum = 61
    else:
        coste_alojam = 3.50 * tiempo
        coste_alum = 61
    coste_tot_alum = coste_alum + coste_comida + coste_alojam
    coste_tot = coste_tot_alum * alumnos
    print("El coste total del viaje es: ", coste_tot)
    print("El coste total por alumno es: ", coste_tot_alum)
