# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 09:59:51 2020

@author: santi
"""

"Character select screen"

import pygame,sys
from pygame.locals import *
import time
import Game

pygame.init()
size = width,height = 1920,1080



class Pollo:
    def __init__(self):
        self.atributo = "Pollo"
        self.imagen = pygame.image.load("IMAGENES/Seleccion_de_personajes/SPRITE_POLLO1.png")
        
        
    def __str__(self):
        texto = "soy un {0}".format(self.atributo)
        return texto
    


class Mago:
    def __init__(self):
        self.atributo = "Mago"
        self.imagen = pygame.image.load("IMAGENES/Seleccion_de_personajes/SPRITE_MAGA3.png")
        self.imagen_vol = pygame.transform.flip(self.imagen, True, False)
        
    def __str__(self):
        texto = "soy un {0}".format(self.atributo)
        return texto
    
    
class Espada:
    def __init__(self):
        self.atributo = "Espada"
        self.imagen = pygame.image.load("IMAGENES/Seleccion_de_personajes/SPRITE_ESPADA2.png")
        self.imagen_vol = pygame.transform.flip(self.imagen, True, False)
        
    def __str__(self):
        texto = "soy un {0}".format(self.atributo)
        return texto
            
        
    
#CLASES (TIPOS DE PERSONAJE)
a = Pollo()
b = Mago()
c = Espada()

#MARCOS PARA ELEGIR PERSONAJE
m_azul = pygame.image.load("IMAGENES/Seleccion_de_personajes/Marco_Azul.png")
m_azul_chs = pygame.image.load("IMAGENES/Seleccion_de_personajes/Marco_Azul_chs.png")

m_verde = pygame.image.load("IMAGENES/Seleccion_de_personajes/Marco_verde.png")
m_verde_chs = pygame.image.load("IMAGENES/Seleccion_de_personajes/Marco_verde_chs.png")

a.imagen = pygame.transform.scale(a.imagen,(300,300))
a.imagen_vol = pygame.transform.scale(a.imagen,(300,300))

b.imagen = pygame.transform.scale(b.imagen,(300,300))
c.imagen = pygame.transform.scale(c.imagen,(300,300))


m_azul = pygame.transform.scale(m_azul ,(300,300))
m_azul_chs = pygame.transform.scale(m_azul_chs,(300,300))
m_azul_chs.set_alpha(0)

m_verde = pygame.transform.scale(m_verde ,(300,300))
m_verde_chs = pygame.transform.scale(m_verde_chs ,(300,300))
m_verde_chs.set_alpha(0)

#SONIDOS
click_character = pygame.mixer.Sound("Sonidos/seleccion_char.wav")

esc_sound = pygame.mixer.Sound("Sonidos/esc_sound.mp3")



fondo_select = pygame.image.load("IMAGENES/Seleccion_de_personajes/fondo2pix.png")


def characters():
    
    x1 = 380
    x2 = 380
    screen = pygame.display.set_mode(size)   
    selection = True
    selected = False 
    selected2 = False
    move = False
    
    while selection:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.mixer.Sound.play(esc_sound)
                    selection = False
                    
                elif event.key == K_e:
                    selected = True
                    m_azul.set_alpha(0)                
                    m_azul_chs.set_alpha(255)
                    pygame.mixer.Sound.play(click_character)

                elif event.key == K_p:
                    selected2 = True  
                    m_verde.set_alpha(0)                
                    m_verde_chs.set_alpha(255)
                    pygame.mixer.Sound.play(click_character)
                    
                elif event.key == K_d:
                    if selected == False:
                        if x1 == 1260:
                            x1 = 380 
                        else:
                            x1 += 440
                elif event.key == K_a:
                    if selected == False:
                        if x1 == 380:
                            x1 = 1260
                        else:
                            x1 -= 440
                elif event.key == K_RIGHT:
                    if selected2 == False:
                        if x2 == 1260:
                            x2 = 380 
                        else:
                            x2 += 440
                elif event.key == K_LEFT:
                    if selected2 == False:
                        if x2 == 380:
                            x2 = 1260
                        else:
                            x2 -= 440
                    
                    

        screen.blit(fondo_select, (0,0))  
                           
        screen.blit(m_azul,(x1,328))        
        screen.blit(m_azul_chs,(x1,328))
        
        screen.blit(m_verde,(x2,328))
        screen.blit(m_verde_chs,(x2,328))
        
        screen.blit(a.imagen,(380,340))
        screen.blit(b.imagen,(820,366))
        screen.blit(c.imagen,(1260,310))
        
        if selected and selected2:
            if x1 == 380:
                p1 = a
            elif x1 == 820:
                p1 = b
            elif x1 == 1260:
                p1 = c
            if x2 == 380:
                p2 = a
            elif x2 == 820:
                p2 = b
            elif x2 == 1260:
                p2 = c
                
                
            Game.battle(p1,p2)
            
            screen.fill((0,0,0))
            
            selected = False
            selected2 = False
            selection = False
        
    
            
        pygame.display.update()






        
   
    
   
