# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 18:37:46 2020

@author: santi
"""
import pygame, sys, Animaciones,random
from pygame.locals import *
pygame.init()

size = width,height = 1920,1080 #Tamaño de la pantalla


global x1 #Variables que se utiliza para marcar puntos de vida
x1 = 500 #Se hacen globales dado a que se utiliza en todo el codigo

global x2 
x2 = 500

def battle(player1, player2): #Se define la funcion que tiene todo el juego con dos argumentos de entrada
                              #Los argumentos son objetos siendo los personajes de ambos jugadoes 
                              
    global screen #Al igual que 
    
    #Invoca la pantalla 
    screen = pygame.display.set_mode(size) 
    
    #Las variables a,b,c,d son las imágenes de la barra de vida, siendo a,c la parte de afuera 
    #y b,c las que se modifican para ver la vida restante
    a1 = pygame.image.load("IMAGENES/Elementos_Juego_Prueba/Barra_vida_roja_1.png")
    a = pygame.transform.scale(a1, (500, 100))
    
    b = pygame.image.load("IMAGENES/Elementos_Juego_Prueba/Barra_vida_verde_1.png")
    
    c1 = pygame.image.load("IMAGENES/Elementos_Juego_Prueba/Barra_vida_roja_2.png")
    c = pygame.transform.scale(c1, (500, 100))
    
    d = pygame.image.load("IMAGENES/Elementos_Juego_Prueba/Barra_vida_verde_2.png")
    
    corazon1 = pygame.image.load("IMAGENES/Elementos_Juego_Prueba/Corazon_1.png")
    corazon = pygame.transform.scale(corazon1, (500, 100))
    corazon2 = pygame.transform.scale(corazon1, (500, 100))
    
    #Imagenes que demarcan las opciones/controles del jugador 1
    C_1 = pygame.image.load("IMAGENES/Elementos_Juego_Prueba/Boton_Q.png")
    C1 = pygame.transform.scale(C_1, (700, 600))
    
    C_2 = pygame.image.load("IMAGENES/Elementos_Juego_Prueba/Boton_W.png")
    C2 = pygame.transform.scale(C_2, (700, 600))
    
    C_3 = pygame.image.load("IMAGENES/Elementos_Juego_Prueba/Boton_E.png")
    C3 = pygame.transform.scale(C_3, (700, 600))
    
    C_4 = pygame.image.load("IMAGENES/Elementos_Juego_Prueba/Boton_R.png")
    C4 = pygame.transform.scale(C_4, (700, 600))
    
    
    #Imagenes que demarcan las opciones/controles del jugador 2   
    C_5 = pygame.image.load("IMAGENES/Elementos_Juego_Prueba/Boton_U.png")
    C5 = pygame.transform.scale(C_5, (700, 600))
    
    C_6 = pygame.image.load("IMAGENES/Elementos_Juego_Prueba/Boton_I.png")
    C6 = pygame.transform.scale(C_6, (700, 600))
    
    C_7 = pygame.image.load("IMAGENES/Elementos_Juego_Prueba/Boton_O.png")
    C7 = pygame.transform.scale(C_7, (700, 600))
    
    C_8 = pygame.image.load("IMAGENES/Elementos_Juego_Prueba/Boton_P.png")
    C8 = pygame.transform.scale(C_8, (700, 600))
    
    #SONIDOS
    botton_ataque = pygame.mixer.Sound("Sonidos/seleccion_ataque.wav")
    
    
    #FONDO DEL JUEGO
    fondo_pelea = pygame.image.load("IMAGENES/Fondo_Pelea.png")
    
    #Texto
    letra_jugadores = pygame.font.Font("FUENTES/fuente1.ttf", 25)
    
    #Variables para determinar el turno de los jugadores y las acciones que se hacen en respestivo turno 
    turno = True  
    pelea = False

    #Variable que reciben las opciones de cada jugador
    A1 = None
    A2 = None
    
    #Variable que mantiene el juego en movimiento
    game_on = True
    

    while game_on: 
        #Eventos 
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                    
        #Fin del juego     
        #Se usan las variables globales x1 y x2 para determinar el fin del juego
        #La primera x que sea menor o igual a 50 juega una animación final y acaba el juego               
        if x1 <= 100 or x2 <= 100:
            
            game_on = False  
            
            
        #Se ponen los "asets"  del juego, siendo las barras de vida y los personajes    
        screen.blit(fondo_pelea, (0,0))        
        
        b = pygame.transform.scale(b,(x1,100)) #Se usan las variables globales para determinar la escala en x
        d = pygame.transform.scale(d,(x2,100)) #Esta es la barra que decrece cada ves que alguno pierde vida 
        
        screen.blit(a, (51,100)) #se muestran barras de vida 
        screen.blit(b, (51,100))
        screen.blit(c, (1391,100))
        screen.blit(d, (1391,100))
        
        screen.blit(corazon, (51,100))
        screen.blit(corazon2, (1391,100))
        
        screen.blit(player1.imagen, (550, 370)) #Se muestran los jugadores
        
        imagen_vol = pygame.transform.flip(player2.imagen, True, False)
        
        screen.blit(imagen_vol, (1340,360))
        
        
        if turno: #Turno del jugador 1
        
            jugador1 = letra_jugadores.render("Turno del jugador 1", True, (255, 255, 255))
            screen.blit(jugador1, (25,25))
        
            screen.blit(C1,(360,470))  #Se muestran opciones del jugador 1 
            screen.blit(C2,(800,470))
            screen.blit(C3,(360,650))
            screen.blit(C4,(800,650))
            
            #Eventos de jugador 1, el programa verifica si se ha oprimido alguna tecla 
            #Cuando elige cualquier opción, habilita el turno del siguiente jugador y asigna un valor a A1
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_q:    #Elije el ataque especial 
                        A1 = 1 
                        pygame.mixer.Sound.play(botton_ataque)
                        turno = False
                        
                    elif event.key == K_w:   #Elije el ataque básico 
                        A1 = 2
                        pygame.mixer.Sound.play(botton_ataque)
                        turno = False    
                           
                    elif event.key == K_e:  #Elije defensa
                        A1 = 3
                        pygame.mixer.Sound.play(botton_ataque)
                        turno = False
                        
                    elif event.key == K_r:   #Elije Chance time 
                        A1 = 4   
                        pygame.mixer.Sound.play(botton_ataque)
                        turno = False 

            
        
        if turno == False: #Turno del jugador 
        
            jugador2 = letra_jugadores.render("Turno del jugador 2", True, (255, 255, 255))
            screen.blit(jugador2, (1350,25))
            
            screen.blit(C5,(360,470))
            screen.blit(C6,(800,470))
            screen.blit(C7,(360,650))
            screen.blit(C8,(800,650))
            
             
            #Eventos de jugador 2, el programa verifica si se ha oprimido alguna tecla 
            #Cuando elige cualquier opción, habilita la animacion de ataque y asigna un valor a A2
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_u:  #Elije el ataque especial 
                        A2 = 1
                        pygame.mixer.Sound.play(botton_ataque)
                        pelea = True
                        
                    elif event.key == K_i: #Elije el ataque básico 
                        A2 = 2
                        pygame.mixer.Sound.play(botton_ataque)
                        pelea = True
                        
                    elif event.key ==K_o:  #Elije defensa
                        A2 = 3
                        pygame.mixer.Sound.play(botton_ataque)
                        pelea = True
                        
                    elif event.key == K_p: #Elije Chance time 
                        A2 = 4 
                        pygame.mixer.Sound.play(botton_ataque)
                        pelea = True
         
        
            
        if pelea:  #Se activa la animacion con los ataques (desiciones) de los jugadores 
                   #A2 representan las aciones del jugador 2; A1 las del jugador. 
                   #Cada condicional es 1 de las 16 combinaciones que se pueden elejir. 
                   #Estan evauadas sobre el jugador 2, es decir, el primer bloque, por ejemplo,
                   #cuando el jugador 2 elije a, se compara con las cuatro posibilidades que
                   #tiene el jugador 1 para elejir
        
        
        
            if A2 == 1 and A1 == 1:
                Animaciones.AtaqueS1(player1,player2,a,b,c,d,corazon,corazon2,C1,C5) #Cada bloque es similar, invocan las funciones relacionadas
                Special1(player1,player2)                      #con las desiciones de cada jugado, luego se reinician cada variable
                
                Animaciones.AtaqueS2(player1,player2,a,b,c,d,corazon,corazon2,C1,C5) #para que vuelva a repetirse cada proceso.
                Special2(player1,player2)
                pelea = False
                turno = True
                A1 = None
                A2 = None
                
            elif A2 == 1 and A1 == 2:
                Animaciones.AtaqueS1(player1,player2,a,b,c,d,corazon,corazon2,C2,C5)
                Basic1()
                Animaciones.AtaqueS2(player1,player2,a,b,c,d,corazon,corazon2,C2,C5)
                Special2(player1,player2)
                pelea = False
                turno = True
                A1 = None
                A2 = None
            elif A2 == 1 and A1 == 3:
                Animaciones.Defensa1(player1,player2,a,b,c,d,corazon,corazon2,C3,C5)
                Defence1()
                pelea = False
                turno = True
                A1 = None
                A2 = None
            elif A2 == 1 and A1 == 4:
                Animaciones.AtaqueS2(player1,player2,a,b,c,d,corazon,corazon2,C4,C5)
                Special2(player1,player2)
                pelea = False
                turno = True
                A1 = None
                A2 = None
                
            elif A2 == 2 and A1 == 1:
                Animaciones.AtaqueS1(player1,player2,a,b,c,d,corazon,corazon2,C1,C6)
                Special1(player1,player2)
                Animaciones.AtaqueS2(player1,player2,a,b,c,d,corazon,corazon2,C1,C6)
                Basic2()
                pelea = False
                turno = True
                A1 = None
                A2 = None
                
            elif A2 == 2 and A1 == 2:
                Animaciones.AtaqueS1(player1,player2,a,b,c,d,corazon,corazon2,C2,C6)
                Basic1()
                Animaciones.AtaqueS2(player1,player2,a,b,c,d,corazon,corazon2,C2,C6)
                Basic2()
                pelea = False
                turno = True
                A1 = None
                A2 = None
                
            elif A2 == 2 and A1 == 3:
                Animaciones.Defensa1(player1,player2,a,b,c,d,corazon,corazon2,C3,C6)
                Defence1()
                pelea = False
                turno = True
                A1 = None
                A2 = None
                
            elif A2 == 2 and A1 == 4:
                Animaciones.AtaqueS2(player1,player2,a,b,c,d,corazon,corazon2,C4,C6)
                Basic2()
                pelea = False
                turno = True
                A1 = None
                A2 = None
                
            elif A2 == 3 and A1 == 1:
                Animaciones.Defensa2(player1,player2,a,b,c,d,corazon,corazon2,C1,C7)
                Defence2()
                pelea = False
                turno = True
                A1 = None
                A2 = None
                
            elif A2 == 3 and A1 == 2:
                Animaciones.Defensa2(player1,player2,a,b,c,d,corazon,corazon2,C2,C7)
                Defence2()
                pelea = False
                turno = True
                A1 = None
                A2 = None
                
            elif A2 == 3 and A1 == 3:
                Animaciones.Defensa3(player1,player2,a,b,c,d,corazon,corazon2,C3,C7)
                Defence1()
                Defence2()
                pelea = False
                turno = True
                A1 = None
                A2 = None
                
            elif A2 == 3 and A1 == 4:
                Animaciones.Defensa4(player1,player2,a,b,c,d,corazon,corazon2,C4,C7,A2,A1)
                Defence2()
                pelea = False
                turno = True
                A1 = None
                A2 = None
                
            elif A2 == 4 and A1 == 1:
                Animaciones.AtaqueS1(player1,player2,a,b,c,d,corazon,corazon2,C1,C8)
                Special1(player1,player2)
                pelea = False
                turno = True
                A1 = None
                A2 = None
                
            elif A2 == 4 and A1 == 2:
                Animaciones.AtaqueS1(player1,player2,a,b,c,d,corazon,corazon2,C2,C8)
                Basic1()
                pelea = False
                turno = True
                A1 = None
                A2 = None
                
            elif A2 == 4 and A1 == 3:
                Animaciones.Defensa4(player1,player2,a,b,c,d,corazon,corazon2,C3,C8, A2,A1)
                Defence1()
                pelea = False
                turno = True
                A1 = None
                A2 = None
                
            elif A2 == 4 and A1 == 4:
                num = random.randrange(1,8,1) #Genera el numero aleatorio para el chance time
                ChanceTime(num)
                Animaciones.ChanceTimeA(player1,player2,num)
                pelea = False
                turno = True
                A1 = None
                A2 = None

            
        pygame.display.update()
   

                  
    while game_on == False:  #Pantalla final del juego, simplemente muestra "Game Over" y se sale del codigo cuando se oprime alguna de las opciones
        
        Animaciones.finito(player1,player2,x1,x2)
        
    pygame.quit()              
                     
 
    
def Special1(player1,player2): #Función que retorna el resultado de vida del jugador 2 cuando el juegador 1 elije el ataque especial.
        global x2
         #Compara los atributos de ambos objetos 
        if player1.atributo != player2.atributo: #De ser diferente utiliza alguna de las combinaciones para determinar el daño
            if player1.atributo == "Pollo":
                if player2.atributo == "Mago":
                    x2 -= 50
                    return x2
                elif player2.atributo == "Espada":
                    x2 -=25
                    return x2
            elif player1.atributo == "Mago":
                if player2.atributo == "Espada":
                    x2 -= 50
                    return x2
                elif player2.atributo == "Pollo":
                    x2 -= 25
                    return x2           
            elif player1.atributo == "Espada":
                if player2.atributo == "Pollo":
                    x2 -= 50
                    return x2
                elif player2.atributo == "Mago":
                    x2 -=25
                    return x2
        elif player1.atributo == player2.atributo: #De ser igual tambien genera daño, diferente a al¿¿las opciones anteriores
            x2 -= 25
            return x2
          

   
        
def Special2(player1,player2): #Función que retorna el resultado de vida del jugador 1 cuando el juegador 2 elije el ataque especial.
          global x1
           #Compara los atributos de ambos objetos 
          if player2.atributo != player1.atributo:#De ser diferente utiliza alguna de las combinaciones para determinar el daño
            if player2.atributo == "Pollo":
                if player1.atributo == "Mago":
                    x1 -= 50
                    return x1
                elif player1.atributo == "Espada":
                    x1 -=25
                    return x1
            elif player2.atributo == "Mago":
                if player1.atributo == "Espada":
                    x1 -= 50
                    return x1
                elif player1.atributo == "Pollo":
                    x1 -= 25  
                    return x1                              
            elif player2.atributo == "Espada":
                if player1.atributo == "Pollo":
                    x1 -= 50
                    return x1
                elif player1.atributo == "Mago":
                    x1 -=25
                    return x1
          elif player2.atributo == player1.atributo:#De ser igual tambien genera daño, diferente a al¿¿las opciones anteriores
                 x1 -= 25
                 return x1
    
    
    
    
#Funciones que retorna el resultado del daño cuando alguno de los personajes eljie el ataque básico     
def Basic1(): 
    global x2
    x2 -= 37
    return x2
    
def Basic2():
    global x1
    x1 -= 37
    return x1    


#Funciones que retorna el resultado del daño cuando alguno de los personajes eljie defensa  
def Defence1():
    global x1
    x1 += 0
    return x1

def Defence2():
    global x2
    x2 += 0
    return x2





#Funciones que retorna un efecto aleatorio para alguno de los personajes 
#recibe un numero aleatorio como argumento
def ChanceTime(num):
    global x1,x2
    if num ==1:
        
        if x1 > 380 and x1 <= 450:
            x1 += 50
            return x1,num
        elif x1 <= 380:
            x1 += 120            
            return x1,num
        
    elif num == 2:
        x2 -= 120
        return x2,num
    
    elif num == 5:
        if x2 > 380 and x2 <= 450:
            x2 += 50
            return x2,num
        elif x2 <= 380:
            x2 += 120
            return x2,num 
        
    elif num == 6:
        x1 -= 120
        return x1,num
    
    else:
        return x1,x2,num
        

