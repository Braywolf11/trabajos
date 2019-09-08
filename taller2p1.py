import os
from random import randint,uniform,random,randrange

def main():
    os.system("cls")
    jugadores = randrange(1,6)
    n = randint(1,3)
    camino = 1 
  
    print("Bienvenidos la cantidad de jugadores es: ", jugadores)

    
    while jugadores < 2  or jugadores > 5 :
            
        jugadores = randint(1,3)
        print("Lo siento, la cantidad de jugadores es invalida : ", jugadores)
        seguir = input(
                "Pulse Intro para intentar nueva cantidad de jugadores: "
            )
    else :
        os.system("cls")
        print("La cantidad de jugadores es : ", jugadores)
        print("Bienvenido al juego")

    if n == 1 :
        print("1. Nivel Basico (Tablero de 20 posiciones)")
        camino = 20 
    elif n == 2:
        print("2. Nivel Intermedio (Tablero de 30 posiciones)")
        camino = 30 
    else:
        print("3. Nivel Intermedio (Tablero de 50 posiciones)")
        camino = 50
    seguir = input(
        "Pulse Intro para lanzar el dado. Pulse otra tecla e Intro para terminar: "
    )
    suma_1 = 0       
    i=1
    j = 1
    total = 0
    total2 = 0
    total3 = 0
    total4 = 0
    total5 = 0
    while seguir == "":     
        
        while i <= jugadores:
            tirada_1 = randrange(1, 6)        
            tirada_2 = randrange(1, 6)
            suma_1 += tirada_1 + tirada_2
            if i == 1:                
                total = total + suma_1 
                print(f"Jugador 1: Tirada: {tirada_1} y {tirada_2} - Suma: {total}")
            elif i == 2:                
                total2 = total2 + suma_1 
                print(f"Jugador 2: Tirada: {tirada_1} y {tirada_2} - Suma: {total2}")
            elif i == 3:                
                total3 = total3 + suma_1 
                print(f"Jugador {i}: Tirada: {tirada_1} y {tirada_2} - Suma: {total3}")
            elif i == 4:                
                total4 = total4 + suma_1 
                print(f"Jugador {i}: Tirada: {tirada_1} y {tirada_2} - Suma: {total3}")
            elif i == 5:                
                total5 = total5 + suma_1 
                print(f"Jugador {i}: Tirada: {tirada_1} y {tirada_2} - Suma: {total3}")
            else:
                print(f" ")
                 
            suma_1=0
            i+=1 
        else:
            if total >=20:
                print('\n'+" FELICITACIONES "+'\n')
                print('\n'+"GANADOR jugador 1 "+'\n')
                break
            elif total2 >=20:
                print('\n'+" FELICITACIONES "+'\n')
                print('\n'+"GANADOR jugador 2"+'\n')
                break
            elif total3 >=20:
                print('\n'+" FELICITACIONES "+'\n')
                print('\n'+"GANADOR jugador 3"+'\n')
                break
            elif total2 >=20:
                print('\n'+" FELICITACIONES "+'\n')
                print('\n'+"GANADOR jugador 4"+'\n')
                break
            elif total3 >=20:
                print('\n'+" FELICITACIONES "+'\n')                
                print('\n'+"GANADOR jugador 5"+'\n')
                break
                               
            print(f"turno {j}")
            j+=1 
            i=0 
            suma_1 = 0                
            print()
            seguir = input(
                "Pulse Intro para lanzar el dado. Pulse otra tecla e Intro para terminar: "
            )
        
    
    print("Bien jugado jugadores.")
    print("Desarrollado por. Brayan Rivera")


###############################

if __name__ == "__main__":
    main()


############################




        




        
            

    


    





 
