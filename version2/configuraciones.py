class configuraciones(object):
    #almacena las configuraciones base
    def __init__(self):
        #inicia las config del juego
        self.screen_width = 800        
        self.screen_height = 600
        self.bg_color = (230, 130, 230)
        
        #configuraciones de la nave
        self.factor_velocidad_nave = 1.5
        