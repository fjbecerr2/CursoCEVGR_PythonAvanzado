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

import Proy_SQL 	# Paquete SQL
import Proy_Scrapy 	# Paquete Scrapy
import Proy_GTK		# Paquete GTK


__version__ = "0.0" # Versión Activa

# Datos Generales BBDD
MyDatosConexion = ["localhost","BDSCRAPY_SEARCH","scrapyUser","scrapypw","TBSCRAPY_SEARCH_URLS"]

if __name__ == "__main__":
    app = Proy_GTK.GUI(MyDatosConexion)        
    app.main()
	
#[Host,DB,User,Password,Tabla].

# Operativa
#Proy_SQL.func_GenerarBBDD_Ejercicio()

# Operativas
#Proy_Scrapy.func_Generar_Scrapy_Proyecto()
#Proy_Scrapy.fun_DefinirItem_Scrapy_Proyecto()
#Proy_Scrapy.func_Generar_AgapeaSpiders_Fichero()
#Proy_Scrapy.func_Generar_ScrapyPider_Resultados() 
    
# Operativas
#
#MyBBDD = Proy_SQL.clssConectMySQL_Mini(MyDatosConexion)	
#print "Conexion establecida"
#print "Preparando registros
#TablaDatos = []	
#Proy_Scrapy.func_Limpiar_FicheroFuente(TablaDatos)
#print TablaDatos
#MyBBDD.func_EstablecerCursor()
#for registro in TablaDatos:
#    MyBBDD.func_Insertar_Registro(registro,False)
#    MyBBDD.func_ExecSQL()
#    MyBBDD.func_HacerCommit()

#MyBBDD.func_Desconectar()
#print "Desconectada"

# Operativa

#TablaDatos = []	
#Proy_Scrapy.func_Limpiar_FicheroFuente(TablaDatos)
#print TablaDatos 

	
        


