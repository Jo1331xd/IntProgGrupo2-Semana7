"""Suma de los primeros N números"""

numero=int(input("Dame un numero: "))
suma=0
for i in range (1, numero +1):
    suma += i
print(suma)