# coding: UTF-8 
# Python Version: 2.7.3
# Fichero: config_render_FJBecerra.py
# Version: 0.0
# Ejercicio: Ejercicio - Pygame 
# Curso: Programacion avanzada en Python
# Centro: CEVUG
# Autor: Fco. J. Becerra
# email: fjbecerr@gmail.com
# Fecha: 13/06/2013
# Operativa: Usar Pygame para crear un video Juego

import pygame
import random
import config_game_FJBecerra

class clssNavea(pygame.sprite.Sprite):
    def __init__ (self):
        pygame.sprite.Sprite.__init__(self) # Inicializar la clase base 
        self.__version__ = "0.0" # Version Activa
        # Inicializar valores
        self.navea_config = config_game_FJBecerra.clssconfig_game()
        self.navea_img = self.navea_config.func_Devolver_Grafico("Navea") 
        self.navea_img = pygame.image.load(self.navea_img) # Crea un superficie con la imagen
        self.naveaex_img = self.navea_config.func_Devolver_Grafico("Explo") 
        self.naveaex_img = pygame.image.load(self.naveaex_img) # Crea un superficie con la imagen
        
        
        self.image = self.navea_img
        self.rect   = self.image.get_rect()

        # Posicion por defecto       
        self.rect.top = 430
        self.rect.left = 225


class clssNaver(pygame.sprite.Sprite):
    def __init__ (self):
        pygame.sprite.Sprite.__init__(self) # Inicializar la clase base 
        self.__version__ = "0.0" # Version Activa
        # Inicializar valores
        self.naver_config = config_game_FJBecerra.clssconfig_game()
        self.naver_img = self.naver_config.func_Devolver_Grafico("Naver") 
        self.naver_img = pygame.image.load(self.naver_img) # Crea un superficie con la imagen
        
        self.image = self.naver_img
        self.rect   = self.image.get_rect()

        # Posicion por defecto       
        self.rect.top = 0
        self.rect.left = 0
        # Posicion aleatorio
        self.MyObjLimx = 5     # Control de rect
        self.MyObjLimy = 495    # Control de rect
        self.rect.top =   random.randrange(self.MyObjLimx,self.MyObjLimy) # Posiciones aleatorias
        self.rect.top =  random.randrange(-(self.MyObjLimy),-(self.MyObjLimx)) # Posiciones aleatorias
         


class clssPantalla():
    
    def __init__(self, Myscreen_width=500, Myscreen_height=500):
        self.__version__ = "0.0" # Version Activa
        # Inicializar valores
        self.MyPantalla_config = config_game_FJBecerra.clssconfig_game()
        
        # Activar propiedades graficas
        self.MyPantalla = self.func_Definir_Tamano_Pantalla() # Asignar tamaño
        self.MyPantalla_color = self.MyPantalla_config.func_Devolver_Color("Blanco")
        self.MyPantalla.fill(self.MyPantalla_color) # Asignar el color de fondo
        self.MyPantalla_img = self.MyPantalla_config.func_Devolver_Grafico("Fondo")
        self.MyPantalla_img = pygame.image.load(self.MyPantalla_img) # Crea un superficie con la imagen
        pygame.display.set_caption(self.MyPantalla_config.men_titulo)
        self.MyListSprites = [ ]
        self.MyVelocidad = 5
        self.MyLimiteSup = 80
        self.MyLimiteInf = 430
        self.MyObjLimx = 5      # Control de rect
        self.MyObjLimy = 495    # Control de rect
        self.MyObjLim = 20  # nº Inicial de elementos
        self.MyObjTamano = 20
    
        # Sonido
        self.MySound_Fondo = self.MyPantalla_config.func_Devolver_Sonido("Fondo")
        self.MySound_Fondo= pygame.mixer.Sound(self.MySound_Fondo)
        self.MySound_Explo = self.MyPantalla_config.func_Devolver_Sonido("Explo")
        self.MySound_Explo= pygame.mixer.Sound(self.MySound_Explo)
        self.MySound_Fondo.play(-1)
        self.MyActivarSound_Fondo = True
    
        # Crear nave azul
        self.MyNavea = clssNavea()
        # Crear un lista de nave roja
        self.MyNavebList = [ ] 
        for contador in range(10):
            self.MyNavebList.append(clssNaver())
        # Redefinir posiciones de salida
        for MyNaver in range(len(self.MyNavebList)):
            # Llega abajo de la pantalla y añadimos otro
            my_x =   random.randrange(self.MyObjLimx,self.MyObjLimy) # Posiciones aleatorias
            my_y =  random.randrange(-(self.MyObjLimy),-(self.MyObjLimx)) # Posiciones aleatorias
            self.MyNavebList[MyNaver].rect =(pygame.Rect(my_x,my_y,self.MyObjTamano,self.MyObjTamano))      
    
        # Definir fuentes de texto
        self.MyFuenteTexto = pygame.font.SysFont("Arial",30, True, False) # Para el reloj de pantalla
        self.MyFuenteTexto_txtcolor  = self.MyPantalla_config.func_Devolver_Color("Amarillo")
        self.MyFuenteTexto_bckcolor = self.MyPantalla_config.func_Devolver_Color("Negro")
    
    # func_Definir_Tamano_Pantalla
    # since :    0.0
    # Estado [D]esarrollo/[O]perativa: D 
    # uso: Define el tamaño de la pantalla
    # author :  
    # param: 
    #       Myscreen_width,Myscreen_height -> Alto y ancho
    # return: Devuelve el tamaño pygame
    def func_Definir_Tamano_Pantalla(self,Myscreen_width=500,Myscreen_height=500):
        # Definir el tamaño de la pantalla
        self.Myscreen_size = Myscreen_width, Myscreen_width
        # Devolver Tamaño
        return pygame.display.set_mode([Myscreen_width,Myscreen_width]) # Crear un objeto para la pantalla
    
    # func_Pintar_Pantalla
    # since :    0.0
    # Estado [D]esarrollo/[O]perativa: D 
    # uso: Pinta la pantalla
    # author :  
    def func_Pintar_Pantalla(self):    
        pygame.display.flip() # Actualiza toda la pantalla    
        self.MyPantalla.fill(self.MyPantalla_color) # Asignar el color de fondo para repintar
        self.MyPantalla.blit(self.MyPantalla_img,[0,0]) # Elemento a pintar y coordenadas [x,y] empiezan en 0,0 superior izq            
        # Actualiza toda la pantalla o el parámetro que se le pase
        #pygame.display.update()  
 
    # func_Pintar_Nave
    # since :    0.0
    # Estado [D]esarrollo/[O]perativa: D 
    # uso: Pinta una nave en pantalla
    # author :  
    # param: Mysprite -> Elemento para pintar
    def func_Pintar_Nave(self,Mysprite):        
            self.MyPantalla.blit(Mysprite.image,(Mysprite.rect.left,Mysprite.rect.top)) # Pintar el sprite como rect
          
    # func_Pintar_Navesr
    # since :    0.0
    # Estado [D]esarrollo/[O]perativa: D 
    # uso: Pintar nave roja en pantalla
    # author :  
    def func_Pintar_Navesr(self):
        for myelemento in self.MyNavebList: # Recorrer la lista
            self.func_Pintar_Nave(myelemento)
    
    # func_Pintar_Textos
    # since :    0.0
    # Estado [D]esarrollo/[O]perativa: D 
    # uso: Pintar un texto en pantalla
    # author :  
    # param: 
    #       MyTexto -> Texto para pintar
    #       x ,y -> Posicion en pantalla
    def func_Pintar_Textos(self,MyTexto,x=50,y=50):
         self.MyPantalla.blit(MyTexto,[x,y]) # Elemento a pintar y coordenadas [x,y] empiezan en 0,0 superior izq
    
    # func_Mover_Navea_Keys
    # since :    0.0
    # Estado [D]esarrollo/[O]perativa: D
    # uso: Mover la nave azul con las teclas
    # author :  
    # param: 
    #       Myrect -> Rect para mover (Nave Azul)
    #       MyTecla -> Tecla pulsada (Cursores)
    def func_Mover_Navea_Keys(self,Myrect,Mytecla): 
        # Aumentar velocidad o disminuir
        if Mytecla == pygame.K_a and self.MyVelocidad < 20:
            self.MyVelocidad+=5  
        if Mytecla == pygame.K_z and self.MyVelocidad > 5:
            self.MyVelocidad-=5         
        
        # Mover según la tecla cursor
        # Los números son los límites en pantalla
        if Mytecla == pygame.K_LEFT:
            if Myrect.left > 5:
                Myrect.move_ip(-(self.MyVelocidad),0) 
        if Mytecla == pygame.K_RIGHT:
            if Myrect.left < 430:
                Myrect.move_ip(self.MyVelocidad,0)
        if Mytecla == pygame.K_UP:
            if  Myrect.top > self.MyLimiteSup:            
                Myrect.move_ip(0,-(self.MyVelocidad)) 
        if Mytecla == pygame.K_DOWN:
            if Myrect.top < self.MyLimiteInf:
                Myrect.move_ip(0,self.MyVelocidad)    
           
    # func_Mover_Navesr
    # since :    0.0
    # Estado [D]esarrollo/[O]perativa: D 
    # uso: Mover las naves por pantalla
    # author :     
    def func_Mover_Navesr(self):
        """Desplaza las naves rojas por la pantalla."""
        for MyNaver in self.MyNavebList:    
            MyNaver.rect.move_ip(0,2)
       
    # func_Refrescar_Navesr
    # since :    0.0
    # Estado [D]esarrollo/[O]perativa: D    
    # uso: Refrescar las naves en pantalla
    # author :                  
    def func_Refrescar_Navesr(self):
        """Hace reaparecer las naves por la parte superior de la pantalla."""
        for MyNaver in range(len(self.MyNavebList)): # Recorrer la lista de naves rojas
            # Llega abajo de la pantalla y añadimos otro
            if self.MyNavebList[MyNaver].rect.top > self.MyLimiteInf:
                my_x =   random.randrange(self.MyObjLimx,self.MyObjLimy) # Posiciones aleatorias
                my_y =  random.randrange(-(self.MyObjLimy),-(self.MyObjLimx)) # Posiciones aleatorias
                # Reasignar una posición de salida
                self.MyNavebList[MyNaver].rect =(pygame.Rect(my_x,my_y,self.MyObjTamano,self.MyObjTamano))
   
    
    # func_Aumentar_Navesr
    # since :    0.0
    # Estado [D]esarrollo/[O]perativa: D    
    # uso: Aumentar el número de naves rojas
    # author :                  
    def func_Aumentar_Navesr(self):
        """Añade una nave roja en pantalla."""
        self.MyNavebList.append(clssNaver())

            
            
    # func_Controlar_Colisiones
    # since :    0.0
    # Estado [D]esarrollo/[O]perativa: D    
    # uso: Controlar colisiones en pantalla
    # author :              
    # return: False / True (True en caso de colision)
    def func_Controlar_Colisiones(self):
        """ Controla las colisiones con las naves en pantalla."""
        # Colisiones con la lista
        for MyNaver in self.MyNavebList:
        # En caso de colisión suena la explosión y asigna la imagen correspondiente
            if self.MyNavea.rect.colliderect(MyNaver.rect):
                self.MySound_Explo.play()                                   
                self.MyNavea.image = self.MyNavea.naveaex_img                                               
                return True
                
        return False 
                
