# -*- coding: utf-8 -*-
# coding: UTF-8 
# Python Version: 2.7.3
# Ejercicio: CRUD_GTK_FJBecerra.py
# Versión: 0.5.2
# Curso: Programación avanzada en Python
# Centro: CEVUG
# Autor: Fco. J. Becerra
# email: fjbecerr@gmail.com
# Fecha: 22/05/2013
# Operativa: Uso de la GTK y Glade para crear un interfaz gráfico

import pygtk
pygtk.require("2.0")
import gtk

class GUI:
		
	# Constructor
	# author :
	# Estado [D]esarrollo/[O]perativa: D	
	# since :	0.5						
        def __init__(self):
                self.mainVersion = "0.5.2" # Versión Activa
                self.gtkBuilder = gtk.Builder() # Creamos
                self.gtkBuilder.add_from_file("CRUD_Main_FJBecerra.glade") # Cargamos del interfaz
                # Asignamos los handlers que utilizaremos en el código
                self.handlers = self.fun_connect_signals()
                #self.handlers = self.gtkBuilder.connect_signals({"on_bAcercaDe_clicked" : self.on_bAcercaDe_clicked})
                # Conectamos los handlers asignados
                self.gtkBuilder.connect_signals(self.handlers)
                self.window = self.gtkBuilder.get_object("main_window") # Accedemos a la ventana principal
                self.window.connect('destroy', self.destroy)
                self.windowsTemp = self.gtkBuilder.get_object("wAcercaDe")
                self.window.show() # Visualizar la ventana principal
		
		
	# Función:	fun_connect_signals
	# author :
	# Estado [D]esarrollo/[O]perativa: D	
	# since :	0.5.2				
	# uso 	: 	Asigna los connect_signals
	# param :			
	# return : 	handlers
        def fun_connect_signals(self):
                connect_signalsTemp = {
			"on_imagemenuitem_AcercaDe_button_press_event" : self.on_imagemenuitem_AcercaDe_button_press_event,
			"on_bConectar_clicked": self.on_bConectar_clicked,
			"on_bDesconectar_clicked" : self.on_bDesconectar_clicked
			}
                handlersTemp = self.gtkBuilder.connect_signals(connect_signalsTemp)
                return handlersTemp
		#handlersTemp = self.gtkBuilder.connect_signals({"on_bAcercaDe_clicked" : self.on_bAcercaDe_clicked})

			
        def destroy(self,window):
                gtk.main_quit()


        # Función: on_bAcercaDe
        # Descripcion: Muetra la ventana "Acerca de" -> wAcercaDe 
	# Asociada al handler: on_bAcercaDe_clicked
        # Parámetros: button    -> GtkButton
        def on_imagemenuitem_AcercaDe_button_press_event(self,widget):                
                self.response = self.windowsTemp.run()
                self.windowsTemp.hide()
        # Menu acerca de
		# Asociar el código del botón
		#on_imagemenuitem_AcercaDe_button_press_event

        def on_bConectar_clicked(self,widget):
                print "x"

        def  on_bDesconectar_clicked(self,widget):
                print "x"       
		
               
			   
        def main(self):
                gtk.main()

        


