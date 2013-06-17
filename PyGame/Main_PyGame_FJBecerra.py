# coding: UTF-8 
# Python Version: 2.7.3
# Fichero: Main_PyGame.py
# Versión: 0.0
# Ejercicio: Ejercicio - Pygame 
# Curso: Programación avanzada en Python
# Centro: CEVUG
# Autor: Fco. J. Becerra
# email: fjbecerr@gmail.com
# Fecha: 13/06/2013
# Operativa: Usar Pygame para crear un video Juego

import pygame
import os, sys 
# Importar módulo gráfico windows
if os.name == "nt":
	os.environ['SDL_VIDEODRIVER'] = 'windib'

# Módulos propios
import config_game_FJBecerra
import config_render_FJBecerra

def main():
    pygame.init() # Inicilizar los módulos de pygame
    salir_event = False
    marcador = 0
    segundos = 0    
    finJuego = False

    # Un reloj evita que el programa compruebe los eventos
    # recursivamente desaprovechando recursos
    time_event_1 = pygame.time.Clock()
    time_screen = pygame.time.Clock()

    # Configuracion del juego
    Myconfig = config_game_FJBecerra.clssconfig_game()
        
    # Crear la pantalla
    MyPantalla = config_render_FJBecerra.clssPantalla()
    MyTiempo = MyPantalla.MyFuenteTexto.render("Tiempo: "+str(segundos),0,MyPantalla.MyFuenteTexto_txtcolor,MyPantalla.MyFuenteTexto_bckcolor)      
        
        
    while salir_event != True:
        # Activamos el reloj 20 Frames/sg lo que detiene el while
        time_event_1.tick(10)
        segundos = pygame.time.get_ticks()/1000 # Pasar de milisegundos a segundos       

        # Cada 30 segundos ponemos una nave mas
        if segundos % 30 ==0 :
            MyPantalla.func_Aumentar_Navesr()

        MyPantalla.func_Pintar_Pantalla()
        MyPantalla.func_Pintar_Nave(MyPantalla.MyNavea) # Nave Azul
        MyPantalla.func_Pintar_Navesr() # Naves rojas
        MyPantalla.func_Pintar_Textos(MyTiempo,5,0)

        

        # Todas las operaciones de movimiento
        if finJuego == False: 
            MyPantalla.func_Mover_Navesr()
            MyPantalla.func_Refrescar_Navesr()
            MyTiempo = MyPantalla.MyFuenteTexto.render("Tiempo: "+str(segundos),0,MyPantalla.MyFuenteTexto_txtcolor,MyPantalla.MyFuenteTexto_bckcolor)      
            MyPantalla.func_Pintar_Textos(MyTiempo,5,0)   
            # Condición de fin
            if MyPantalla.func_Controlar_Colisiones() == True:
                finJuego = True
       
        for event in pygame.event.get(): # Recorrer los eventos
            if event.type == pygame.QUIT: # Cerrar ventana
                salir_event = True
                
            # Eventos de teclado
            if event.type == pygame.KEYDOWN:                
                if finJuego == False:
                    MyPantalla.func_Mover_Navea_Keys(MyPantalla.MyNavea.rect,event.key)
                # Controlar el sonio de fondo
                if  event.key== pygame.K_s:
                    if MyPantalla.MyActivarSound_Fondo == False:
                        MyPantalla.MySound_Fondo.play(-1)
                        MyPantalla.MyActivarSound_Fondo = True
                    else    :
                        MyPantalla.MySound_Fondo.stop()
                        MyPantalla.MyActivarSound_Fondo = False
       
    pygame.quit()

main()
