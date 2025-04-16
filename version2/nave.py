import pygame

class Nave():
    def __init__(self, ai_configuraciones,  pantalla):
        self.pantalla = pantalla
        self.ai_configuraciones = ai_configuraciones
        
        #cargar imagen y su hitbox
        self.imagen = pygame.image.load("imagenes/nave1.png")
        self.rect = self.imagen.get_rect()
        self.pantalla_rect = pantalla.get_rect()
        
        #nueva nave en la parte inferior central
        self.rect.centerx = self.pantalla_rect.centerx
        self.rect.bottom = self.pantalla_rect.bottom
        
        #almacena valores decimales
        self.center = float(self.rect.centerx)
        
        #movimiento
        self.moving_right = False
        self.moving_left = False
        
        
    def update(self):
        #actualizar posicion de la nave
        if self.moving_right and self.rect.right < self.pantalla_rect.right:
            self.center += self.ai_configuraciones.factor_velocidad_nave
        
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_configuraciones.factor_velocidad_nave
        
        #actualiza el objeto red desde selft center
        self.rect.centerx = self.center
           
    def blitme(self):
        #dibujado de la ubicacion
        self.pantalla.blit(self.imagen, self.rect)
        