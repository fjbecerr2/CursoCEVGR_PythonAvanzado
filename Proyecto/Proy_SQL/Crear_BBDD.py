#!/usr/bin/python
# -*- coding: utf-8 -*-
# coding: UTF-8 
# Python Version: 2.7.3
# Ejercicio: Crear_BBDD.py
# Versión: 1.0
# Curso: Programación avanzada en Python
# Centro: CEVUG
# Autor: Fco. J. Becerra
# email: fjbecerr@gmail.com
# Fecha: 18/06/2013
# Operativa: Crear un Script SQL para Generar una BBDD MySQL

import os

# -------------------  FUNCIONES DE CREACIÓN --------------

# func_GenerarSQL
# Estado [D]esarrollo/[O]perativa: O   
# uso :     Genera un archivo SQL.
# param :  
#       MySQL -> Nombre del fichero de  destiono
#       SQLText  -> Líneas SQL
# return: False / True (Operacion Termino)
def func_GenerarSQL(MySQL, SQLText = []):
    """Genera un archivo SQL."""
    try:
        destinoSQL = open(MySQL,"w")
        for LineaSQL in SQLText:        
            destinoSQL.write(LineaSQL)
        destinoSQL.close()  
        return True
    except:
        return False

# func_CrearBBDD
# Estado [D]esarrollo/[O]perativa: O   
# uso :     Generar el texto para crear una BBDD.
# param :  
#       MyBBDD -> Nombre de la BBDD
#       SQLText  -> Líneas SQL
def func_CrearBBDD(MyBBDD, SQLText = []):
    """Generar el texto para crear una BBDD.""" 
    SQLText.append("-- Crear la Base de Datos\n")
    SQLText.append("CREATE DATABASE " + MyBBDD+";\n")
    SQLText.append("COMMIT;\n\n")
    
# func_CrearUsuario
# Estado [D]esarrollo/[O]perativa: O   
# uso :     Genera text SQL para crear un usuario.
# param :  
#       MyBBDD -> Nombre de la BBDD
#       MyUsuario -> Usuario
#       MyIP -> Servidor
#       MyPW -> Contraseña
#       SQLText  -> Líneas SQL    
def func_CrearUsuario(MyBBDD, MyUsuario, MyIP, MyPW, SQLText = []):
    """Genera text SQL para crear un usuario."""
    # Componer
    SQLText_Temp = "GRANT ALL ON TABLE " + MyBBDD + ".* TO "
    SQLText_Temp += "'"+MyUsuario+"'@'"+MyIP+"' IDENTIFIED BY '"+MyPW+"';\n"
    # Generar   
    SQLText.append("-- Crear el Usuario\n")
    SQLText.append(SQLText_Temp)
    SQLText.append("USE "+MyBBDD+";\n")
    SQLText.append("COMMIT;\n\n")
 

# func_CrearTablaBBDD
# Estado [D]esarrollo/[O]perativa: O   
# uso :     Genera text SQL para crear una tabla.
# param :  
#       MyBBDD -> Nombre de la BBDD
#       MyTabla -> Tabla
#       MyCampos -> Lista de campos en formato SQL
#       SQLText  -> Líneas SQL    
def func_CrearTablaBBDD(MyBBDD, MyTabla, MyCampos, SQLText = []):
    """Genera text SQL para crear una tabla.""" 
    SQLText.append("-- Crear la  tabla\n")
    # Componer
    SQLText_Temp = "CREATE TABLE " + MyTabla + " ("
    for MyCampo_Temp in MyCampos:
        SQLText_Temp +=  MyCampo_Temp
    SQLText_Temp+= ");\n"
    SQLText.append(SQLText_Temp)
    SQLText.append("COMMIT;\n\n")
 
 
# ---------------------- FUNCIONES DE ELIMINACIÓN ---------------
# func_EliminarBBDD
# Estado [D]esarrollo/[O]perativa: O   
# uso :     Generar el texto para eliminar una BBDD.
# param :  
#       MyBBDD -> Nombre de la BBDD
#       SQLText  -> Líneas SQL   
def func_EliminarBBDD(MyBBDD,SQLText = []):
    """Generar el texto para eliminar una BBDD.""" 
    SQLText.append("-- Eliminar la Base de Datos\n")
    SQLText.append("DROP DATABASE " + MyBBDD+";\n")
    SQLText.append("COMMIT;\n\n")
    
# func_EliminarTablaBBDD
# Estado [D]esarrollo/[O]perativa: O   
# uso :     Generar el texto para eliminar una Tabla.
# param :  
#       MyTabla -> Nombre de la Tabla
#       SQLText  -> Líneas SQL   
def func_EliminarTablaBBDD(MyTabla, SQLText = []):
    """Generar el texto para eliminar una Tabla.""" 
    SQLText.append("-- Eliminar la Tabla de Datos\n")
    SQLText.append("DROP TABLE " + MyTabla+";\n")
    SQLText.append("COMMIT;\n\n")
 
 
# func_GenerarBBDD_Ejercicio
# Estado [D]esarrollo/[O]perativa: O   
# uso :     Generar el SQL para comenzar el ejercicio.
def func_GenerarBBDD_Ejercicio():
    """Generar el SQL para comenzar el ejercicio."""
    # Comprobar la existencia del directorio
    dir_Actual = os.getcwd()
     
    SQLText = [] # Almacen de líneas SQL
    # Elementos de la BBDD
    MyBBDD = "BDSCRAPY_SEARCH"
    MyUsuario = "scrapyUser"
    MyIP = "localhost"
    MyPW = "scrapypw"
    MyTablas = {"MyTabla_Urls": "TBSCRAPY_SEARCH_URLS" }
    
    MyCampos_Urls = [] # Tabla
    MyCampos_Urls.append("Dominio VARCHAR(100),")
    MyCampos_Urls.append("Url VARCHAR(150),")
    MyCampos_Urls.append("Titulo VARCHAR(100),")
    MyCampos_Urls.append("Autor VARCHAR(50),")
    MyCampos_Urls.append("Precio FLOAT")
        
    try:
		# Funciones que van componiendo las líneas del script SQL
        SQLText.append("-- OPERACIONES DE CREACION\n")
        func_CrearBBDD(MyBBDD, SQLText)
        func_CrearUsuario(MyBBDD,  MyUsuario,MyIP,MyPW,SQLText)        
        func_CrearTablaBBDD(MyBBDD,MyTablas["MyTabla_Urls"],MyCampos_Urls,SQLText)
        SQLText.append("-- OPERACIONES DE ELIMINACION\n")        
        func_EliminarTablaBBDD(MyTablas["MyTabla_Urls"],SQLText)
        func_EliminarBBDD(MyBBDD,SQLText)               
        func_GenerarSQL("MySQL.SQL",SQLText)  # Generar el Script mysql> source ruta\archivo
        return True
    except:
        return False
           
            
