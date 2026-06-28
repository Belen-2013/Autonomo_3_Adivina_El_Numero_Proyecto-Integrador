
# Mensaje inicial
print("BIENVENIDOS AL JUEGO ADIVINA EL NÚMERO")

import random # Importa la librería que permite generar números aleatorios

# Genera un número secreto aleatorio entre 1 y 500
num_oculto= random.randint (1, 500)

# Variable que almacenará la cantidad de intentos realizados por el jugador
intentos= 0

# Mantiene el juego repitiéndose hasta que el usuario adivine el número
while True:
    Inicie_su_Intento= int(input("Ingrese su intento con números del 1 al 500:   "))

    intentos += 1   # Aumenta el contador cada vez que el usuario realiza un intento
    if Inicie_su_Intento == num_oculto:
        print("Felicitaciones, ¡lo lograste!")
        print("Lo adivinaste en", intentos, "Intentos")

        break   # Finaliza el ciclo while porque el juego terminó
    else:
        if Inicie_su_Intento > num_oculto:
            print("El número ingresado es mayor, intenta con un número menor")
        else:
            print("El número ingresado es bajo, intenta con un número mayor")
