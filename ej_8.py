def prima( distancia, prim_dist, tiempo, prim_tiempo, prim_tot,num_accidentes):
    distancia = int(input("Ingrese la distancia recorrida en km: "))
    while distancia < 0:
        print("La distancia no puede ser negativa")
        distancia = int(input("Ingrese la distancia recorrida en km: "))
        prim_dist = distancia * 0.01
    if prim_dist > 400:
        prim_dist = 400
    tiempo = int(input("Ingrese el tiempo en la empresa en años: "))
    while tiempo < 0:
        print("El tiempo no puede ser negativo")
        tiempo = int(input("Ingrese el tiempo en la empresa en años: "))
    if tiempo < 4:
        prim tiempo = 0
    else:
        prim_tiempo = 200 + (tiempo - 4) * 20
    responsabilidad = int(input("Ingrese la responsabilidad del accidente: "))
    while responsabilidad < 0:
        print("La responsabilidad no puede ser negativa")
        responsabilidad = int(input("Ingrese la responsabilidad del accidente: "))
    num_accidentes = int(input("Ingrese el numero de accidentes: "))
    while num_accidentes < 0:
        print("El numero de accidentes no puede ser negativo")
        num_accidentes = int(input("Ingrese el numero de accidentes: "))
    if num_accidentes == 0:
        prim_tot = prim_dist + prim_tiempo
    elif num_accidentes == 1:
        prim_tot = (prim_dist + prim_tiempo) * 0.5
    elif num_accidentes == 2:
        prim_tot = (prim_dist + prim_tiempo) * 0.33
    elif num_accidentes >= 3:
        prim_tot = (prim_dist + prim_tiempo) * 0.25
    else:
        prim_tot = 0
    print("La prima total es: ", prim_tot)
    