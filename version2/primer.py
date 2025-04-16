import pygame

from configuraciones import configuraciones

from nave import Nave

import funciones_juego as fj

def run_game():
    #iniciar el juego y crear un objeto (la pantalla) y config
    pygame.init()
    ai_configuraciones = configuraciones()
    pantalla = pygame.display.set_mode(
        (ai_configuraciones.screen_width, ai_configuraciones.screen_height))
    pygame.display.set_caption("invacion alienigena")
    
    #crear la nave
    nave = Nave(pantalla)
    
    #iniciar el bucle del juego
    while True:
        #eventos del teclado
        fj.verificar_eventos(nave)
        nave.update()
        fj.actualizar_pantalla(ai_configuraciones, pantalla, nave)
        
        
run_game()