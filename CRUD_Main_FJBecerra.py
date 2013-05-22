# -*- coding: utf-8 -*-
# coding: UTF-8 
# Python Version: 2.7.3
# Ejercicio: Victima_Conan_FJBecerra.py
# Versión: 0.5
# Curso: Programación avanzada en Python
# Centro: CEVUG
# Autor: Fco. J. Becerra
# email: fjbecerr@gmail.com
# Fecha: 15/05/2013
# Operativa: Uso de la GTK y Glade para crear un interfaz gráfico

import pygtk
pygtk.require("2.0")
import gtk

mainVersion = 0.5 # Versión Activa

class GUI(object):       
	def __init__(self):
	    gtkBuilder = gtk.Builder() # Creamos
	    gtkBuilder.add_from_file("Ejer1.glade") # Cargamos del interfaz
	    gtkBuilder.connect_signals(Handler()) # Conectar con el código
	    self.window = gtkBuilder.get_object("main_window") # Accedemos a la ventana principal	    
	    self.window.show() # Visualizar la ventana principal

if __name__ == "__main__":
	app = GUI()
	gtk.main()


