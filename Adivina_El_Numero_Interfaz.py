import pygame
import random

# Iniciar pygame
pygame.init()

# Crear pantalla
pantalla = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Adivina el número")


# Colores
AZUL = (30, 90, 180)
AZUL_OSCURO = (20, 50, 120)
BLANCO = (255, 255, 255)
DORADO = (255, 220, 80)


# Fuentes
fuente_titulo = pygame.font.Font(None, 55)
fuente = pygame.font.Font(None, 35)


# Número secreto
num_oculto = random.randint(1, 500)

intentos = 0
numero = ""

mensaje = "Ingresa un numero del 1 al 500"


# Números decorativos del fondo
numeros_fondo = ["5", "25", "100", "250", "500"]


# Ciclo principal
jugando = True

while jugando:

    # Fondo
    pantalla.fill(AZUL)


    # Dibujar números del fondo
    for i, n in enumerate(numeros_fondo):
        texto = fuente.render(n, True, (70,150,230))
        pantalla.blit(texto, (50 + i*120, 20))


    # Título
    titulo = fuente_titulo.render(
        "ADIVINA EL NUMERO",
        True,
        BLANCO
    )

    pantalla.blit(titulo, (120,70))


    # Cuadro del número
    pygame.draw.rect(
        pantalla,
        AZUL_OSCURO,
        (150,140,300,60),
        border_radius=15
    )


    texto_numero = fuente.render(
        "Numero: " + numero,
        True,
        DORADO
    )

    pantalla.blit(texto_numero,(190,155))


    # Cuadro del mensaje
    pygame.draw.rect(
        pantalla,
        AZUL_OSCURO,
        (60,220,480,70),
        border_radius=15
    )


    texto_mensaje = fuente.render(
        mensaje,
        True,
        BLANCO
    )

    pantalla.blit(texto_mensaje,(80,240))


    # Intentos
    texto_intentos = fuente.render(
        "Intentos: " + str(intentos),
        True,
        BLANCO
    )

    pantalla.blit(texto_intentos,(220,330))


    # Eventos
    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            jugando = False


        if evento.type == pygame.KEYDOWN:


            # Escribir números
            if evento.unicode.isdigit():
                numero += evento.unicode


            # Borrar
            if evento.key == pygame.K_BACKSPACE:
                numero = numero[:-1]


            # Enter
            if evento.key == pygame.K_RETURN:


                if numero != "":

                    intentos += 1

                    intento = int(numero)


                    if intento == num_oculto:

                        mensaje = "Felicitaciones, ¡lo lograste!"


                    elif intento > num_oculto:

                        mensaje = "El número ingresado es mayor,\nintenta con un número menor"


                    else:

                        mensaje = "El número ingresado es bajo, \n intenta con un número mayor"


                    numero = ""


    pygame.display.update()


pygame.quit()
