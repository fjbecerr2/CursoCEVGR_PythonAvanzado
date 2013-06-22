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
import Proy_Scrapy  # Paquete Scrapy
import Proy_SQL     # Paquete SQL
import time

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
        self.func_Captar_Rutas()
        self.gtkBuilder.add_from_file(self.intefazGTK) # Cargamos del interfaz
        self.gtkBuilder.get_object("window_Main_Page1_lRuta").set_text(self.dir_scrapy)
        self.gtkBuilder.get_object("window_Main_Page1_lRuta3").set_text(self.fDatos)
        self.Myseleccion = ""
        self.Myspider = ""
        
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
        self.func_Definir_Url()
        self.Myseleccion =  self.gtkBuilder.get_object("window_Main_cbOpciones").get_active_text()
        self.gtkBuilder.get_object("window_Main_lUrl").set_text(self.MyUrls[self.Myseleccion])
        
    
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
                ,"on_wMain_menuitem_Informacion_button_press_event" : self.on_wMain_menuitem_Informacion_button_press_event
                ,"on_window_Inform_bAceptar_button_press_event" : self.on_window_Inform_bAceptar_button_press_event
                ,"on_window_Main_cbOpciones_changed" : self.on_window_Main_cbOpciones_changed
                ,"on_window_Main_bSiguiente_clicked" : self.on_window_Main_bSiguiente_clicked
                ,"on_window_Mensaje_bAceptar_button_press_event" : self.on_window_Mensaje_bAceptar_button_press_event
                ,"on_window_Main_bSiguiente2_clicked" : self.on_window_Main_bSiguiente2_clicked
                ,"on_window_Main_bSiguiente3_clicked" : self.on_window_Main_bSiguiente3_clicked
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
        self.func_Abrir_Ventana("About")
        
    def on_wMain_menuitem_Config_button_press_event(self,widget,data=None): 
        # No usamos la lista de definición porque no coinciden los índice con los datos de conexión
        self.gtkBuilder.get_object("window_Config_lvServidor").set_text(self.MyDatosConexion[0])
        self.gtkBuilder.get_object("window_Config_lvBBDD").set_text(self.MyDatosConexion[1])
        self.gtkBuilder.get_object("window_Config_lvTabla").set_text(self.MyDatosConexion[4])
        self.gtkBuilder.get_object("window_Config_lvUsuario").set_text(self.MyDatosConexion[2])
        self.func_Abrir_Ventana("Config")
        
    def on_wMain_menuitem_Informacion_button_press_event(self,widget,data=None): 
        self.func_Abrir_Ventana("Inform")

    def on_window_Config_bAceptar_clicked(self,widget,data=None): 
        self.func_Cerrar_Ventana("Config")

    def on_window_Inform_bAceptar_button_press_event(self,widget,data=None): 
         self.func_Cerrar_Ventana("Inform")
    
    def on_window_Main_cbOpciones_changed(self,widget,data=None): 
        self.Myseleccion =  self.gtkBuilder.get_object("window_Main_cbOpciones").get_active_text()
        self.gtkBuilder.get_object("window_Main_lUrl").set_text(self.MyUrls[self.Myseleccion])
        
    
    def on_window_Main_bSiguiente_clicked(self,widget,data=None): 
        bSinError = True
        self.gtkBuilder.get_object("notebook1").next_page()
        # Generar el proyecto
        if Proy_Scrapy.func_Generar_Scrapy_Proyecto() == True:
            Proy_Scrapy.fun_DefinirItem_Scrapy_Proyecto() # Generando los items
            self.gtkBuilder.get_object("window_Mensaje_lMensaje").set_text("Se ha generado un proyecto SCRAPY o Proyecto ya existente")           
            self.gtkBuilder.get_object("window_Main_Page1_lRuta").set_text(self.dir_scrapy)           
        else :  
            self.gtkBuilder.get_object("window_Mensaje_lMensaje").set_text("ERROR generando proyecto SCRAPY")
            bSinError  = False
        self.func_Abrir_Ventana("Mensaje")
        
        
    def on_window_Mensaje_bAceptar_button_press_event(self,widget,data=None):  
        self.func_Cerrar_Ventana("Mensaje")
        
    def on_window_Main_bSiguiente2_clicked(self,widget,data=None): 
        MyUrl = self.gtkBuilder.get_object("window_Main_lUrl").get_text()
        if (Proy_Scrapy.func_Generar_AgapeaSpiders_Fichero(self.dir_scrapy, MyUrl)==True):
            Proy_Scrapy.func_Generar_ScrapyPider_Resultados() 
            # Datos para la pantalla de traspaso
            self.Myspider = self.Myseleccion 
            self.gtkBuilder.get_object("window_Main_Page1_lInformacion7").set_text(("Actual Spider : "+self.Myspider ))
            
        else:
            self.gtkBuilder.get_object("window_Main_Page1_lInformacion5").set_text("ERROR generando spider")
     
    def on_window_Main_bSiguiente3_clicked(self,widget,data=None):
         # Datos Generales BBDD
        print "siguiente 3"
        MyDatosConexion = ["localhost","BDSCRAPY_SEARCH","scrapyUser","scrapypw","TBSCRAPY_SEARCH_URLS"]
        
        TablaDatos = [] 
        self.Myseleccion 
        Proy_Scrapy.func_Limpiar_FicheroFuente(self.fDatos,TablaDatos,self.Myseleccion,self.MyUrls[self.Myseleccion])
        for elemento in TablaDatos:
            print elemento
        MyBBDD = Proy_SQL.clssConectMySQL_Mini(MyDatosConexion) 
        MyBBDD.func_EstablecerCursor()
        for registro in TablaDatos:
            MyBBDD.func_Insertar_Registro(registro,False)
            MyBBDD.func_ExecSQL()
            MyBBDD.func_HacerCommit()

#MyBBDD.func_Desconectar()
    
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
        ,"window_Config_lvDominio"
        ,"window_Config_lvUrl"
        ]
        
        self.window_Config_Etiquetas = ["window_Config_lServidor"
        ,"window_Config_lBBDD"
        ,"window_Config_lTabla"
        ,"window_Config_lUsuario"
        ,"window_Config_lDominio"
        ,"window_Config_lUrl"
        ]
       

    def func_Definir_Ventanas(self):
        self.window_Aplicacion = {"About":self.gtkBuilder.get_object("window_About")
        , "Config":self.gtkBuilder.get_object("window_Config")
        , "Inform":self.gtkBuilder.get_object("window_Inform")      
        , "Mensaje":self.gtkBuilder.get_object("window_Mensaje")   
        }
        
        self.window_Titles = {"About":"Acerca de..."
        , "Config": "Configuración Aplicación"
        , "Inform": "Información de la aplicación"
        , "Mensaje": "Mensaje"
        }
        
        
    def func_Abrir_Ventana(self,MyVentana):
        self.window_Aplicacion[MyVentana].set_title(self.window_Titles[MyVentana])  
        self.window_Aplicacion[MyVentana].run() 
        self.window_Aplicacion[MyVentana].hide() 
    
    def func_Cerrar_Ventana(self,MyVentana):
        self.window_Aplicacion[MyVentana].hide() 
    
    def func_Definir_Url(self):
        self.MyUrls = {"MySQL" : "http://www.agapea.com/MYSQL-cn254p1i.htm"
        , "Oracle" : "http://www.agapea.com/Oracle-cn248p1i.htm"
        ,"C" : "http://www.agapea.com/C-cn316p1i.htm"
        ,"C++" : "http://www.agapea.com/C---cn277p1i.htm"
        ,"Linux" : "http://www.agapea.com/Linux-cn332p1i.htm"
        ,"Windows" : "http://www.agapea.com/Windows-cn331p1i.htm"
        }
        
    def func_Captar_Rutas(self):
        # Ubicación de recursos
        self.dir_aplicacion = os.getcwd()  # Ubicación del programa
        self.intefazGTK = self.dir_aplicacion
        self.dir_recursos = self.dir_aplicacion
        self.dir_scrapy = self.dir_aplicacion
        self.dir_spiders = self.dir_aplicacion      
        self.dir_Datos = self.dir_aplicacion     
        self.fDatos = "scrapycsv.txt"
        MySistemaOP = os.name   # Sistema Operativo
    
        # Localizar los directorios y ficheros creados por Scrapy
        if MySistemaOP == "nt": # Presumiblemente Windows
            self.intefazGTK += "\\resources\\Proy.glade"
            self.dir_recursos +=  "\\resources"
            self.dir_scrapy += "\\Proyscrapytemp\\Proyscrapytemp"
            self.dir_spiders += "\\Proyscrapytemp\\Proyscrapytemp\\spiders"
            self.dir_Datos += "\\Proyscrapytemp"
            self.fDatos = self.dir_Datos + "\\scrapycsv.txt"
            
        if MySistemaOP == "posix": # Presumiblemente Linux
            self.intefazGTK += "/resources/Proy.glade"
            self.dir_recursos += "/resources"
            self.dir_scrapy += "/Proyscrapytemp/Proyscrapytemp"
            self.dir_spiders += "/Proyscrapytemp/Proyscrapytemp/spiders"
            self.dir_Datos += "/Proyscrapytemp"
            self.fDatos = self.dir_Datos + "/scrapycsv.txt"
        
              
        
