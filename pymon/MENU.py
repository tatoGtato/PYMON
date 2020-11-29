# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 19:15:17 2020

@author: Acer
"""

import pygame, sys
from pygame.locals import *
import character_select


pygame.init()

#surface
mysurface = pygame.display.set_mode((1920,1080))
pygame.display.set_caption("PYMON")

#IMAGEN
paisaje = pygame.image.load("IMAGENES/fondopix.png")
fondo = pygame.transform.scale(paisaje, (1920,1080))

#megafono
megafono = pygame.image.load("IMAGENES/megafono.png")
megafono_scaled = pygame.transform.scale(megafono, (200,200))

megafono_silenciado = pygame.image.load("IMAGENES/megafono_silenciado.png")
megafonosc_scaled = pygame.transform.scale(megafono_silenciado, (200,200))


#icono
icono = pygame.image.load("IMAGENES/icono.png")
pygame.display.set_icon(icono)

#texto
my_font = pygame.font.Font("FUENTES/fuente1.ttf", 180)

my_font2 = pygame.font.Font("FUENTES/fuente1.ttf", 20)

my_font3 = pygame.font.Font("FUENTES/fuente1.ttf", 100)


#TEXTO BOTONES
letra_boton1 = pygame.font.Font("FUENTES/fuente1.ttf", 50)

letra_boton2 = pygame.font.Font("FUENTES/fuente1.ttf", 40)

#TEXTO EXTRAS
name_font = pygame.font.Font("FUENTES/fuente1.ttf", 50)


#SONIDOS
click_menu = pygame.mixer.Sound("Sonidos/boton_menu.mp3")

esc_sound = pygame.mixer.Sound("Sonidos/esc_sound.mp3")




def menu_principal ():
    click = False
    while True:
        
        
        #DEFINIR EL FONDO CON LA FOTO
        mysurface.blit(fondo, (0,0))
        
        #TEXTO
        texto = my_font.render("PYMON", True, (255, 255, 255))
        mysurface.blit(texto, (400,100))

        #SE RECOGE LA POSICION DEL MOUSE
        mx, my = pygame.mouse.get_pos()
        
        #SE CREAN LOS BOTONES
        button_1 = pygame.Rect(760, 800, 500, 125)
        button_2 = pygame.Rect(760, 600, 500, 125)
        
        #SE DIBUJAN LOS BOTONES
        pygame.draw.rect(mysurface, (39, 57, 161), button_1)
        pygame.draw.rect(mysurface, (39, 57, 161), button_2)
        
        #DETALLES BOTON
        detalles_button1 = pygame.Rect(780, 820, 460, 90)
        detalles_button2 = pygame.Rect(780, 620, 460, 90)
        
        pygame.draw.rect(mysurface, (0,0,0),  detalles_button1)
        pygame.draw.rect(mysurface, (0,0,0), detalles_button2)
        
        #TEXTO PARA IR A OPCIONES
        texto = letra_boton1.render("JUGAR", True, (255, 255, 255))
        mysurface.blit(texto, (840,630))
        
        #TEXTO PARA IR EL JUEGO
        texto = letra_boton2.render("OPCIONES", True, (255, 255, 255))
        mysurface.blit(texto, (790,825))
        
        
        #SE VE SI SE CLICKEA EL BOTON
        if button_2.collidepoint((mx, my)):
            if click:
                pygame.mixer.Sound.play(click_menu)
                character_select.characters()
                
        if button_1.collidepoint((mx, my)):
            if click:
                pygame.mixer.Sound.play(click_menu)
                opciones()

        click = False    
        
        #EVENTOS
        for event in pygame.event.get():   
            #PARA CERRAR
            if event.type == pygame.QUIT:
                pygame.quit()
                pygame.sys.exit()
             
            #PARA VER SI SE CLICKEA    
            if event.type == pygame.MOUSEBUTTONDOWN:  
                if event.button == 1:
                    click = True
                    
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    pygame.sys.exit()

        pygame.display.update()

        
      
def opciones():
    x = 0
    click = False 
    running = True
    while running:
        
        
        #FONDO DE PANTALLA
        mysurface.blit(fondo, (0,0))
        
         
        #TEXTO TITULO
        texto = my_font3.render("OPCIONES", True, (255, 255, 255))
        mysurface.blit(texto, (150,100))
        
        #SE RECOGE LA POSICION DEL MOUSE
        mx2, my2 = pygame.mouse.get_pos()
        
        #SE CREAN LOS BOTONES
        button_EXTRA = pygame.Rect(760, 800, 500, 125)
        button_SONIDOS = pygame.Rect(760, 600, 500, 125)
        
        #SE DIBUJAN LOS BOTONES
        pygame.draw.rect(mysurface, (39, 57, 161), button_EXTRA)
        pygame.draw.rect(mysurface, (39, 57, 161), button_SONIDOS)
        
        #DETALLES BOTON
        detalles_buttonE = pygame.Rect(780, 820, 460, 90)
        detalles_buttonS = pygame.Rect(780, 620, 460, 90)
        
        pygame.draw.rect(mysurface, (0,0,0),  detalles_buttonE)
        pygame.draw.rect(mysurface, (0,0,0), detalles_buttonS)

        #TEXTO PARA IR A OPCIONES
        texto = letra_boton2.render("SONIDOS", True, (255, 255, 255))
        mysurface.blit(texto, (820,630))
        
        #TEXTO PARA IR EL JUEGO
        texto = letra_boton2.render("EXTRAS", True, (255, 255, 255))
        mysurface.blit(texto, (840,825))
        
        #MEGAFONO    
        mysurface.blit(megafono_scaled, (1250,560))
        
        mysurface.blit(megafonosc_scaled, (1250,560))

        
        #SE VE SI SE CLICKEA EL BOTON
        if x == 0:
            if button_SONIDOS.collidepoint((mx2, my2)):
                if click:
                                   
                    global z, f
                
                    pygame.mixer.Sound.play(click_menu) 
                
                    megafono_scaled.set_alpha(0)                
                    megafonosc_scaled.set_alpha(255)
                
                    z = esc_sound.set_volume(0.0)
                    f = click_menu.set_volume(0.0)
                    
                    x = 1
                
                
        elif x == 1:     
            if button_SONIDOS.collidepoint((mx2, my2)):
                if click:
                
                    x = 1
                    global z2, f2
                
                    pygame.mixer.Sound.play(click_menu) 
                
                    megafono_scaled.set_alpha(255)                
                    megafonosc_scaled.set_alpha(0)
                
                    z2 = esc_sound.set_volume(1.0)
                    f2 = click_menu.set_volume(1.0)
                    
                    x = 0
        
        
                    
                
        if button_EXTRA.collidepoint((mx2, my2)):
            if click:
                pygame.mixer.Sound.play(click_menu)
                extras()

                
        click = False
        
        #EVENTOS
        for event in pygame.event.get():
            #PARA SALIR
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            #PARA VER SI SE CLICKEA    
            if event.type == pygame.MOUSEBUTTONDOWN:  
                if event.button == 1:
                    click = True
                    
            #para regresar al menu
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.mixer.Sound.play(esc_sound)
                    running = False
                
        pygame.display.update()    
        
def extras():
    y = 0
    y_A = 260
    y_Ar = 460
    y_V = 660
    
    running = True
    while running:
        
        
        #FONDO DE PANTALLA
        mysurface.blit(fondo, (0,y))
        y -= 1
         
        #texto
        Aillon = name_font.render("Santiago Aillon", True, (255, 255, 255))        
        mysurface.blit(Aillon, (560,y_A))
        y_A -=1
        
        Arevalo = name_font.render("Santiago Arevalo", True, (255, 255, 255))        
        mysurface.blit(Arevalo, (560,y_Ar))
        y_Ar -=1
        
        Hernandez = name_font.render("Valentina Hernandez", True, (255, 255, 255))        
        mysurface.blit(Hernandez, (560,y_V))
        y_V -=1
        
        if (y == -1080):
            running = False

        #EVENTOS
        for event in pygame.event.get():
            #PARA SALIR
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            #para regresar al menu
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.mixer.Sound.play(esc_sound)
                    running = False
                
        pygame.display.update()  

        
        
menu_principal()        
        

      
        
        