# # # # # # # # # # # # # # # # # # # # # # #
#                                           #
#           SPONJEBOB ATTACK                #
#    * Modulo principal del juego           #
#    * Autor: Genesis Guerrero              #
#    * Fecha: 14/12/11                      # 
#    * Web:http://pinguinazos.blogspot.com/ #  
#                                           #  
# # # # # # # # # # # # # # # # # # # # # # #


import pygame
import sujetos
import os

# Constantes
ANCHO = 640
ALTO = 480
# Fin constantes

# Inicializaciones y variables globales
pygame.init()
screen = pygame.display.set_mode((ANCHO,ALTO))
pygame.display.set_caption("SponjeBob Attack")
reloj = pygame.time.Clock()
# Fin Inicializaciones


# Funciones

# Carga las imagenes
def load_img(nombre, directorio):
    ruta = os.path.join(directorio,nombre)
    try:
        image = pygame.image.load(ruta)
    except:
        print "Error! no se puede cargar la imagen"
    return image.convert_alpha()       

imagenesPlayerDer = [load_img("walkr1.png","Res"),load_img("walkr2.png","Res"),
                     load_img("walkr3.png","Res"),load_img("walkr4.png","Res"),
                     load_img("walkr5.png","Res"),load_img("walkr6.png","Res"),]    
imagenesPlayerIzq = [load_img("walkl1.png","Res"),load_img("walkl2.png","Res"),
                     load_img("walkl3.png","Res"),load_img("walkl4.png","Res"),
                     load_img("walkl5.png","Res"),load_img("walkl6.png","Res"),]
imagenFondo = load_img("fondo.png","Res")
                     
# Pinta las imagenes en la pantalla                     
def paint(player):
    screen.blit(imagenFondo,[0,0])
    player.update(screen)
    pygame.display.update()
    player.nextFrame()

# Definicion main 
def main():   
        
    spritesRight = True
                            
    player = sujetos.Player(imagenesPlayerDer)    
    exit = False   
    vx = 15
    
    while exit != True:     # Bucle principal
        paint(player)        
        player.move(vx,0)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:                
                exit = True
                
        # control de los limites   
        if player.rect.left >= ANCHO or player.rect.left <= 0:
            vx=-vx
            if spritesRight == True:  #si mira hacia la derecha
                player.setNewSprites(imagenesPlayerIzq)
                spritesRight = False
            else: #si mira hacia la izquierda
                player.setNewSprites(imagenesPlayerDer)
                spritesRight = True     
        reloj.tick(12)
    pygame.quit()
# Fin Funciones

# INICIO
if __name__ == '__main__':
    main()
