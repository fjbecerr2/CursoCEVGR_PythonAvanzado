# -*- coding: utf-8 -*-
# coding: UTF-8 
# Python Version: 2.7.3
# Ejercicio: CRUD_GTK_FJBecerra.py
# Versión: 1.6
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
    """Maneja un interfaz usando GTK."""
            
    # Constructor
    # author :
    # Estado [D]esarrollo/[O]perativa: D    
    # since :   0.5                     
    def __init__(self):
        """Constructor de la clase GUI.

        Asigna los elementos mínimos para el uso de un interfaz GTK generado con Glade."""
        self.__version__ = "1.6" # Versión Activa
        self.gtkBuilder = gtk.Builder() # Creamos
        self.gtkBuilder.add_from_file("CRUD_Main_FJBecerra.glade") # Cargamos del interfaz
        # Función para cargar los elementos de pantalla (no automática)
        self.func_DefinirCamposPantallas()
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
    # update : 1.5
    # uso   :   Asigna los connect_signals        
    # return :  handlers
    def fun_connect_signals(self):
        """Permite generar un diccionario con todos los signals y 
        devolver los handlers."""
        connect_signalsTemp = {
                "on_imagemenuitem_AcercaDe_button_press_event" : self.on_imagemenuitem_AcercaDe_button_press_event,
                "on_bConectar_clicked": self.on_bConectar_clicked,
                "on_bDesconectar_clicked" : self.on_bDesconectar_clicked,              
                "on_menuitemCrearRegistro_button_press_event" : self.on_menuitemCrearRegistro_button_press_event,
                "on_menuitemObtenerRegistro_button_press_event" : self.on_menuitemObtenerRegistro_button_press_event,
                "on_menuitemActualizarRegistro_button_press_event" : self.on_menuitemActualizarRegistro_button_press_event,
                "on_menuitemBorrarRegistro_button_press_event" : self.on_menuitemBorrarRegistro_button_press_event,
                "on_menuitemBorrarTabla_button_press_event" : self.on_menuitemBorrarTabla_button_press_event,
                "on_bBuscar_clicked" : self.on_bBuscar_clicked,
                "on_bCancelar_clicked" : self.on_bCancelar_clicked,
                "on_bBorrar_clicked" : self.on_bBorrar_clicked,
                "on_bAceptar_clicked" : self.on_bAceptar_clicked
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
        """Muestra la ventana de Acerca de -> WAcercaDe y permite cerrarla."""      
        self.response = self.windowsTemp.run()
        self.windowsTemp.hide()

        
    # Función:  on_bConectar_clicked
    # author :
    # Estado [D]esarrollo/[O]perativa: D    
    # since :   0.6
    # update :  1.5
    # uso   :   Activa la conexión a BBDD 
    # param :   widget -> Cualquier que lance la ventana    
    def on_bConectar_clicked(self,widget):
        """Permite la conexión a una BBDD MySQL haciendo
        uso del módulo clssConectMySQL usando MySQLdb."""
        try:
            # Cargar los datos de conexión de la pantalla            
            self.ConectDatos = ["localhost"]
            self.ConectDatos.append(self.gtkBuilder.get_object(self.CamposConexion_main_window[0]).get_text())
            self.ConectDatos.append(self.gtkBuilder.get_object(self.CamposConexion_main_window[1]).get_text())
            self.ConectDatos.append(self.gtkBuilder.get_object(self.CamposConexion_main_window[2]).get_text())
            self.ConectDatos.append(self.gtkBuilder.get_object(self.CamposConexion_main_window[3]).get_text())
            # Conectar
            self.ConexionTemp = clssConectMySQL.clssConectMySQL(self.ConectDatos)
            self.ConexionTemp.func_EstablecerCursor(0)            
            self.func_DatosConexion()
            self.gtkBuilder.get_object("lEstadoActual").set_text("CONECTADO")
            self.func_ActualizarEstado("CONECTADO")
            # Controlar los componentes de la pantalla
            self.func_ActivarMenus(True)
            self.func_ActivarBotonConexion(True)
            self.func_ControlCamposConexion(False)
            self.ConexionTemp.MyNewR = False # Control de operación de inserción
            # Se cargar los datos iniciales
            self.func_CargarDatosPantalla()
        #except NameError:
            #print NameError 
        except:            
            self.gtkBuilder.get_object("lEstadoActual").set_text("DESCONECTADO")
            self.func_ActualizarEstado("DESCONECTADO")
            self.func_ActualizarEstado("ERROR EN CONEXION")
            self.func_ActivarMenus(False)
            self.func_ActivarBotonConexion(False)

    # Función:  on_bDesconectar_clicked
    # author :# Estado [D]esarrollo/[O]perativa: D
    # since :   0.6
    # uso   :   Desactiva la conexión a BBDD
    # param :   widget -> Cualquier que lance la ventana
    def on_bDesconectar_clicked(self,widget):
        """Permite la desconexión a una BBDD MySQL haciendo uso
        del módulo clssConectMySQL usando MySQLdb."""
        try:
            self.ConexionTemp.func_HacerCommit() # Actualizar
            self.ConexionTemp.func_DesconectarCursor()
            self.ConexionTemp.func_Desconectar()
            self.lMyhostActual.set_text("---")            
            self.gtkBuilder.get_object("lEstadoActual").set_text("DESCONECTADO") 
            self.func_ActualizarEstado("DESCONECTADO")
            # Controlar los componentes de la pantalla
            self.func_ActivarMenus(False)
            self.func_ActivarBotonConexion(False)
            self.func_ActivarMenuBotones("",False)
            self.func_ControlCamposConexion(True)
        except:
            self.gtkBuilder.get_object("lEstadoActual").set_text("DESCONECTADO")            

    
    # Función:  on_menuitemCrearRegistro_button_press_event
    # author :
    # Estado [D]esarrollo/[O]perativa: D    
    # since :   1.2            
    # uso   :   Prepara la ventana para un nuevo registros 
    # param :   widget -> Cualquier que lance la ventana
    def on_menuitemCrearRegistro_button_press_event(self,widget,data=None):
        """Prepara la ventana para un nuevo registro"""        
        self.ConexionTemp.MyNewR = True       
        self.func_ActivarMenuBotones("menuitemCrearRegistro")
        self.gtkBuilder.get_object("menuitemSQL").deselect() # Cerra el Menu
        self.gtkBuilder.get_object("entry_Tematica_main_window").grab_focus() # Pasar el foco


    # Función:  on_menuitemObtenerRegistro_button_press_event
    # author :
    # Estado [D]esarrollo/[O]perativa: D    
    # since :   1.2            
    # uso   :   Prepara la ventana para localizar un registro 
    # param :   widget -> Cualquier que lance la ventana
    def on_menuitemObtenerRegistro_button_press_event(self,widget,data=None):
        """Prepara la ventana para localizar un registro."""
        self.ConexionTemp.MyNewR = False
        self.func_ActivarMenuBotones("menuitemObtenerRegistro")
        self.gtkBuilder.get_object("menuitemSQL").deselect() # Cerra el Menu
        self.gtkBuilder.get_object("entry_Buscar_main_window").grab_focus() # Pasar el foco


    # Función:  on_menuitemActualizarRegistro_button_press_event
    # author :
    # Estado [D]esarrollo/[O]perativa: D    
    # since :   1.2            
    # uso   :   Prepara la ventana para actualizar un registro 
    # param :   widget -> Cualquier que lance la ventana    
    def on_menuitemActualizarRegistro_button_press_event(self,widget,data=None):
        """Prepara la ventana para la actualización de un registro."""
        self.ConexionTemp.MyNewR = False
        self.func_ActivarMenuBotones("menuitemActualizarRegistro")
        self.gtkBuilder.get_object("menuitemSQL").deselect() # Cerra el Menu
        self.gtkBuilder.get_object("entry_Buscar_main_window").grab_focus() # Pasar el foco


    # Función:  on_menuitemBorrarRegistro_button_press_event
    # author :
    # Estado [D]esarrollo/[O]perativa: D    
    # since :   1.2            
    # uso   :   Prepara la ventana para borrar un registro 
    # param :   widget -> Cualquier que lance la ventana     
    def on_menuitemBorrarRegistro_button_press_event(self,widget,data=None):
        """Prepara la ventana para borrar un registro."""
        self.ConexionTemp.MyNewR = False
        self.func_ActivarMenuBotones("menuitemBorrarRegistro")
        self.gtkBuilder.get_object("menuitemSQL").deselect() # Cerra el Menu
        self.gtkBuilder.get_object("entry_Buscar_main_window").grab_focus() # Pasar el foco


    # Función:  on_menuitemBorrarTabla_button_press_event
    # author :
    # Estado [D]esarrollo/[O]perativa: D    
    # since :   1.6
    # uso   :   Borrar todos o parte de los resgistro de una tabla
    # param :   widget -> Cualquier que lance la operación
    def on_menuitemBorrarTabla_button_press_event(self, widget, data=None):
        """Eliminar todos los registros de la tabla o los que cumplan una condición."""
        self.ConexionTemp.MyNewR = False
        try:
            # La lanzamos directamente sobre la conexión, no tiene interfaz para el filtro
            # de manera que los borra todos
            self.ConexionTemp.func_BorrarRegistros("all")
            self.func_ActualizarEstado("BORRAR TODO CORRECTO")
            self.on_bCancelar_clicked(self)
        except:            
            self.func_ActualizarEstado("ERROR BORRAR TODO")

        
    # Función:  on_bCancelar_clicked
    # author :
    # Estado [D]esarrollo/[O]perativa: D    
    # since :   1.2
    # update : 1.5
    # uso   :   Cancela las operaciones sobre la ventana 
    # param :   button -> Cualquier que lance la ventana 
    def on_bCancelar_clicked(self, button):
        """Cancela las operaciones sobre la ventana."""
        # Operaciones sobre el interfaz
        self.func_ActivarMenus(True)        
        self.func_ActivarMenuBotones("",False)
        self.func_ActivarCamposEdicion(False)
        # Se cargar los datos iniciales
        self.func_CargarDatosPantalla()
        # Reactivar los menus       
        for MenuTemp in self.Menus_main_window :            
            self.gtkBuilder.get_object(MenuTemp).set_sensitive(True)
     

    # Función:  on_bBorrar_clicked
    # author :
    # Estado [D]esarrollo/[O]perativa: D    
    # since :   1.2            
    # uso   :   Borra un registro
    # param :   button -> Cualquier que lance la ventana 
    def on_bBorrar_clicked(self, button):
        """Borra un registro."""
        # Después de borrar retorna el estado de todo
        # Controla los campos porque no tiene operación intermedia entre
        # el interfaz y la BBDD
        if self.func_ControlarCampos() == True:
            try:
                nRegistroTemp = self.gtkBuilder.get_object("entry_Buscar_main_window").get_text()            
                self.ConexionTemp.func_BorrarRegistro(int(nRegistroTemp))
                self.func_ActualizarEstado("BORRAR CORRECTO")                        
            except:
                self.func_ActualizarEstado("ERROR EN BORRAR")
        else:
            self.func_ActualizarEstado("ERROR EN BORRAR")

        self.on_bCancelar_clicked(self)
        

    # Función:  on_bAceptar_clicked
    # author :
    # Estado [D]esarrollo/[O]perativa: D    
    # since :   1.3            
    # uso   :   Guardar nuevo registro
    # param :   button -> Cualquier que lance la ventana 
    def on_bAceptar_clicked(self, button):
        """Acepta la inserción de un nuevo registro o una actualizacion."""
        if self.ConexionTemp.MyNewR == True :  # Nuevo registro
            self.ConexionTemp.MyNewR = False # Tras guardar
            # Pasar los datos
            if self.func_InsertarDatos() == True:
                self.func_ActualizarEstado("INSERT CORRECTO")
            else:
                self.func_ActualizarEstado("INSERT ERROR")
        else: # Es una actualización
            if self.func_ActualizarDato() == True:
                self.func_ActualizarEstado("UPDATE CORRECTO")
            else:
                self.func_ActualizarEstado("UPDATE ERROR")
                
            
        # Después de borrar retorna el estado de todo        
        self.on_bCancelar_clicked(self)        
        
        
    # Función:  on_bBuscar_clicked
    # author :
    # Estado [D]esarrollo/[O]perativa: D    
    # since :   1.3            
    # uso   :   Localizar un registro
    # param :   button -> Cualquier que lance la ventana    
    def on_bBuscar_clicked(self, button):
        """Localizar un registro."""
        try:
            nRegistroTemp = self.gtkBuilder.get_object("entry_Buscar_main_window").get_text()
            self.func_CargarDatosPantalla(int(nRegistroTemp))
            self.func_ActualizarEstado("BUSCAR CORRECTO")
        except:
            self.func_ActualizarEstado("BUSCAR ERROR")
        
            
    # Función:  func_DatosConexion
    # author :
    # Estado [D]esarrollo/[O]perativa: D    
    # since :   0.7
    # update: 1.0
    # uso   :   Asigna los datos de la conexión a la pantalla principal    
    def func_DatosConexion(self):
        """Asigna los datos de la conexión a la pantalla principal."""
        self.lMyhostActual = self.gtkBuilder.get_object("lMyhostActual")            
        self.lMyhostActual.set_text(self.ConexionTemp.Myhost)        

       
    # Función:  func_ActualizarEstado
    # author :
    # Estado [D]esarrollo/[O]perativa: D    
    # since :   1.0            
    # uso   :   Asigna información de estado
    # param :   TextoActualizar - Texto de información sobre la operacion
    def func_ActualizarEstado(self, TextoActualizar):
        """Actualiza una etiqueta con la información de operaciones."""
        self.label_Datos_main_window = self.gtkBuilder.get_object("label_Datos_main_window")
        TextoTemp = self.label_Datos_main_window.get_text()
        TextoTemp = "\n"+TextoActualizar
        self.label_Datos_main_window.set_text("")
        self.label_Datos_main_window.set_text(TextoTemp)

    # Función:  func_ActivarCamposEdicion
    # author :
    # Estado [D]esarrollo/[O]perativa: D    
    # since :   1.0            
    # uso   :   Activa/Desactiva los campos de edición
    # param :   bActivar (False = Desactivar / True = Activar)
    def func_ActivarCamposEdicion(self,bActivar = False):
        """Activa o desactiva los campos de edicion."""
        # Elementos de la pantalla        
        for CampoTemp in self.CamposEdicion_main_window:
            self.gtkBuilder.get_object(CampoTemp).set_text("") # Vaciar el contenido
            self.gtkBuilder.get_object(CampoTemp).set_editable(bActivar) # Activar / Desactivar campos de edición
        
        if self.ConexionTemp.MyNewR == True:
            self.gtkBuilder.get_object(self.CamposEdicion_main_window[0]).set_editable(False)            
            self.gtkBuilder.get_object(self.CamposEdicion_main_window[0]).set_text(str(self.ConexionTemp.func_ControlarID(True)))            
        else:
            self.gtkBuilder.get_object(self.CamposEdicion_main_window[0]).set_editable(bActivar)

       
    # Función:  func_ActivarMenus
    # author :
    # Estado [D]esarrollo/[O]perativa: D    
    # since :   1.2            
    # uso   :   Activa y desactiva los menus
    # param :   bActivar (False = Desactivar / True = Activar)
    def func_ActivarMenus(self, bActivar = False):
        """Activa y desactiva los menus."""
        # Activar / Desactivar Menús
        for MenuTemp in self.Menus_main_window:
            self.gtkBuilder.get_object(MenuTemp).set_sensitive(bActivar)

        
    # Función:  func_ActivarBotonConexion
    # author :
    # Estado [D]esarrollo/[O]perativa: D    
    # since :   1.2            
    # uso   :   Activa y desactiva los botones de conexión
    # param :   bActivar (False = Desactivar / True = Activar)
    def func_ActivarBotonConexion(self, bActivar = False):
        """Activa y desactiva los botones de conexión."""
        # Activar / Desactivar botones de conexión
        self.gtkBuilder.get_object("bConectar").set_sensitive(not bActivar)
        self.gtkBuilder.get_object("bDesconectar").set_sensitive(bActivar)


    # Función:  func_ActivarMenuBotones
    # author :
    # Estado [D]esarrollo/[O]perativa: D    
    # since :   1.2
    # update : 1.6
    # uso   :   Activar / Desactivar los botones para cada operación
    # param :   bActivar (False = Desactivar / True = Activar)
    def func_ActivarMenuBotones(self,Text, bActivar = True):
        """Activar / Desactivar los botones para cada operación"""
        # Lista de botones
        botonesTemp = ["bAceptar","bBuscar","bBorrar","bCancelar"]
            
        self.gtkBuilder.get_object("bCancelar").set_sensitive(True)
        self.gtkBuilder.get_object("menuitemCrearRegistro").set_sensitive(False)
        self.gtkBuilder.get_object("menuitemObtenerRegistro").set_sensitive(False)
        self.gtkBuilder.get_object("menuitemActualizarRegistro").set_sensitive(False)
        self.gtkBuilder.get_object("menuitemBorrarRegistro").set_sensitive(False)
        self.gtkBuilder.get_object("menuitemBorrarTabla").set_sensitive(False)
        
        if Text == "menuitemCrearRegistro":
            self.gtkBuilder.get_object("bAceptar").set_sensitive(True)        
            self.gtkBuilder.get_object("bBuscar").set_sensitive(False)
            self.gtkBuilder.get_object("bBorrar").set_sensitive(False)            
            self.func_ActivarCamposEdicion(True)          

        if Text == "menuitemObtenerRegistro":
            self.gtkBuilder.get_object("bAceptar").set_sensitive(False)            
            self.gtkBuilder.get_object("bBuscar").set_sensitive(True)
            self.gtkBuilder.get_object("bBorrar").set_sensitive(False)
            self.gtkBuilder.get_object("entry_Buscar_main_window").show()            
            self.func_ActivarCamposEdicion(False)
            self.gtkBuilder.get_object("entry_Buscar_main_window").set_sensitive(True)
            self.gtkBuilder.get_object("entry_Buscar_main_window").set_editable(True)
        else: # Ocultar el campo de búsqueda
            self.gtkBuilder.get_object("entry_Buscar_main_window").hide()

        if Text == "menuitemActualizarRegistro":
            self.gtkBuilder.get_object("bAceptar").set_sensitive(True)            
            self.gtkBuilder.get_object("bBuscar").set_sensitive(False)
            self.gtkBuilder.get_object("bBorrar").set_sensitive(False)    
            self.func_ActivarCamposEdicion(True)
            # Activamos la opción de búsqueda para localizar registros y borrarlos
            self.gtkBuilder.get_object("bBuscar").set_sensitive(True)
            self.gtkBuilder.get_object("entry_Buscar_main_window").show()
            self.gtkBuilder.get_object("entry_Buscar_main_window").set_sensitive(True)
            self.gtkBuilder.get_object("entry_Buscar_main_window").set_editable(True)
            
        if Text == "menuitemBorrarRegistro":
            self.gtkBuilder.get_object("bAceptar").set_sensitive(False)                        
            self.gtkBuilder.get_object("bBorrar").set_sensitive(True)
            self.func_ActivarCamposEdicion(True)
            # Activamos la opción de búsqueda para localizar registros y borrarlos
            self.gtkBuilder.get_object("bBuscar").set_sensitive(True)
            self.gtkBuilder.get_object("entry_Buscar_main_window").show()
            self.gtkBuilder.get_object("entry_Buscar_main_window").set_sensitive(True)
            self.gtkBuilder.get_object("entry_Buscar_main_window").set_editable(True)

        # Pararlos todos por desconexion
        if bActivar == False:
            for botonTemp in botonesTemp:
                self.gtkBuilder.get_object(botonTemp).set_sensitive(bActivar)

    # Función:  func_ControlCamposConexion
    # author :
    # Estado [D]esarrollo/[O]perativa: D    
    # since :   1.2            
    # uso   :   Activa / Desactiva los campos de conexión.
    # param :   bActivar (False = Desactivar / True = Activar)
    def func_ControlCamposConexion(self,bActiva = False):
        """Activa / Desactiva los campos de conexión."""
        # Elementos de la conexión
        CamposTemp = ["entry_MydbActual_main_window","entry_MyuserActual_main_window",
                      "entry_MyPasswActual_main_window","entry_MyTablaActual_main_window"]

        for CampoTemp in CamposTemp:              
            self.gtkBuilder.get_object(CampoTemp).set_sensitive(bActiva)        


    # Función:  func_CargarDatosPantalla
    # author :
    # Estado [D]esarrollo/[O]perativa: D    
    # since :   1.2
    # update : 1.5
    # uso   :  Cargar los datos iniciales en pantalla    
    def func_CargarDatosPantalla(self, nIdTemp = 0):
        """Carga el primer registro de una tabla en pantalla."""
        # Iniciar los datos SQL

        self.ConexionTemp.func_HacerCommit() # Actualizar
        CamposTemp = self.ConexionTemp.func_CargarRegistroInicial(nIdTemp)        
        
        for ContadorCampoTemp in range(len(CamposTemp)):
            # Controlar el id
            if str(type(CamposTemp[ContadorCampoTemp])) == "<type \'str\'>": # Controlar el tipo del resto            
                self.gtkBuilder.get_object(self.CamposEdicion_main_window[ContadorCampoTemp]).set_text(str(CamposTemp[ContadorCampoTemp]))
            else:
                self.gtkBuilder.get_object(self.CamposEdicion_main_window[ContadorCampoTemp]).set_text(str(CamposTemp[ContadorCampoTemp]))                                           
        

    # Función:  func_DefinirCamposPantallas
    # author :
    # Estado [D]esarrollo/[O]perativa: D    
    # since :   1.2
    # update : 1.5
    # uso   :  Definir los elementos del interfaz
    def func_DefinirCamposPantallas(self):
        """Definir los campos de interfaz para usarlos."""
        # Campos de edicion
        self.CamposEdicion_main_window = ["entry_Id_main_window","entry_Tematica_main_window","entry_Titulo_main_window",
                                          "entry_Formato_main_window","entry_Paginas_main_window",
                                          "entry_Puntuacion_main_window", "entry_Buscar_main_window"]

        # Campos de la conexión
        self.CamposConexion_main_window = ["entry_MydbActual_main_window","entry_MyuserActual_main_window",
                                           "entry_MyPasswActual_main_window","entry_MyTablaActual_main_window"]

        # Menus disponibles
        self.Menus_main_window = ["menuitemCrearRegistro","menuitemObtenerRegistro",
                     "menuitemActualizarRegistro","menuitemBorrarRegistro","menuitemBorrarTabla"]
        

    # Función:  func_InsertarDatos
    # author :
    # Estado [D]esarrollo/[O]perativa: D    
    # since :   1.2
    # update : 1.5
    # uso   :  Pasa los elementos de pantalla a una SQL Insert
    # return :  False / True (Fin de la operacion Incorrecto / Correcto)
    def func_InsertarDatos(self):
        """Insertará los datos de pantalla en una consulta SQL."""        
        SQLValores = []      

        if self.func_ControlarCampos() == False: # No todos los campos están completos
            return False
        
        # No hay campos vacíos y los añadimos
        for ContadorCampoTemp in range(len(self.CamposEdicion_main_window)):
           # Saltar campo de búsqueda
           if not (str(self.CamposEdicion_main_window[ContadorCampoTemp]) == "entry_Buscar_main_window"): 
               try: 
                   # Campos numéricos 
                   if ContadorCampoTemp == 0 or ContadorCampoTemp == 4 or ContadorCampoTemp == 5:
                       SQLValores.append(int(self.gtkBuilder.get_object(self.CamposEdicion_main_window[ContadorCampoTemp]).get_text()))
                   else:
                       SQLValores.append(str(self.gtkBuilder.get_object(self.CamposEdicion_main_window[ContadorCampoTemp]).get_text()))
               except:
                   return False # Error de conversión

        # Generar la Query SQL        
        self.ConexionTemp.func_Insertar_Basic(SQLValores)
       
        # Lanzar la consulta
        try:
            self.ConexionTemp.func_ExecSQL()
            self.ConexionTemp.func_HacerCommit()            
        except:
            return False
                      
        return True

    # Función:  func_ActualizarDato
    # author :
    # Estado [D]esarrollo/[O]perativa: D        
    # update : 1.6
    # uso   :  Actualizar un registro
    # return :  False / True (Fin de la operacion Incorrecto / Correcto)
    def func_ActualizarDato(self):
        """Actualizar un registro."""
        SQLValores = []
        if self.func_ControlarCampos() == False: # No todos los campos están completos
            return False
        
        # No hay campos vacíos y los añadimos
        for ContadorCampoTemp in range(1,len(self.CamposEdicion_main_window)):           
           # Saltar campo de búsqueda
           if not (str(self.CamposEdicion_main_window[ContadorCampoTemp]) == "entry_Buscar_main_window"):                
                try:                   
                   # Campos numéricos 
                   if ContadorCampoTemp == 0 or ContadorCampoTemp == 4 or ContadorCampoTemp == 5:
                       SQLValores.append(int(self.gtkBuilder.get_object(self.CamposEdicion_main_window[ContadorCampoTemp]).get_text()))
                   else:
                       SQLValores.append(str(self.gtkBuilder.get_object(self.CamposEdicion_main_window[ContadorCampoTemp]).get_text()))
                except:
                    return False # Error de conversión
        
        # Generar la Query SQL        
        nRegistroTemp = self.gtkBuilder.get_object("entry_Buscar_main_window").get_text()
        return self.ConexionTemp.fun_ActualizarRegistro(nRegistroTemp,SQLValores)           
        
        
    # Función:  func_ControlarCampos
    # author :
    # Estado [D]esarrollo/[O]perativa: D        
    # update : 1.6
    # uso   :  Controlar que no existan datos vacios en pantalla
    # return :  False / True (Fin de la operacion Incorrecto / Correcto)
    def func_ControlarCampos(self):
        """Controlar que no existan datos vacios en pantalla."""       
        # Recorrer los valores del interfaz
        # Controlar si algún campo está vacío
        for ContadorCampoTemp in range(len(self.CamposEdicion_main_window)):
            # Saltar campos de búsqueda
            if not (str(self.CamposEdicion_main_window[ContadorCampoTemp]) == "entry_Buscar_main_window"):
                # Comprobar el tamaño
                if self.gtkBuilder.get_object(self.CamposEdicion_main_window[ContadorCampoTemp]).get_text_length() == 0:
                    return False

        return True # No hay campo vacío                
		
