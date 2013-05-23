# -*- coding: utf-8 -*-
# coding: UTF-8 
# Python Version: 2.7.3
# Ejercicio: CRUD_Main_FJBecerra.py
# Versión: 0.5.2
# Curso: Programación avanzada en Python
# Centro: CEVUG
# Autor: Fco. J. Becerra
# email: fjbecerr@gmail.com
# Fecha: 22/05/2013
# Operativa: Uso de la GTK y Glade para crear un interfaz gráfico

#import pygtk
#pygtk.require("2.0")
#import gtk
import CRUD_GTK_FJBecerra 	# Interfaz gráfica
import clssConectMySQL		# Clase de conexión con MySQL


Version = "0.5.2" # Versión Activa

if __name__ == "__main__":
        app = CRUD_GTK_FJBecerra.GUI()        
        app.main()
        


