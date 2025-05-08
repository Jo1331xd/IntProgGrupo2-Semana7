def calificaciones ():
    numero_calificaciones=int(input("Cual es el numero de calificaciones que tienes"))
    for i in range(numero_calificaciones):
        calificacion=int(input("Cual es la calificacion que tienes: "))
        if numero_calificaciones == 0:
            print("Adios")
            break

        else:  
            calificacion *= numero_calificaciones

            print(f"Tienes de promedio {calificacion}")
calificaciones()