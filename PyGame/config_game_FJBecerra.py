# coding: UTF-8 
# Python Version: 2.7.3
# Fichero: config_game_FjBecerra.py
# Version: 0.0
# Ejercicio: Ejercicio - Pygame 
# Curso: Programacion avanzada en Python
# Centro: CEVUG
# Autor: Fco. J. Becerra
# email: fjbecerr@gmail.com
# Fecha: 13/06/2013
# Operativa: Usar Pygame para crear un video Juego

import os

# Clase: clssconfig_game
# Uso: Clase para configurar los parametros y elementos del juego
class clssconfig_game:
    """ Genera y chequea la configuracion del juego. """
    
    # Constructor
    # since :    0.0
    # Estado [D]esarrollo/[O]perativa: D    
    # author :
    # update:
    # uso :     Asignar los parametros de uso
    # param :  
    # return:
    def __init__(self):
        """Asigna los valores del juego"""
        self.__version__ = "0.0" # Version Activa
        self.dir_aplicacion = os.getcwd()
        
        # Detectar el tipo de sistema operativo
        self.MySistemaOP = os.name
        
        if self.MySistemaOP == "nt": # Presumiblemente Windows
            self.dir_recursos = self.dir_aplicacion + '\\resources'
            self.dir_sonidos = self.dir_recursos + '\\sound'
            self.dir_imagenes = self.dir_recursos + '\\img'
        
        if self.MySistemaOP == "posix": # Presumiblemente Linux
            self.dir_recursos = self.dir_aplicacion + '/resources'
            self.dir_sonidos = self.dir_recursos + '/sound'
            self.dir_imagenes = self.dir_recursos + '/img'
        
        self.nivel = 1

        # Definir los elementos
        self.func_Asignar_Graficos()
        self.func_Asignar_Sonidos()
        self.func_Definir_Colores()
        self.func_Definir_Mensajes()
        
    # func_Asignar_Graficos
    # since :    0.0
    # Estado [D]esarrollo/[O]perativa: D    
    # author :
    # uso :     Asignar los ficheros graficos    
    def func_Asignar_Graficos(self):
        """Asigna los ficheros graficos del juego"""
        if self.MySistemaOP == "nt": # Presumiblemente Windows
            self.dic_Graficos = {"Fondo": self.dir_imagenes+'\\fondo.png',
                "Naver": self.dir_imagenes+'\\naver.png',
                "Navea": self.dir_imagenes+'\\navea.png',
                "Explo": self.dir_imagenes+'\\explo.png',
                "Rayo": self.dir_imagenes+'\\rayo.png'
                }
        
        if self.MySistemaOP == "posix": # Presumiblemente Linux     
                self.dic_Graficos = {"Fondo": self.dir_imagenes+'/fondo.png',
                "Naver": self.dir_imagenes+'/naver.png',
                "Navea": self.dir_imagenes+'/navea.png',
                "Explo": self.dir_imagenes+'/explo.png',
                "Rayo": self.dir_imagenes+'/rayo.png'
                }

        
    # func_Asignar_Sonidos
    # since :    0.0
    # Estado [D]esarrollo/[O]perativa: D    
    # author :
    # uso :     Asignar los ficheros sonido         
    def func_Asignar_Sonidos(self):
        if self.MySistemaOP == "nt": # Presumiblemente Windows
            self.dic_Sonidos = {"Fondo": self.dir_sonidos+'\\fondo.wav',
                "Explo":self.dir_sonidos+'\\explo.wav',
                "Rayo":self.dir_sonidos+'\\rayo.wav',
                "Final":self.dir_sonidos+'\\final.wav'
                }
        
        if self.MySistemaOP == "posix": # Presumiblemente Linux          
                self.dic_Sonidos = {"Fondo": self.dir_sonidos+'/fondo.wav',
                "Explo":self.dir_sonidos+'/explo.wav',
                "Rayo":self.dir_sonidos+'/rayo.wav',
                "Final":self.dir_sonidos+'/final.wav'
                }
     
    # func_Definir_Colores
    # since :    0.0
    # Estado [D]esarrollo/[O]perativa: D    
    # author :
    # uso :     Definir los colores estandar
    def func_Definir_Colores(self):
        """Crea un diccionario con los colores  RGB utilizables."""     
        self.dic_colores = {"Amarillo":(255,255,128) ,
        "Azul":(0,128,255),
        "Blanco":(255,255,255) ,
        "Gris":(192,192,192) ,
        "Marron":(128,64,0),
        "Morado":(128,128,255),
        "Naranja":(255,128,128) ,
        "Negro":(0,0,0),
        "Rojo":(255,0,0) ,
        "Rosa":(255,128,255),
        "Verde":(128,255,128)}
        
    # func_Definir_Mensajes
    # since :    0.0
    # Estado [D]esarrollo/[O]perativa: D    
    # author :
    # uso :     Definir los mensajes estandar   
    def func_Definir_Mensajes(self):
        """Contiene los mensajes de pantalla"""
        self.men_titulo = "Ejercicio PyGame"
        self.men_tiempo = "Tiempo "
        self.men_puntos = "Puntuacion "
        self.men_final = "Fin del Juego "
        self.men_ayuda = " Cursores para desplazamiento, a +Velocidad, z -Velocidad"
        self.men_nivel = "Nivel"
        
    # func_Devolver_Grafico
    # since :    0.0
    # Estado [D]esarrollo/[O]perativa: D    
    # author :
    # uso :    Devuelve un grafico         
    def func_Devolver_Grafico(self, MyGrafico):
        """Devuelve el nombre y ubicacion del fichero graficos solicitado."""
        return self.dic_Graficos[MyGrafico]
     
    # func_Devolver_Sonido
    # since :    0.0
    # Estado [D]esarrollo/[O]perativa: D    
    # author :
    # uso :    Devuelve un sonido    
    def func_Devolver_Sonido(self, MySonido):
        """Devuelve el nombre y ubicacion del fichero sonido solicitado."""
        return self.dic_Sonidos[MySonido]
     
    # func_Devolver_Color
    # since :    0.0
    # Estado [D]esarrollo/[O]perativa: D    
    # author :
    # uso :    Devuelve un color
    def func_Devolver_Color(self, MyColor):
        """Devuelve el color solicitado."""
        return self.dic_colores[MyColor]
