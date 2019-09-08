import os
from random import randint,uniform,random


pala = ""
def menu():
	"""
	Función que limpia la pantalla y muestra nuevamente el menu
	"""
	os.system('cls') 
	print ("Selecciona una opción")
	print ("\t1 - primera opción")
	print ("\t2 - segunda opción")
	print ("\t3 - tercera opción")
	print ("\t9 - salir")
    
def jugar(x, y):
    intentos= range(y)
    if x == None:
        print("INTENTE INGERSAR PRIMERO LA PALBRA")
        seguir = input(
        "Pulse Intro para lanzar el dado. Pulse otra tecla e Intro para terminar: "
        )
        menu()
    else:
        print('A H O R C A D O')
        letrasIncorrectas = ''
        letrasCorrectas = ''     
        palabraSecreta = x
        juegoTerminado = False
        
        while True:
            mostrarTablero(letrasIncorrectas, letrasCorrectas, palabraSecreta)
        
            intento = obtenerIntento(letrasIncorrectas + letrasCorrectas)
        
            if intento in palabraSecreta:
                letrasCorrectas = letrasCorrectas + intento
        
                encontradoTodasLasLetras = True
                for i in range(len(palabraSecreta)):
                    if palabraSecreta[i] not in letrasCorrectas:
                        encontradoTodasLasLetras = False
                        break
                if encontradoTodasLasLetras:
                    print('¡Sí! ¡La palabra secreta es "' + palabraSecreta + '"! ¡Has ganado!')
                    juegoTerminado = True
            else:
                letrasIncorrectas = letrasIncorrectas + intento
        
                if len(letrasIncorrectas) == len(intentos):
                    mostrarTablero( letrasIncorrectas, letrasCorrectas, palabraSecreta)
                    print('¡Te has quedado sin intentos!\nDespués de ' + str(len(letrasIncorrectas)) + ' intentos fallidos y ' + str(len(letrasCorrectas)) + ' aciertos, la palabra era "' + palabraSecreta + '"')
                    juegoTerminado = True
                
            if juegoTerminado:
                if jugarDeNuevo():
                    letrasIncorrectas = ''
                    letrasCorrectas = ''
                    juegoTerminado = False
                    palabraSecreta = x

                else:
                    break

    
 
 
def mostrarTablero(letrasIncorrectas, letrasCorrectas, palabraSecreta):
    print([len(letrasIncorrectas)])
    print()
 
    print('Letras incorrectas:', end=' ')
    for letra in letrasIncorrectas:
        print(letra, end=' ')
    print()
 
    espaciosVacíos = '_' * len(palabraSecreta)
 
    for i in range(len(palabraSecreta)): 
        if palabraSecreta[i] in letrasCorrectas:
            espaciosVacíos = espaciosVacíos[:i] + palabraSecreta[i] + espaciosVacíos[i+1:]
 
    for letra in espaciosVacíos:
        print(letra, end=' ')
    print()
 
def obtenerIntento(letrasProbadas):
     while True:
        print('Adivina una letra.')
        intento = input()
        intento = intento.lower()
        if len(intento) != 1:
            print('Por favor, introduce una letra.')
        elif intento in letrasProbadas:
            print('Ya has probado esa letra. Elige otra.')
        elif intento not in 'abcdefghijklmnñopqrstuvwxyz':
            print('Por favor ingresa una LETRA.')
        else:
            return intento
 
def jugarDeNuevo():   
    print('¿Quieres jugar de nuevo? (sí o no si desea comenzar con una palabra nueva)')
    
    return input().lower().startswith('s')
 

	



if __name__ == "__main__": 
    pala = None 
    while True:        
        menu()  
        opcionMenu = input("inserta un numero valor >> ")
    
        if opcionMenu=="1":
            print ("")
            palar = input("iNGRESE PALABRA: ")  
            pala = palar          
            
        elif opcionMenu=="2":
            print ("")
            jugar(pala,6)
            
        elif opcionMenu=="3":
            print ("")
            os.system('cls') 
            
            print ("Selecciona una opción")
            print ("\t1 - primera opción")
            print ("\t2 - segunda opción")
            print ("\t3 - tercera opción") 
            op = int(input("ingrese su opcion: "))           
            while op < 1  or op > 3 :
                print("Lo siento, la opcion es invalida : ", op)
                op = int(input("ingrese su opcion: ")) 
                seguir = input(
                        "Pulse Intro para intentar nueva opcion : "
                    )
            else :
                os.system("cls")

                print("La opcion es correcta : ", op)
                if op == 1 :
                    print("tamano_max_palabra <- 10")
                    print("vidas <- 6")
                    palabra = input("digite la palabra: ")
                    inten = int(input("numero de intentos: "))
                    jugar(palabra,inten)

                elif op == 2:
                    print("tamano_max_palabra <- 15")
                    print("vidas <- 6")
                    palabra = input("digite la palabra: ")
                    inten = int(input("numero de intentos: "))
                    jugar(palabra,inten)
                else:
                    print("tamano_max_palabra <- 20")
                    print("vidas <- 4")
                    palabra = input("digite la palabra: ")
                    inten = int(input("numero de intentos: "))
                    jugar(palabra,inten)
                seguir = input(
                    "Pulse Intro para para seguir. Pulse otra tecla e Intro para terminar: "
                )
                
        elif opcionMenu=="9":
            break
        else:
            print ("")
            input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")
        print(pala)
    
    salir = False
    opcion = 0
