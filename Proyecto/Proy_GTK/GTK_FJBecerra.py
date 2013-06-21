# -*- coding: utf-8 -*-
# coding: UTF-8 
# Python Version: 2.7.3
# Ejercicio: GTK_FJBecerra.py
# Versión: 0.0
# Curso: Programación avanzada en Python
# Centro: CEVUG
# Autor: Fco. J. Becerra
# email: fjbecerr@gmail.com
# Fecha: 21/06/2013
# Operativa: Uso de la GTK y Glade para crear un interfaz gráfico del proyecto

import pygtk
pygtk.require("2.0")
import gtk
import os
#import clssConectMySQL # Importa el módulo que contiene las operaciones MySQL

class GUI:
    """Maneja un interfaz usando GTK."""
            
    # Constructor
    # author :
    # Estado [D]esarrollo/[O]perativa: D    
    # since :   0.5                     
    def __init__(self, MyDatosConexion = []):
        """Constructor de la clase GUI.

        Asigna los elementos mínimos para el uso de un interfaz GTK generado con Glade."""
        self.MyDatosConexion = MyDatosConexion
        self.__version__ = "1.6" # Versión Activa
        self.gtkBuilder = gtk.Builder() # Creamos
        # Ubicación de recursos
        dir_aplicacion = os.getcwd()
        intefazGTK = dir_aplicacion 
        MySistemaOP = os.name   # Sistema Operativo
    
        # Localizar los directorios y ficheros creados por Scrapy
        if MySistemaOP == "nt": # Presumiblemente Windows
            intefazGTK = dir_aplicacion + "\\resources\\Proy.glade"
            
        if MySistemaOP == "posix": # Presumiblemente Linux
            intefazGTK = dir_aplicacion + "/resources/Proy.glade"
        
        self.gtkBuilder.add_from_file(intefazGTK) # Cargamos del interfaz
        
        # Función para cargar los elementos de pantalla (no automática)
        self.func_DefinirCamposPantallas()
        # Asignamos los handlers que utilizaremos en el código
        self.handlers = self.fun_connect_signals()                
        # Conectamos los handlers asignados
        self.gtkBuilder.connect_signals(self.handlers)
        self.window = self.gtkBuilder.get_object("window_Main") # Accedemos a la ventana principal
        self.window.set_title("Super Proyecto Chachi")
        self.window.connect('destroy', self.destroy)
        self.func_Definir_Ventanas()
        self.window.show() # Visualizar la ventana principal
    
    # Función:  main
    # author :
    # Estado [D]esarrollo/[O]perativa: O    
    # since :   0.5
    def main(self):
        gtk.main()  
    
    # Función:  destroy
    # author :
    # Estado [D]esarrollo/[O]perativa: O    
    # since :   0.5             
    def destroy(self,window):
        gtk.main_quit()
        
    # Función:  fun_connect_signals
    # author :
    # Estado [D]esarrollo/[O]perativa: O    
    # since :   0.5.2
    # update : 1.5
    # uso   :   Asigna los connect_signals        
    # return :  handlers
    def fun_connect_signals(self):
        """Permite generar un diccionario con todos los signals y 
        devolver los handlers."""
        connect_signalsTemp = {
                "on_wMain_menuitem_AcercaDe_button_press_event" : self.on_wMain_menuitem_AcercaDe_button_press_event
                ,"on_wMain_menuitem_Config_button_press_event" : self.on_wMain_menuitem_Config_button_press_event
                ,"on_window_Config_bAceptar_clicked":self.on_window_Config_bAceptar_clicked
                }
        handlersTemp = self.gtkBuilder.connect_signals(connect_signalsTemp)
        return handlersTemp     

    # Función:  on_wMain_menuitem_AcercaDe_button_press_event
    # author :
    # Estado [D]esarrollo/[O]perativa: D    
    # since :   0.5.2               
    # uso   :   Muetra la ventana "Acerca de" -> window_About 
    # param :   widget -> Cualquier que lance la ventana
    def on_wMain_menuitem_AcercaDe_button_press_event(self,widget,data=None):
        """Muestra la ventana de Acerca de -> window_About  y permite cerrarla."""      
        #self.response = 
        self.window_About.run()
        self.window_About.hide()
    
    def on_wMain_menuitem_Config_button_press_event(self,widget,data=None): 
        self.window_Config.set_title("Configuración BBDD")  
        # No usamos la lista de definición porque no coinciden los índice con los datos de conexión
        self.gtkBuilder.get_object("window_Config_lvServidor").set_text(self.MyDatosConexion[0])
        self.gtkBuilder.get_object("window_Config_lvBBDD").set_text(self.MyDatosConexion[1])
        self.gtkBuilder.get_object("window_Config_lvTabla").set_text(self.MyDatosConexion[4])
        self.gtkBuilder.get_object("window_Config_lvUsuario").set_text(self.MyDatosConexion[2])
        self.window_Config.run()
        
        self.window_Config.hide()   

    def on_window_Config_bAceptar_clicked(self, widget):
        self.window_Config.hide()
        
    # Función:  func_DefinirCamposPantallas
    # author :
    # Estado [D]esarrollo/[O]perativa: D    
    # since :   1.2
    # update : 1.5
    # uso   :  Definir los elementos del interfaz
    def func_DefinirCamposPantallas(self):
        """Definir los campos de interfaz para usarlos."""
        # Campos window_Config
        self.window_Config_Campos = ["window_Config_lvServidor"
        ,"window_Config_lvBBDD"
        ,"window_Config_lvTabla"
        ,"window_Config_lvUsuario"
        ]
        
        self.window_Config_Etiquetas = ["window_Config_lServidor"
        ,"window_Config_lBBDD"
        ,"window_Config_lTabla"
        ,"window_Config_lUsuario"
        ]
       

    def func_Definir_Ventanas(self):
        self.window_About = self.gtkBuilder.get_object("window_About")
        self.window_Config= self.gtkBuilder.get_object("window_Config")         
