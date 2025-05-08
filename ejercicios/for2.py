def palabra_conteo():
    for _ in range(100000):
        palabra = input("Ingrese una palabra: ")
        if palabra.lower() == "terminar":
            print("Adiós")
            break
        else:
            print(f"Esta {palabra.capitalize()} tiene {len (palabra)} letras")



palabra_conteo()