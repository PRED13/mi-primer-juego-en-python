import sys
import pygame

def verificar_eventos_keydown(evento, nave):
    #respuesta a las teclas
    if evento.key == pygame.K_RIGHT:
        nave.moving_right = True
    elif evento.key == pygame.K_LEFT:
        nave.moving_left = True
            
def verificar_eventos_keyup(evento, nave):
    #respuesta a las teclas
    if evento.key == pygame.K_RIGHT:
        nave.moving_right = False
    elif evento.key == pygame.K_LEFT:
        nave.moving_left = False


def verificar_eventos(nave):
    #eventos de teclado y raton
    for evento in pygame.evento.get():  
        if evento.type == pygame.QUIT:
            sys.exit()
        elif evento.type == pygame.KEYDOWN:
            verificar_eventos_keydown(evento, nave)
                
        elif evento.type == pygame.KEYUP:
            verificar_eventos_keyup(evento, nave)

def actualizar_pantalla(ai_configuraciones, pantalla, nave):
        #actualizar imagenes
        pantalla.fill(ai_configuraciones.bg_color)#mandar llamar el color de fondo
        nave.blitme()
        #hacer visible la pantalla mas reciente
        pygame.display.flip()