import pygame
import sys
from pygame.sprite import Sprite

class bala(Sprite):
    def __init__(self, ai_configuraciones, pantalla, nave):
        super (bala, self).__init__()
        self.pantalla = pantalla
        #bala rect en 0,0 y establecer posicion
        self.rect = pygame.rect(0,0, ai_configuraciones.bala_width,
                                ai_configuraciones.bala_height)
        self.rect.centerx = nave.rect.centerx
        self.rect.top = self.rect.top
        
        #valor decimal para la bala
        self.y = float(self.rect.y)
        
        self.color = ai_configuraciones.bala_color
        self.factor_velocidad = ai_configuraciones.bala_factor_velocidad