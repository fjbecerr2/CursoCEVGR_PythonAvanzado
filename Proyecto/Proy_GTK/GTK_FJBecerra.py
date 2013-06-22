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


class GUI:
    """Maneja un interfaz usando GTK."""
            
    # Constructor
    # author :
    # Estado [D]esarrollo/[O]perativa: O   
    # since :   0.5                     
    def __init__(self, MyDatosConexion = []):
        """Constructor de la clase GUI.
        
        Asigna los elementos mínimos para el uso de un interfaz GTK generado con Glade."""
        
        self.MyDatosConexion = MyDatosConexion # Datos para la conexión MySQL
        
        self.__version__ = "1.0" # Versión Activa
        self.gtkBuilder = gtk.Builder() # Creamos
        self.func_Captar_Rutas()    # Preparar rutas para todos los ficheros
        self.gtkBuilder.add_from_file(self.intefazGTK) # Cargamos del interfaz
                
        if os.path.isdir(self.dir_Datos): # Localizar el proyecto existente
            self.gtkBuilder.get_object("window_Main_Page1_lRuta").set_text(self.dir_Datos )
        else:
            self.gtkBuilder.get_object("window_Main_Page1_lRuta").set_text("NO EXISTE PROYECTO")
        
        # Indicar el proyecto en la pantalla de traspaso de datos
        self.gtkBuilder.get_object("window_Main_Page1_lRuta3").set_text(self.fDatos)
        self.Myseleccion = ""
        self.Myspider = ""
        
        # Asignamos los handlers que utilizaremos en el código
        self.handlers = self.fun_connect_signals()                
        # Conectamos los handlers asignados
        self.gtkBuilder.connect_signals(self.handlers)
        self.window = self.gtkBuilder.get_object("window_Main") # Accedemos a la ventana principal
        self.window.set_title("Super Proyecto Chachi")
        self.window.connect('destroy', self.destroy)
        
        self.func_Definir_Ventanas()    # Ventanas del interfaz
        self.func_Definir_Url() # Url utilizadas para el spiders
        # Cargar los opciones para el spider
        self.Myseleccion =  self.gtkBuilder.get_object("window_Main_cbOpciones").get_active_text()
        # Carga la url del elemento seleccionado para el spider
        self.gtkBuilder.get_object("window_Main_lUrl").set_text(self.MyUrls[self.Myseleccion])
        
        self.window.show() # Visualizar la ventana principal
        self.func_Abrir_Ventana("Inform") # Abrir la pantalla de información
                
    
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
    # Estado [D]esarrollo/[O]perativa: O    
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
                ,"on_wMain_menuitem_Operaciones_CrearBBDD_button_press_event" : self.on_wMain_menuitem_Operaciones_CrearBBDD_button_press_event
                ,"on_wMain_menuitem_Operaciones_VerDatos_button_press_event" : self.on_wMain_menuitem_Operaciones_VerDatos_button_press_event
                ,"on_window_Datos_bAceptar_clicked" : self.on_window_Datos_bAceptar_clicked
                }
        handlersTemp = self.gtkBuilder.connect_signals(connect_signalsTemp)
        return handlersTemp     

    # Función:  on_wMain_menuitem_AcercaDe_button_press_event
    # Estado [D]esarrollo/[O]perativa: O             
    # uso   :   Muetra la ventana "Acerca de" -> window_About 
    # param :   widget -> Cualquier que lance la ventana
    def on_wMain_menuitem_AcercaDe_button_press_event(self,widget,data=None):
        """Muestra la ventana de Acerca de -> window_About  y permite cerrarla."""      
        self.func_Abrir_Ventana("About")
     
     
    # Función:  on_wMain_menuitem_Config_button_press_event
    # Estado [D]esarrollo/[O]perativa: O             
    # uso   :   Muestra la pantalla de configuración
    # param :   widget -> Cualquier que lance la ventana     
    def on_wMain_menuitem_Config_button_press_event(self,widget,data=None): 
        """Muestra la pantalla de configuración."""
        # No usamos la lista de definición porque no coinciden los índice con los datos de conexión
        self.gtkBuilder.get_object("window_Config_lvServidor").set_text(self.MyDatosConexion[0])
        self.gtkBuilder.get_object("window_Config_lvBBDD").set_text(self.MyDatosConexion[1])
        self.gtkBuilder.get_object("window_Config_lvTabla").set_text(self.MyDatosConexion[4])
        self.gtkBuilder.get_object("window_Config_lvUsuario").set_text(self.MyDatosConexion[2])
        self.gtkBuilder.get_object("window_Config_lvDominio").set_text("agapea.com")
        self.gtkBuilder.get_object("window_Config_lvUrl").set_text("http://www.agapea.com/")
        self.func_Abrir_Ventana("Config")
    
    
    # Función:  on_wMain_menuitem_Informacion_button_press_event
    # Estado [D]esarrollo/[O]perativa: O             
    # uso   :   Muestra la pantalla de configuración
    # param :   widget -> Cualquier que lance la ventana        
    def on_wMain_menuitem_Informacion_button_press_event(self,widget,data=None): 
        """Abrir la pantalla de información."""
        self.func_Abrir_Ventana("Inform")

        
    # Función:  on_window_Config_bAceptar_clicked
    # Estado [D]esarrollo/[O]perativa: O             
    # uso   :   Cierra la pantalla de configuración
    # param :   widget -> Cualquier que lance la ventana        
    def on_window_Config_bAceptar_clicked(self,widget,data=None):
        """Cierra la pantalla de configuración."""
        self.func_Cerrar_Ventana("Config")

    # Función:  on_window_Inform_bAceptar_button_press_event
    # Estado [D]esarrollo/[O]perativa: O             
    # uso   :   Cierra la pantalla de Información
    # param :   widget -> Cualquier que lance la ventana        
    def on_window_Inform_bAceptar_button_press_event(self,widget,data=None): 
        """Cierra la pantalla de información."""
        self.func_Cerrar_Ventana("Inform")
    
    # Función:  on_window_Main_cbOpciones_changed
    # Estado [D]esarrollo/[O]perativa: O             
    # uso   :   Actualiza la opción seleccionada para el spider
    # param :   widget -> Cualquier que lance la ventana    
    def on_window_Main_cbOpciones_changed(self,widget,data=None): 
        """Actualiza el elemento seleccionado para el spider."""
        self.Myseleccion =  self.gtkBuilder.get_object("window_Main_cbOpciones").get_active_text()
        self.gtkBuilder.get_object("window_Main_lUrl").set_text(self.MyUrls[self.Myseleccion])
        
    
    # Función:  on_window_Main_bSiguiente_clicked
    # Estado [D]esarrollo/[O]perativa: O             
    # uso   :   Genera el proyecto scrapy y pasa a la pantalla de spider
    # param :   widget -> Cualquier que lance la ventana    
    def on_window_Main_bSiguiente_clicked(self,widget,data=None): 
        """Genera el proyecto scrapy y pasa a la pantalla de spider."""                
        # Generar el proyecto
        if Proy_Scrapy.func_Generar_Scrapy_Proyecto() == True:
            Proy_Scrapy.fun_DefinirItem_Scrapy_Proyecto() # Generando los items
            self.gtkBuilder.get_object("window_Mensaje_lMensaje").set_text("Se ha generado un proyecto SCRAPY o Proyecto ya existente")           
            self.gtkBuilder.get_object("window_Main_Page1_lRuta").set_text(self.dir_scrapy)           
            self.gtkBuilder.get_object("notebook1").next_page() # Pasa a la página de spiders
        else :  
            self.gtkBuilder.get_object("window_Mensaje_lMensaje").set_text("ERROR generando proyecto SCRAPY \n o Proyecto ya existente")

        self.func_Abrir_Ventana("Mensaje")
        
    
    # Función:  on_window_Mensaje_bAceptar_button_press_event
    # Estado [D]esarrollo/[O]perativa: O             
    # uso   :   Cierra la ventana de mensaje
    # param :   widget -> Cualquier que lance la ventana    
    def on_window_Mensaje_bAceptar_button_press_event(self,widget,data=None):  
        """Cierra la ventana de mensaje."""
        self.func_Cerrar_Ventana("Mensaje")
        
    
    # Función:  on_window_Main_bSiguiente2_clicked
    # Estado [D]esarrollo/[O]perativa: O             
    # uso   :   Genera el fichero de spider y extrae los datos
    # param :   widget -> Cualquier que lance la ventana    
    def on_window_Main_bSiguiente2_clicked(self,widget,data=None): 
        """Genera el fichero de spider y extrae los datos."""
        MyUrl = self.gtkBuilder.get_object("window_Main_lUrl").get_text()
        if (Proy_Scrapy.func_Generar_AgapeaSpiders_Fichero(self.dir_scrapy, MyUrl)==True):
            Proy_Scrapy.func_Generar_ScrapyPider_Resultados() 
            # Datos para la pantalla de traspaso
            self.Myspider = self.Myseleccion 
            self.gtkBuilder.get_object("window_Main_Page1_lInformacion7").set_text(("Actual Spider : "+self.Myspider ))            
        else:
            self.gtkBuilder.get_object("window_Main_Page1_lInformacion5").set_text("ERROR generando spider")
     
    
    # Función:  on_window_Main_bSiguiente3_clicked
    # Estado [D]esarrollo/[O]perativa: O             
    # uso   :   Formatear los datos extraidos e insertarlos en la BBDD
    # param :   widget -> Cualquier que lance la ventana    
    def on_window_Main_bSiguiente3_clicked(self,widget,data=None):
        """Formatear los datos extraidos e insertarlos en la BBDD."""
        # Datos Generales BBDD
        MyDatosConexion = ["localhost","BDSCRAPY_SEARCH","scrapyUser","scrapypw","TBSCRAPY_SEARCH_URLS"]
        
        TablaDatos = [] 
        # Formatea los datos
        Proy_Scrapy.func_Limpiar_FicheroFuente(self.fDatos,TablaDatos,self.Myseleccion,self.MyUrls[self.Myseleccion])
        # Insertar los datos en la BBDD
        try:
            MyBBDD = Proy_SQL.clssConectMySQL_Mini(MyDatosConexion) 
            MyBBDD.func_EstablecerCursor()
            # Insertar los registros
            for registro in TablaDatos:
                MyBBDD.func_Insertar_Registro(registro)
                MyBBDD.func_ExecSQL()   
                MyBBDD.func_HacerCommit()
            
            MyBBDD.func_DesconectarCursor()
            MyBBDD.func_Desconectar()   
            self.gtkBuilder.get_object("window_Mensaje_lMensaje").set_text("Datos insertados en la Tabla")           
            self.func_Abrir_Ventana("Mensaje")
        except:
            self.gtkBuilder.get_object("window_Mensaje_lMensaje").set_text("ERROR insertando en la Tabla") 
            self.func_Abrir_Ventana("Mensaje")

    
    # Función:  on_wMain_menuitem_Operaciones_CrearBBDD_button_press_event
    # Estado [D]esarrollo/[O]perativa: O             
    # uso   :   Generar el script de la BBDD
    # param :   widget -> Cualquier que lance la ventana    
    def on_wMain_menuitem_Operaciones_CrearBBDD_button_press_event(self,widget,data=None):
        """ Generar el script de la BBDD."""
        if Proy_SQL.func_GenerarBBDD_Ejercicio() == True:
            self.gtkBuilder.get_object("window_Mensaje_lMensaje").set_text("Se ha generado el archivo MySQL.SQL")           
        else:
            self.gtkBuilder.get_object("window_Mensaje_lMensaje").set_text("ERROR generando el archivo MySQL.SQL")           
        self.func_Abrir_Ventana("Mensaje")
            
    
    # Función:  on_wMain_menuitem_Operaciones_VerDatos_button_press_event
    # Estado [D]esarrollo/[O]perativa: O             
    # uso   :   Visualizar los datos insertados en la  BBDD
    # param :   widget -> Cualquier que lance la ventana
    def on_wMain_menuitem_Operaciones_VerDatos_button_press_event(self,widget,data=None):
        """Visualizar los datos insertados en la  BBDD."""
        
        try:
            MyBBDD = Proy_SQL.clssConectMySQL_Mini(self.MyDatosConexion) 
            MyBBDD.func_EstablecerCursor()
            SQLTabla = "TBSCRAPY_SEARCH_URLS"
            SQLCampos = "Dominio, Url,Titulo, Autor, Precio"
            SQLWhere = " 1 "
            MyBBDD.func_Seleccionar(SQLTabla, SQLCampos, SQLWhere)
            MyBBDD.func_ExecSQL()
            Registros =  MyBBDD.MyCursor.fetchall()
            self.gtkBuilder.get_object("liststore2").clear()
        
            lista=gtk.ListStore(str,str,str,str,float)
            for registro in Registros:              
                lista.append(registro)            
        
            render=gtk.CellRendererText()
            columna1=gtk.TreeViewColumn("Dominio",render,text=0)
            columna2=gtk.TreeViewColumn("Url",render,text=1)
            columna3=gtk.TreeViewColumn("Titulo",render,text=2)
            columna4=gtk.TreeViewColumn("Autor",render,text=3)
            columna5=gtk.TreeViewColumn("Precio",render,text=4)
            self.gtkBuilder.get_object("treeview1").set_model(lista)
            self.gtkBuilder.get_object("treeview1").append_column(columna1)
            self.gtkBuilder.get_object("treeview1").append_column(columna2)
            self.gtkBuilder.get_object("treeview1").append_column(columna3)
            self.gtkBuilder.get_object("treeview1").append_column(columna4)
            self.gtkBuilder.get_object("treeview1").append_column(columna5)
        
            MyBBDD.func_HacerCommit()      
            MyBBDD.func_Desconectar()  
      
            self.func_Abrir_Ventana("Datos")
        except:
            self.gtkBuilder.get_object("window_Mensaje_lMensaje").set_text("ERROR al acceder a los datos")           
            self.func_Abrir_Ventana("Mensaje")
            
    
    # Función:  on_window_Datos_bAceptar_clicked
    # Estado [D]esarrollo/[O]perativa: O             
    # uso   :   Cerrar la ventana de datos
    # param :   widget -> Cualquier que lance la ventana
    def on_window_Datos_bAceptar_clicked(self,widget,data=None):
        """Cerrar la ventana de datos."""
        self.func_Cerrar_Ventana("Datos")
    
    # Función:  func_Definir_Ventanas
    # Estado [D]esarrollo/[O]perativa: O             
    # uso   :   Define la ventanas del interfaz
    # param :   widget -> Cualquier que lance la ventana
    def func_Definir_Ventanas(self):
        """Define la ventanas del interfaz."""
        # Ventanas
        self.window_Aplicacion = {"About":self.gtkBuilder.get_object("window_About")
        , "Config":self.gtkBuilder.get_object("window_Config")
        , "Inform":self.gtkBuilder.get_object("window_Inform")      
        , "Mensaje":self.gtkBuilder.get_object("window_Mensaje")   
        , "Datos":self.gtkBuilder.get_object("window_Datos")   
        }
        
        # Definir los títulos
        self.window_Titles = {"About":"Acerca de..."
        , "Config": "Configuración Aplicación"
        , "Inform": "Información de la aplicación"
        , "Mensaje": "Mensaje"
        ,"Datos": "Datos"
        }
        
     
    # Función:  func_Abrir_Ventana
    # Estado [D]esarrollo/[O]perativa: O             
    # uso   :   Abrir una ventana pasada como parámetro
    # param :   widget -> Cualquier que lance la ventana     
    def func_Abrir_Ventana(self,MyVentana):
        """Abrir una ventana pasada como parámetro."""
        # Asignar el título
        self.window_Aplicacion[MyVentana].set_title(self.window_Titles[MyVentana]) 
        self.window_Aplicacion[MyVentana].run() 
        self.window_Aplicacion[MyVentana].hide() 
    
    # Función:  func_Cerrar_Ventana
    # Estado [D]esarrollo/[O]perativa: O             
    # uso   :   Cerrar un ventana pasada como parámetros
    # param :   widget -> Cualquier que lance la ventana     
    def func_Cerrar_Ventana(self,MyVentana):
        """ Cerrar un ventana pasada como parámetro."""
        self.window_Aplicacion[MyVentana].hide() 
    
    
    # Función:  func_Definir_Url
    # Estado [D]esarrollo/[O]perativa: O             
    # uso   :   Url predefinidas para el spider
    # param :   widget -> Cualquier que lance la ventana
    def func_Definir_Url(self):
        """Url predefinidas para el spider."""
        self.MyUrls = {"MySQL" : "http://www.agapea.com/MYSQL-cn254p1i.htm"
        , "Oracle" : "http://www.agapea.com/Oracle-cn248p1i.htm"
        ,"C" : "http://www.agapea.com/C-cn316p1i.htm"
        ,"C++" : "http://www.agapea.com/C---cn277p1i.htm"
        ,"Linux" : "http://www.agapea.com/Linux-cn332p1i.htm"
        ,"Windows" : "http://www.agapea.com/Windows-cn331p1i.htm"
        }
     

    # Función:  func_Captar_Rutas
    # Estado [D]esarrollo/[O]perativa: O             
    # uso   :   Definir la rutas y directorios de la aplicación y recursos
    # param :   widget -> Cualquier que lance la ventana
    def func_Captar_Rutas(self):
        """Definir la rutas y directorios de la aplicación y recursos."""
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
        
              
        
