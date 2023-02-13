def semana(dia):
    dia = input("Escriba un día de la semana:")
    if dia == "lunes":
        print("mañana será martes")
    elif dia == "martes":
        print("mañana será miércoles")
    elif dia == "miércoles":
        print("mañana será jueves")
    elif dia == "jueves":  
        print("mañana será viernes")
    elif dia == "viernes":
        print("mañana será sábado")
    elif dia == "sábado":
        print("mañana será domingo")
    elif dia == "domingo":
        print("mañana será lunes")
    else:
        print("no pusiste ningun dia de la semana")
