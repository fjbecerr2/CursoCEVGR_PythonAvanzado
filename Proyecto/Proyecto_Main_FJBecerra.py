# -*- coding: utf-8 -*-
# coding: UTF-8 
# Python Version: 2.7.3
# Ejercicio: CRUD_Main_FJBecerra.py
# Versión: 0
# Curso: Programación avanzada en Python
# Centro: CEVUG
# Autor: Fco. J. Becerra
# email: fjbecerr@gmail.com
# Fecha: 18/06/2013
# Operativa: Proyecto

#import pygtk
#pygtk.require("2.0")
#import gtk

import Proy_SQL 		# Paquete SQL
import Proy_Scrapy 	# Paquete Scrapy


__version__ = "0.0" # Versión Activa

#if __name__ == "__main__":
  #      app = CRUD_GTK_FJBecerra.GUI()        
    #    app.main()
	
#[Host,DB,User,Password,Tabla].

Proy_SQL.func_GenerarBBDD_Ejercicio()
    
# Operativas
"""
MyDatosConexion = ["localhost","BDSCRAPY_SEARCH","scrapyUser","scrapypw"]
MyBBDD = Proy_SQL.clssConectMySQL_Mini(MyDatosConexion)	
MyBBDD.func_Insertar_Registro(
print "Conexion establecida"
MyBBDD.func_Desconectar()
print "Desconectada"
"""	

# Operativas
"""
Proy_Scrapy.func_Generar_Scrapy_Proyecto()
Proy_Scrapy.fun_DefinirItem_Scrapy_Proyecto()
Proy_Scrapy.func_Generar_AgapeaSpiders_Fichero()
"""
	


	
        


