# -*- coding: utf-8 -*-
# coding: UTF-8 
# Python Version: 2.7.3
# Ejercicio: CRUD_GTK_FJBecerra.py
# Versión: 0.9
# Curso: Programación avanzada en Python
# Centro: CEVUG
# Autor: Fco. J. Becerra
# email: fjbecerr@gmail.com
# Fecha: 23/05/2013
# Operativa: Uso de la GTK y Glade para crear un interfaz gráfico

import pygtk
pygtk.require("2.0")
import gtk
import clssConectMySQL # Importa el módulo que contiene las operaciones MySQL
import webbrowser


class GUI:
        
    # Constructor
    # author :
    # Estado [D]esarrollo/[O]perativa: D    
    # since :   0.5                     
    def __init__(self):
        """Constructor de la clase GUI. Asigna los elementos mínimos para el
        uso de un interfaz GTK generado con Glade."""
        self.Version = "0.9" # Versión Activa
        self.gtkBuilder = gtk.Builder() # Creamos
        self.gtkBuilder.add_from_file("CRUD_Main_FJBecerra.glade") # Cargamos del interfaz
        # Asignamos los handlers que utilizaremos en el código
        self.handlers = self.fun_connect_signals()                
        # Conectamos los handlers asignados
        self.gtkBuilder.connect_signals(self.handlers)
        self.window = self.gtkBuilder.get_object("main_window") # Accedemos a la ventana principal
        self.window.set_title("CRUD_Main_FJBecerra")
        self.window.connect('destroy', self.destroy)
        self.windowsTemp = self.gtkBuilder.get_object("wAcercaDe") 
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
    # uso   :   Asigna los connect_signals
    # param :           
    # return :  handlers
    def fun_connect_signals(self):
        """Permite generar un diccionario con todos los signals y 
        devolver los handlers."""
        connect_signalsTemp = {
                "on_imagemenuitem_AcercaDe_button_press_event" : self.on_imagemenuitem_AcercaDe_button_press_event,
                "on_bConectar_clicked": self.on_bConectar_clicked,
                "on_bDesconectar_clicked" : self.on_bDesconectar_clicked,
		"on_menuitemCrearTabla_button_press_event" : self.on_menuitemCrearTabla_button_press_event,
                "on_wCrearTabla_delete_event" : self.on_wCrearTabla_delete_event,
                "on_bAyudaSQL_wCrearTabla_clicked" : self.on_bAyudaSQL_wCrearTabla_clicked,
                "on_bAutoTabla_wCrearTabla_clicked" : self.on_bAutoTabla_wCrearTabla_clicked
                }
        handlersTemp = self.gtkBuilder.connect_signals(connect_signalsTemp)
        return handlersTemp     

    # Función:  on_imagemenuitem_AcercaDe_button_press_event
    # author :
    # Estado [D]esarrollo/[O]perativa: D    
    # since :   0.5.2               
    # uso   :   Muetra la ventana "Acerca de" -> wAcercaDe 
    # param :   widget -> Cualquier que lance la ventana
    def on_imagemenuitem_AcercaDe_button_press_event(self,widget,data=None):
        """Muestra la ventana de Acerca de -> WAcercaDe 
        y permite cerrarla."""      
        self.response = self.windowsTemp.run()
        self.windowsTemp.hide()

        
    # Función:  on_bConectar_clicked
    # author :
    # Estado [D]esarrollo/[O]perativa: D    
    # since :   0.6            
    # uso   :   Activa la conexión a BBDD 
    # param :   widget -> Cualquier que lance la ventana    
    def on_bConectar_clicked(self,widget):
        """Permite la conexión a una BBDD MySQL haciendo 
        uso del módulo clssConectMySQL usando MySQLdb."""
        try:
            self.ConectDatos = ["localhost","DBdeConan","conan","crom","Victimas"]
            self.ConexionTemp = clssConectMySQL.clssConectMySQL(self.ConectDatos)
            self.ConexionTemp.func_EstablecerCursor(0)
            self.Tablas = self.func_RecuperarTablas()
            self.func_DatosConexion()
            self.lEstadoActual = self.gtkBuilder.get_object("lEstadoActual")
            self.lEstadoActual.set_text("CONECTADO")
        except:            
            self.lEstadoActual = self.gtkBuilder.get_object("lEstadoActual")
            self.lEstadoActual.set_text("DESCONECTADO")

    # Función:  on_menuitemCrearTabla_button_press_event
    # author :
    # Estado [D]esarrollo/[O]perativa: D    
    # since :   0.8            
    # uso   :   Abrir ventana wCrearTabla
    # param :   widget -> Cualquier que lance la ventana  
    def on_menuitemCrearTabla_button_press_event(self,widget,data=None):
        """Abre la ventana wCrearTabla."""       
        self.wCrearTabla = self.gtkBuilder.get_object("wCrearTabla")
        self.wCrearTabla.set_title("Crear Tabla")
        self.wCrearTabla.show_all()
        

    # Función:  on_wCrearTabla_delete_event
    # author :
    # Estado [D]esarrollo/[O]perativa: D    
    # since :   0.8            
    # uso   :   Cerrar ventana wCrearTabla
    # param :   *args - Representa los elementos de la ventana
    # return :  True
    def on_wCrearTabla_delete_event(self, *args):
        self.wCrearTabla = self.gtkBuilder.get_object("wCrearTabla")
        self.wCrearTabla.hide()
        return True
	

    # Función:  on_bDesconectar_clicked
    # author :
    # Estado [D]esarrollo/[O]perativa: D    
    # since :   0.6            
    # uso   :   Desactiva la conexión a BBDD 
    # param :   widget -> Cualquier que lance la ventana
    def  on_bDesconectar_clicked(self,widget):
        """Permite la desconexión a una BBDD MySQL haciendo 
        uso del módulo clssConectMySQL usando MySQLdb."""
        try:
            self.ConexionTemp.func_HacerCommit() # Actualizar
            self.ConexionTemp.func_DesconectarCursor()
            self.ConexionTemp.func_Desconectar()
            self.lMyhostActual.set_text("---")
            self.lMydbActual.set_text("---")
            self.lMyuserActual.set_text("---")
            self.lMyTablaActual.set_text("---")
            self.lEstadoActual.set_text("DESCONECTADO")
        except:
            self.lEstadoActual = self.gtkBuilder.get_object("lEstadoActual")
            self.lEstadoActual.set_text("DESCONECTADO") 

    # Función:  on_bAyudaSQL_wCrearTabla_clicked
    # author :
    # Estado [D]esarrollo/[O]perativa: D    
    # since :   0.9            
    # uso   :   Mostrar web de ayuda SQL
    # param :   button -> Cualquier que lance la ventana
    def on_bAyudaSQL_wCrearTabla_clicked(self,button):
        """ Muestra una web con ayuda SQL."""
        try:
            urlAyuda = 'http://dev.mysql.com/doc/refman/5.0/es/column-types.html'
            webbrowser.open_new_tab(urlAyuda)
        except:
            error = True

    # Función:  on_bAutoTabla_wCrearTabla_clicked
    # author :
    # Estado [D]esarrollo/[O]perativa: D    
    # since :   0.9            
    # uso   :   Autocompletar el campo entry_Campos_wCrearTabla
    # param :   button -> Cualquier que lance la ventana        
    def on_bAutoTabla_wCrearTabla_clicked(self, button):
        """Autocompleta el campo entry_Campos_wCrearTabla."""
        self.entry_Campos_wCrearTabla = self.gtkBuilder.get_object("entry_Campos_wCrearTabla")
        self.entry_Tabla_wCrearTabla = self.gtkBuilder.get_object("entry_Tabla_wCrearTabla")
        self.entry_Campos_wCrearTabla.set_text("id INT, Nombre VARCHAR(100), DNI VARCHAR(20)")
        self.entry_Tabla_wCrearTabla.set_text("TablaPrueba")

        
    # Función:  func_RecuperarTablas
    # author :
    # Estado [D]esarrollo/[O]perativa: D    
    # since :   0.6            
    # uso   :   Muetra la ventana "Acerca de" -> wAcercaDe 
    # param :   widget -> Cualquier que lance la ventana
    def func_RecuperarTablas(self):
        """Almacena la lista de tablas disponibles."""
        self.Tablas = self.ConexionTemp.func_RecuperarTablas()


            
    # Función:  func_DatosConexion
    # author :
    # Estado [D]esarrollo/[O]perativa: D    
    # since :   0.7            
    # uso   :   Asigna los datos de la conexión a la pantalla principal    
    def func_DatosConexion(self):
        """Asigna los datos de la conexión a la pantalla principal."""
        self.lMyhostActual = self.gtkBuilder.get_object("lMyhostActual")
        self.lMydbActual = self.gtkBuilder.get_object("lMydbActual")
        self.lMyuserActual = self.gtkBuilder.get_object("lMyuserActual")
        self.lMyTablaActual = self.gtkBuilder.get_object("lMyTablaActual")        
        
        self.lMyhostActual.set_text(self.ConexionTemp.Myhost)
        self.lMydbActual.set_text(self.ConexionTemp.Mydb)
        self.lMyuserActual.set_text(self.ConexionTemp.Myuser)
        self.lMyTablaActual.set_text(self.ConexionTemp.MyTabla)
       

        


