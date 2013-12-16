# # # # # # # # # # # # # # # # # #
#  Clases usadas para el juego    #
#    Autor: Genesis Guerrero      #
#    Fecha: 14/12/11              #   
# # # # # # # # # # # # # # # # # #

import pygame

class sujeto(pygame.sprite.Sprite):
    """De esta clase heredan los objetos vivientes"""    
    def __init__(self, imagenes):        
        self.imagenes = imagenes        
        self.frame = 0   
        self.indicador = 30     
        self.rect = self.imagenes[self.frame].get_rect()
        self.rect.top = 300
        self.rect.left = 40        
    def move(self, vx,vy):
        self.rect.move_ip(vx,vy)
    def update(self, superficie):
        superficie.blit(self.imagenes[self.frame],self.rect)   
    def nextFrame(self):  
        self.frame = self.indicador % len(self.imagenes) #controla los indices de las imagenes
        self.indicador+=1   #sigue a la imagen siguiente
    def setNewSprites(self,imagenes):
        self.imagenes = imagenes    
        
class Player(sujeto):
    """Clase del heroe"""
    def __init__(self, imagenes):        
        sujeto.__init__(self,imagenes)        
    def getLife():
        return self.life  
""" 
class enemy(sujeto):    
    def __init__(self):
        sujeto.__init__(self,imagenes)
        self.vivo = True
    def getEstado():
        return vivo
    def morir():
        vivo = False
    def nacer():
        vivo = True
"""    
