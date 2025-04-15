import sys
import pygame

from configuraciones import configuraciones
def run_game():
    
    #iniciar el juego y crear un objeto (la pantalla) y config
    pygame.init()
    ai_configuraciones = configuraciones()
    pantalla = pygame.display.set_mode(
        (ai_configuraciones.screen_width, ai_configuraciones.screen_heigth))
    pygame.display.set_caption("invacion alienigena")
    
    #iniciar el bucle del juego
    while True:
        
        #eventos del teclado
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                
        pantalla.fill(ai_configuraciones.bg_color)#mandar llamar el color de fondo
        
        #hacer visible la pantalla mas reciente
        pygame.display.flip()

run_game()