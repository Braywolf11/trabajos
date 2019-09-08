##Point Number une
import os

N = int(input("Cantidad de casillas: "))
i = 1
num1 = int(input("Ahora ingrese el primer numero : "))
num2 = int(input("Ahora ingrese el siguiente numero : "))
####################
lista = []
lista.append(num1)
lista.append(num2)
#####################
os.system("cls")
print("Elemetos del vector ")
print(lista)
suma = lista[0]+lista[len(lista)-1]
i = 1
while i < N-2 :
    numero = int(input("Escriba un número positivo: "))
    while suma == numero :
        print(" NO es posible agregar ese número, ya que la suma del primer y último número existentes en el vector hasta el momento")
        numero = int(input("Escriba un número : "))    
    if  len(lista) == 3 :
        print(" ")
        lista.append(numero)
        print(lista)
    else :
        lista.append(numero)
        print(lista)
        i = i + 1
    suma = lista[0]+lista[len(lista)-1]

os.system("cls")

print("El vector termino con los siguentes numeros en las ",N," casillas ")
print(lista)
print("Gracias por su colaboración, Ralizado por Brayan Rivera")









