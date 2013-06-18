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

# func_GenerarSQL
# since :    1.0
# Estado [D]esarrollo/[O]perativa: O   
# author :
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
# since :    1.0
# Estado [D]esarrollo/[O]perativa: O   
# author :
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
# since :    1.0
# Estado [D]esarrollo/[O]perativa: O   
# author :
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
# since :    1.0
# Estado [D]esarrollo/[O]perativa: O   
# author :
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
 
# func_GenerarBBDD_Ejercicio
# since :    1.0
# Estado [D]esarrollo/[O]perativa: O   
# author :
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
    MyTablas = {"MyTabla_Dominios":"TBSCRAPY_SEARCH_DOMINIO",
                    "MyTabla_Urls": "TBSCRAPY_SEARCH_URLS" }
    
    MyCampos_Dominios = [] # Primera tabla
    MyCampos_Dominios.append("Titulo VARCHAR(100),")
    MyCampos_Dominios.append("Link VARCHAR(150)")
    
    MyCampos_Urls = [] # Segunda tabla
    MyCampos_Urls.append("Titulo VARCHAR(100),")
    MyCampos_Urls.append("Link VARCHAR(150),")
    MyCampos_Urls.append("Descrip VARCHAR(250)")
    
    print "Generando SQL..."
    try:
        func_CrearBBDD(MyBBDD, SQLText)
        func_CrearUsuario(MyBBDD,  MyUsuario,MyIP,MyPW,SQLText)
        func_CrearTablaBBDD(MyBBDD,MyTablas["MyTabla_Dominios"],MyCampos_Dominios,SQLText)
        func_CrearTablaBBDD(MyBBDD,MyTablas["MyTabla_Urls"],MyCampos_Urls,SQLText)
        func_GenerarSQL("MySQL.SQL",SQLText)    
        print "SQL Listo..."    
        print dir_Actual + "\\MySQL.SQL"
    except Myex:
        print "Se produjo un ERROR al generar el FICHERO SQL"
        print "Puede usar el fichero BBDD.SQL para generar la base de datos"
    
func_GenerarBBDD_Ejercicio()
        

    
    
            
