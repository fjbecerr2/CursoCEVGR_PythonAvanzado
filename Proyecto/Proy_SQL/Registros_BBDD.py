#!/usr/bin/python
# -*- coding: utf-8 -*-
# coding: UTF-8 
# Python Version: 2.7.3
# Ejercicio: Registros_BBDD.py
# Versión: 1.0
# Curso: Programación avanzada en Python
# Centro: CEVUG
# Autor: Fco. J. Becerra
# email: fjbecerr@gmail.com
# Fecha: 18/06/2013
# Operativa: Operaciones son una BBDD

import MySQLdb #Importar libreria


# Clase: clssConectMySQL_Mini
# Uso: Clase para operación de conexión a MySQL
class clssConectMySQL_Mini:
    """Maneja operaciones sobre MySQL."""
    
    # Constructor
    # Estado [D]esarrollo/[O]perativa: O       
    # uso :     Asigna los parámetros para una conexión y una query
    # param :   
    #   ConectData=[] -> Parámentros de la conexión
    def __init__(self,ConectData=[]):
        """Realiza la conexión a una BBDD MySQL. Toma como parametros
        los datos de conexión con lista [Host,DB,User,Password,Tabla]."""
        self.__version__ = "1.0" # Versión Activa
        # Comprobar el número de elementos
        # Estableciendo parametros de conexion
        self.Myhost = ConectData[0]
        self.Mydb = ConectData[1]
        self.Myuser = ConectData[2]
        self.Mypassw = ConectData[3]        
        self.MyTablas = {"MyTabla_Urls": "TBSCRAPY_SEARCH_URLS" }
                    
        self.MyQuery = " "                
        # Establece una conexión MySQL
        self.MyConexion = MySQLdb.connect(host=self.Myhost, user=self.Myuser, passwd=self.Mypassw, db=self.Mydb)       
         

    # Función:  func_Desconectar
    # Estado [D]esarrollo/[O]perativa: O    
    # uso   :   Desconectar la conexión
    def func_Desconectar(self):
		"""Desconectar la conexión MySQL."""
		self.MyConexion.close()

		
    # Función:  func_DesconectarCursor
    # Estado [D]esarrollo/[O]perativa: O    
    # uso   :   Desconecta un cursor
    def func_DesconectarCursor(self):
        """Desconecta el cursor."""
        self.MyCursor.close();  

    
    # Función:  func_EstablecerCursor
    # Estado [D]esarrollo/[O]perativa: O    
    # uso   :   Activa un cursor para nuestra conexión
    # param :   iTipoCursor -> Entero permite especificar el tipo   
    def func_EstablecerCursor(self, iTipoCursor=0):
        """Establece el cursor."""
        if iTipoCursor == 1: # Cursor con DictCursor            
            self.MyCursor = self.MyConexion.cursor(MySQLdb.cursors.DictCursor)                    
        else: # Cursor standard            
            self.MyCursor = self.MyConexion.cursor()        

    
    # Función:  func_Insertar_Registro
    # Estado [D]esarrollo/[O]perativa: O           
    # uso   :   Genera una consulta INSERT
    # param :
    #       SQLDatos - Datos asignados a los campos     
    def func_Insertar_Registro(self, SQLDatos = []):
		"""Genera una query INSERT...
		
		Se le pasan: los datos como lista. Inserta en la BBDD de prueba""" 
		self.MyQuery = "INSERT INTO " + self.MyTablas["MyTabla_Urls"] + "(" 
		CamposMyQuery = ["Dominio", "Url", "Titulo", "Autor", "Precio"]

        # Ajustar el formato a un query añadiendo comillas "" y comas "," a los campos
		CamposMyQuery = self.func_ComponerSQL(CamposMyQuery,0)
		ValoresMyQuery = self.func_ComponerSQL(SQLDatos,1)
		
		for campo in CamposMyQuery: # Componer los campos de la consulta
			self.MyQuery += campo
		self.MyQuery += ")"
        
        # Componer los valores de los campos de la consulta
		self.MyQuery += " VALUES ("
		for campo in ValoresMyQuery:
			self.MyQuery += campo
		self.MyQuery += ");"

        
    # Función:  func_ComponerSQL
    # Estado [D]esarrollo/[O]perativa: O         
    # uso   :   Añade las "" y "," necesarias a los elementos de una consulta
    # param :
    #   Campos - Campos o Valores que queremos formatear
    #   Campo_o_Valor - Vale 0 cuando para formatear campos (sólo añade "," como separador)
    #                   Vale 1 cuando para formatear valores (añade "" y ",")   
    # return :  La lista con los campos adaptados a SQL
    def func_ComponerSQL(self, Campos = [], Campo_o_Valor = 0):
        """Realiza el formateo de una lista para ajustarla a la sintaxis SQL."""
        camposTemp = [] # Temporal para la composición
        campoTemp = ""  # Temporal para la composición
        ultimoCampo = False # Detecta si alcanzamos el último campo
        longitud = 0 # Controlar el nº de campos en operación para fijar el último
        # Añadir las comillas
        for campo in Campos:
			if str(type(campo)) == "<type \'str\'>" and Campo_o_Valor == 1:
				campoTemp = "\"" + campo + "\""
			else:
				campoTemp = str(campo) # No añadimos ajuste, campos no str (numérico)
            
            # Existen varios campos y no estamos en el último
			if len(Campos)>0 and ultimoCampo == False: 
				campoTemp += ","
				longitud = longitud + 1 # Sumar el campo al control
				if longitud == len(Campos) - 1: # Ultimo campo? no añade la ","
					ultimoCampo = True # Pasar del campo inicial
			camposTemp.append(campoTemp) # Añadimos al temporal
                
        return camposTemp # Devolvemos los campos formateados como SQL

    
    # Función:  func_Seleccionar
    # Estado [D]esarrollo/[O]perativa: O    
    # uso   :   Formatea una consulta de selección
    # param :           
    #       SQLTabla - Tabla para la consulta
    #       SQLCampos - Lista de campos de la operación
    #       SQLWhere - Condición
    def func_Seleccionar(self, SQLTabla, SQLCampos, SQLWhere):
        """Compone una query SELECT...

        Se la pasan: el nombre de la tabla, 
        los campos y la condición de WHERE."""        
        self.MyQuery = "SELECT " + SQLCampos
        self.MyQuery += " FROM " + SQLTabla
        self.MyQuery += " WHERE " + SQLWhere
        self.MyQuery += ";"


    # Función:  func_HacerCommit
    # Estado [D]esarrollo/[O]perativa: O        
    # uso   :   Realizar un commit de la conexión
    def func_HacerCommit(self):
		"""Realiza commit de la conexion."""
		self.MyConexion.commit() # Actualizar

    
    # Función:  func_ExecSQL
    # Estado [D]esarrollo/[O]perativa: O            
    # uso   :   Ejecutar una consulta
    def func_ExecSQL(self):
        """Ejecuta una Query SQL."""
        self.MyCursor.execute(self.MyQuery)

    
    # Función:  func_BorrarRegs
    # Estado [D]esarrollo/[O]perativa: O    
    # uso   :   Eliminar los registros actuales
    # param :   Operacion - Índica que tipo de borrar
    def func_BorrarRegistros(self, Operacion):
        """Realiza un DELETE sobre una tabla completa.

        Se puede pasar como parámetro 'all' para borrar
        todos los registros o cualquier condición sobre los campos como id > 1"""

        if Operacion == "all": # Eliminar todos los registros
            SQLTemp = "DELETE FROM " + self.MyTabla+ ";"
        else: # Usar el filtro pasado
            SQLTemp = "DELETE FROM " + self.MyTabla+ " WHERE "+Operacion+" ;"            
        self.MyCursor.execute(SQLTemp)
                

				