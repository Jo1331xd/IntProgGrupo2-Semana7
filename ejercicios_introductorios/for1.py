"""Leer una palabra diferente a fin y convertirla a mayuscula"""

palabra = input("Dime una palabra: ")

fin="Fin"

for i in range (10000000):
    if(palabra.lower()=="fin"):
        print("Adios..")
        break
    else:
        print(f"{palabra.upper()} tiene {len (palabra)} letras")
        palabra=input("Dime una palabra: ")
        print(palabra.upper())