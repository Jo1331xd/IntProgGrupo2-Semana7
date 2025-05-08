def pares ():
    contador=0
    producto=1
    par=2
    numero=int(input("Dame un numero "))
    while contador < numero:
        contador+=1
        producto*=par
        par=2
        print(f"El producto de los numeros pares de {numero} es: {producto}")

pares()