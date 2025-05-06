"""Leer una palabra diferente a fin y convertirla a MAYUSCULA"""

palabra = input("Dime una palabra ")
while palabra.lower() != "fin":
    print(f"{palabra.upper()} tiene {len (palabra)} letras")
    palabra=input("Dime una palabra: ")
    print(palabra.upper())
else:
    print("Adios.....")
        
    
