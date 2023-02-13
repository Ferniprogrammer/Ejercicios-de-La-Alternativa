def notas(nota1, nota2, nota3, nota4, media):
    nota1 = int(input("Ingrese la primera nota ente 0 y 20: "))
    while nota1 < 0 or nota1 > 20:
        print("La nota no es válida")
        nota1 = int(input("Ingrese la primera nota ente 0 y 20: "))
    nota2 = int(input("Ingrese la segunda nota ente 0 y 20: "))
    while nota2 < 0 or nota2 > 20:
        print("La nota no es válida")
        nota2 = int(input("Ingrese la segunda nota ente 0 y 20: "))
    nota3 = int(input("Ingrese la tercera nota ente 0 y 20: "))
    while nota3 < 0 or nota3 > 20:
        print("La nota no es válida")
        nota3 = int(input("Ingrese la tercera nota ente 0 y 20: "))
    nota4 = int(input("Ingrese la cuarta nota ente 0 y 20: "))
    while nota4 < 0 or nota4 > 20:
        print("La nota no es válida")
        nota4 = int(input("Ingrese la cuarta nota ente 0 y 20: "))
    media = (nota1 + nota2 + nota3 + nota4) / 4
    if media > 15:
        print("Alumno con talento")
    elif 12 <= media <= 15:
        print("Alumno con capacidad")
    else:
        print("El alumno debe reorientarse")
    
    