#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
import random
import os, sys 
# Importar módulo gráfico windows
os.environ['SDL_VIDEODRIVER'] = 'windib'

def main():
    pygame.init() # Inicilizar los módulos de pygame
    salir_event = False
    marcador = 0
    segundor = 0
    finJuego = False
    detener_sonido_final = False
    directorio_aplicacion = os.getcwd()
    directorio_recursos = directorio_aplicacion + '\\resources'
    directorio_sonidos = directorio_recursos + '\\sound'
    directorio_imagenes = directorio_recursos + '\\img'

    # Un reloj evita que el programa compruebe los eventos
    # recursivamente desaprovechando recursos
    time_event_1 = pygame.time.Clock()
    time_screen = pygame.time.Clock()

    # Asignar equiqueta ventana
    pygame.display.set_caption("Teste Pygame")

    screen = definir_tamano_screen() # Asignar tamaño (ancho,algo) defecto (500,500)
    screen_color = devolver_color("Gris") # Asignar color
    screen.fill(screen_color) # Asignar el color de fondo

    subscreen1 = definir_tamano_surface() # Crear  superficie (ancho,algo) defecto (100,100)
    subscreen1_color = devolver_color("Azul") # Asignar color
    subscreen1.fill(subscreen1_color) # Rellenar
     
    rect_screen1 = definir_tamano_rect() # Crear un rectángulo (x,y,ancho,largo)
    rect_screen1_color = devolver_color("Rojo") # Asignar color

    rect_screen2 = definir_tamano_rect(60,60,15,15) # Crear un rectángulo
    rect_screen2_color = devolver_color("Verde") # Asignar color

    rect_screen3 = definir_tamano_rect(30,230,20,20) # Crear un rectángulo
    rect_screen3_color = devolver_color("Morado") # Asignar color

    rect_screen_lista = []
    definir_lista_rect(rect_screen_lista) # 10 por defecto
    rect_screen_lista_color = devolver_color("Naranja") # Asignar color

    font_screen1 = pygame.font.Font(None, 30) # Para el marcador
    font_screen2 = pygame.font.SysFont("Arial",30, True, False) # Para el reloj de pantalla
    font_screen1_textcolor = devolver_color("Amarillo")
    font_screen1_backcolor = devolver_color("Negro")
    # Crear la superficie Texto (se puede ignorar el background)
    text_screen1 = font_screen1.render("Marcador",0,font_screen1_textcolor,font_screen1_backcolor)
    text_screen2 = font_screen2.render("Tiempo: ",0,font_screen1_textcolor,font_screen1_backcolor)

    # sonidos
    sound_inicial_screen = pygame.mixer.Sound("farm009.wav")
    sound_final_screen = pygame.mixer.Sound("comic013.wav")
    sound_acccion_screen = pygame.mixer.Sound("battle002.wav")
    sound_error_screen = pygame.mixer.Sound("cartoon008.wav")

    # Imágenes
    ima_fondo_screen = directorio_imagenes+'\Fondo_500_500.png'
    ima_fondo_screen = pygame.image.load(ima_fondo_screen) # Crea un superficie con la imagen
    ima_naver_screen = directorio_imagenes+'\Bullet_TankEpic_0.png'
    ima_naver_screen = pygame.image.load(ima_naver_screen) # Crea un superficie con la imagen
    ima_obj_screen = pygame.sprite.Sprite # Creamos un sprite
    ima_obj_screen.image = ima_naver_screen # Asignamos la imagen
    ima_obj_screen.rect = ima_naver_screen.get_rect()
    
    sound_inicial_screen.play()
    mover_raton_posicion_inicial() # Posicion Inicial
    
    while salir_event != True:        
        for event in pygame.event.get(): # Recorrer los eventos
            if event.type == pygame.QUIT: # Cerrar ventana
                salir_event = True

            mover_rect_con_raton(rect_screen1)
            
            # Podemos especificar el boton    
            if event.type == pygame.MOUSEBUTTONDOWN: # Pulsación del ratón               
                rect_screen2 = mover_rect_pulsar_raton(rect_screen2) # Movimiento y reasignación, rect avance_x y avance_y (10,10 por defecto)
                if rect_screen1.colliderect(rect_screen3):
                    eliminar_rect_pulsar_raton(rect_screen3)
                    sound_error_screen.play()
                    
                # Colisiones con la lista
                for myrect in rect_screen_lista:
                    if rect_screen1.colliderect(myrect):
                        eliminar_rect_pulsar_raton(myrect)
                        sound_acccion_screen.play()
                        marcador +=1
                        text_screen1 = font_screen1.render("Marcador: "+str(marcador),0,font_screen1_textcolor,font_screen1_backcolor)
                        
                        
                
                # rect_screen2 = rect_screen2.move(100,100) # Movimiento y reasignación

            if event.type == pygame.MOUSEMOTION: # Mover el ratón
                rect_screen1.move_ip(5,5) # Mover según el ratón
                #rect_screen = rect_screen.move(5,5) # Movimiento (positivo o negativo) y reasignación
                

            if event.type == pygame.KEYDOWN: # Pulsar una tecla Or KEYUP (soltarla) (se puede escoger la tecla- documentacion)                 
               #mover_rect_teclas(rect_screen2,event.key)
                mover_rect_teclas(ima_obj_screen.rect,event.key)

            if rect_screen1.colliderect(rect_screen2):
                # Para evitar colisiones debemos guardar la
                # posición anterior del objeto y reposicionarlo
                mover_rect_por_pantalla(rect_screen2)
                # Disminuir el objeto con el que choca
                rect_screen2.inflate_ip(-1,-1)
                            
                

        # Activamos el reloj 20 Frames/sg lo que detiene el while
        time_event_1.tick(10)
        segundos = pygame.time.get_ticks()/1000 # Pasar de milisegundos a segundos
        # Comprobar si quedan elementos por eliminar
        finJuego = True
        for myrect in rect_screen_lista:            
            if myrect.height != 0 and myrect.width != 0:
                finJuego = False  
                text_screen2 = font_screen2.render("Tiempo: "+str(segundos),0,font_screen1_textcolor,font_screen1_backcolor)

        if finJuego == True and detener_sonido_final==False:
            sound_final_screen.play()
            detener_sonido_final = True
            #sound_final_screen.stop() # Por si se acabo el juego
            
            

        pintar_surface_pantalla(screen,subscreen1)  # Pantalla, surface, x, y (defecto 50,50)
        pintar_surface_pantalla(screen,ima_fondo_screen,0,0)  # Pantalla, surface, x, y (defecto 50,50)
        pintar_surface_pantalla(screen,text_screen1,5,0) # Texto
        pintar_surface_pantalla(screen,text_screen2,250,0) # Texto
        pintar_rect_pantalla(screen,rect_screen1_color,rect_screen1) # Pintar el rectángulo
        pintar_rect_pantalla(screen,rect_screen2_color,rect_screen2) # Pintar el rectángulo
        pintar_rect_pantalla(screen,rect_screen3_color,rect_screen3) # Pintar el rectángulo

        pintar_sprite_pantalla(screen,ima_obj_screen)
        

        for myrect in rect_screen_lista:
            pintar_rect_pantalla(screen,rect_screen_lista_color,myrect)

        pintar_pantalla(screen,screen_color)
        

    pygame.quit()

def definir_tamano_screen(Myscreen_width=500,Myscreen_height=500):
    # Definir el tamaño de la pantalla
    Myscreen_size = Myscreen_width, Myscreen_width
    # Devolver Tamaño
    return pygame.display.set_mode([Myscreen_width,Myscreen_width]) # Crear un objeto para la pantalla

def definir_tamano_surface(Mysurface_width=100,Mysurface_height=100):
    # Crear un tercera superficie usando una lista
    #subscreen_2 = pygame.Surface([50,50])    
     return pygame.Surface((Mysurface_width,Mysurface_height))

def definir_tamano_rect(x=50,y=50,ancho=45,largo=45):
  # Crear un rectángulo
  return pygame.Rect(x,y,ancho,largo) # x, y, ancho, largo

def definir_lista_rect(screen_rect_list = [], cuantos=10):
    
    # Establecer los límites
    mywidth_inferior = 20
    mywidth_superior = 60
    myheight_inferior = 20
    myheight_superior = 60
    my_x = 450
    my_y = 450
       
    for Myrect in range(cuantos):
        # Asi se generarían de distintos tamaños
        #mywidth = random.randrange(mywidth_inferior,mywidth_superior)
        #myheight = random.randrange(myheight_inferior,myheight_superior)
        
        mywidth = mywidth_inferior
        myheight = myheight_inferior
        myx = random.randrange(my_x) # Posiciones aleatorias
        myy = random.randrange(my_y) # Posiciones aleatorias
        screen_rect_list.append(pygame.Rect(myx,myy,mywidth,myheight))
                               
def devolver_color(color):
    # Blanco por defecto
    new_color = (255,255,255) # RGB
    if color == "Blanco":
        new_color = (255,128,128) # RGB
    if color == "Naranja":
        new_color = (255,128,128) # RGB
    if color == "Amarillo":
        new_color = (255,255,128) # RGB
    if color == "Verde":
        new_color = (128,255,128) # RGB
    if color == "Azul":
        new_color = (0,128,255) # RGB
    if color == "Rosa":
        new_color = (255,128,255) # RGB
    if color == "Rojo":
        new_color = (255,0,0) # RGB
    if color == "Morado":
        new_color = (128,128,255) # RGB
    if color == "Marron":
        new_color = (128,64,0) # RGB        
    if color == "Negro":
        new_color = (0,0,0) # RGB    
    if color == "Gris":
        new_color = (192,192,192) # RGB        

    return new_color
   
def pintar_surface_pantalla(screen,subscreen,x=50,y=50):
    screen.blit(subscreen,[x,y]) # Elemento a pintar y coordenadas [x,y] empiezan en 0,0 superior izq

def pintar_rect_pantalla(screen,color,rect):   
    pygame.draw.rect(screen,color,rect) # Superficie destino, color , rectángulo

def pintar_sprite_pantalla(screen,mysprite):
    screen.blit(mysprite.image,mysprite.rect) # Pintar el sprite como rect
    
def pintar_pantalla(screen,color):    
    pygame.display.flip() # Actualiza toda la pantalla    
    screen.fill(color) # Asignar el color de fondo para repintar
    # Actualiza toda la pantalla
    # o el parámetro que se le pase
    #pygame.display.update()    


    
def mover_rect_con_raton(rect_screen):    
    # Aquí movemos directamente con el ratón
    (rect_screen.left,rect_screen.top) = pygame.mouse.get_pos()
    # Hacer que el puntero del ratón esté en el centro del rect
    rect_screen.left -= rect_screen.width/2 # Calcula el centro por el tamaño   
    rect_screen.top -= rect_screen.height/2

def mover_raton_posicion_inicial():
    # Podemos fijar una posición para el ratón
    pygame.mouse.set_pos(10,10)

def mover_rect_teclas(rect_screen,tecla):    
        if tecla == pygame.K_LEFT:
             rect_screen.move_ip(-5,0) # Mover según la tecla
        if tecla == pygame.K_RIGHT:
            rect_screen.move_ip(5,0) # Mover según la tecla

def mover_rect_pulsar_raton(rect_screen,avancex=100,avancey=100):
     return rect_screen.move(avancex,avancey) # Movimiento y reasignación

def eliminar_rect_pulsar_raton(rect_screen):
      rect_screen.height = 0
      rect_screen.width = 0
    
def mover_rect_por_pantalla(rect_screen,avancex=10, avancey=10):
    (rect_screen.left,rect_screen.top)=(rect_screen.left+avancex,rect_screen.top+avancey)
    

    
    
main()
# Efectos de sonido gratis
# http://www.spriters-resource.com/
# http://www.genbeta.com/multimedia/10-sitios-para-descargar-gratis-efectos-de-sonido
# mp3 http://efectos-de-sonido.anuncios-radio.com/gratis/index.php
# wav http://www.grsites.com/archive/sounds/
# http://www.uniquetracks.com/Free-Music-Loops.html # Musica fondo
# Programacion Juegos Pygame 17 - Terminamos el Primer Juego
# Programacion Juegos Pygame 22 - Class Player
# ChelinTutorials ChelinTutorials·284 vídeos
