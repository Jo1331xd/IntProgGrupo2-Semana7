import datetime
import random
import time as t 
import os 

fecha= datetime.date.today()

print(f"Bienvenida \n {fecha}")

def esperar (espera):
    while(espera >= 0 ):
        os.system("cls || clear ")
        print(f"Espera {espera}")
        espera-=1
        t.sleep(1)
    os.system("cls || clear ")

def adivinar (num_user, num_rdn):
    esperar(5)
    if num_user == num_rdn:
        print ("Adivinaste ")
    else:
        print("Lo siento, no es el numero ") 
        
def main():
    numero_alea = random.randint (1,10)
    resp = "s"
    while resp.lower() != 'n':
        
        num= input("Ingresa un numero del 1 al 10:" )
        adivinar (int(num), numero_alea)
        resp = input ("Desea seguir jugando? [ S / N / R ]: ")
        if resp.lower == 'r':
            num_alea = random.randit (1,10)
main()