def factorial ():

    numero_positivo=int(input("Dame un numero: "))
    contador= 0 
    producto= 1
    factorial=1

    while contador < numero_positivo:
        contador +=1 
        producto *= factorial
        factorial +=1
        
        print (f"La multiplicacion de los numeros hasta {numero_positivo} es: {producto}")
factorial()