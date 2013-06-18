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
# Operativa: Crear un Script SQL para Generar una BBDD MySQL

import MySQLdb #Importar libreria


# Clase: clssConectMySQL_Mini
# Uso: Clase para operación de conexión a MySQL
class clssConectMySQL_Mini:
    """Maneja operaciones sobre MySQL."""
    
    # Constructor
    # since :    1.0
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
        #self.MyTabla = ConectData[4]
        self.MyTablas = {"MyTabla_Dominios":"TBSCRAPY_SEARCH_DOMINIO",
                    "MyTabla_Urls": "TBSCRAPY_SEARCH_URLS" }
                    
        self.MyQuery = " "
        self.MyID = 0 # Valor inicial
        self.MyNewR = False # Controla si estamos insertando un registro
        # Descripcion: Establece una conexión MySQL
        self.MyConexion = MySQLdb.connect(host=self.Myhost, user=self.Myuser, passwd=self.Mypassw, db=self.Mydb)       
         

    # Función:  func_Desconectar
    # author :
    # Estado [D]esarrollo/[O]perativa: O    
    # since :   1.0
    # uso   :   Desconectar la conexión
    def func_Desconectar(self):
        self.MyConexion.close()

    
    # Función:  func_DesconectarCursor
    # author :
    # Estado [D]esarrollo/[O]perativa: O    
    # since :   1.0             
    # uso   :   Desconecta un cursor
    def func_DesconectarCursor(self):
        """Desconecta el cursor."""
        self.MyCursor.close();  

    
    # Función:  func_EstablecerCursor
    # author :
    # Estado [D]esarrollo/[O]perativa: O    
    # since :   1.0             
    # uso   :   Activa un cursor para nuestra conexión
    # param :   iTipoCursor -> Entero permite especificar el tipo   
    def func_EstablecerCursor(self, iTipoCursor):
        """Establece el cursor."""
        if iTipoCursor == 1: # Cursor con DictCursor            
            self.MyCursor = self.MyConexion.cursor(MySQLdb.cursors.DictCursor)                    
        else: # Cursor standard            
            self.MyCursor = self.MyConexion.cursor()        

    
    # Función:  func_Insertar_Registro
    # author :
    # Estado [D]esarrollo/[O]perativa: O    
    # since :   2.0         
    # uso   :   Genera una consulta INSERT
    # param :
    #       SQLDatos - Datos asignados a los campos 
    #       Dominio - (True) Dominio / (False) Url
    def func_Insertar_Registro(self, SQLDatos = [], Dominio = True):
        """Genera una query INSERT...

        Se le pasan: los datos como lista. Inserta en la BBDD de prueba"""
        self.MyNewR = True # Nuevo registro en inserción
        if Dominio == True: 
            self.MyQuery = "INSERT INTO " + self.MyTablas["MyTabla_Dominios"] + "("
            CamposMyQuery = ["Dominio","Link"]
        else: 
            self.MyQuery = "INSERT INTO " + self.MyTablas["MyTabla_Urls"] + "(" 
            CamposMyQuery = ["Dominio","Titulo","Link","Descrip"]
        
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
    # author :
    # Estado [D]esarrollo/[O]perativa: O    
    # since :   1.0             
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
    # author :
    # Estado [D]esarrollo/[O]perativa: O    
    # since :   1.0             
    # uso   :   Formatea una consulta de selección
    # param :           
    # Parámetros: 
    #       SQLTabla - Tabla para la consulta
    #       SQLCampos - Lista de campos de la operación
    #       SQLWhere - Condición
    def func_Seleccionar(self, SQLTabla, SQLCampos, SQLWhere):
        """Compone una query SELECT...

        Se la pasan: el nombre de la tabla, 
        los campos y la condición de WHERE."""
        self.MyNewR = False # Registro en selección
        self.MyQuery = "SELECT " + SQLCampos
        self.MyQuery += " FROM " + SQLTabla
        self.MyQuery += " WHERE " + SQLWhere
        self.MyQuery += ";"


    # Función:  func_HacerCommit
    # author :
    # Estado [D]esarrollo/[O]perativa: O    
    # since :   1.0         
    # uso   :   Realizar un commit de la conexión
    def func_HacerCommit(self):
        self.MyConexion.commit() # Actualizar

    
    # Función:  func_ExecSQL
    # author :
    # Estado [D]esarrollo/[O]perativa: O    
    # since :   1.0             
    # uso   :   Ejecutar una consulta
    def func_ExecSQL(self):
        """Ejecuta una Query SQL."""
        self.MyCursor.execute(self.MyQuery)

    
    # Función:  func_BorrarRegs
    # author :
    # Estado [D]esarrollo/[O]perativa: O    
    # since :   1.0
    # update :  2.1
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
    
            
             
    # Función:  func_CargarRegistroInicial
    # author :
    # Estado [D]esarrollo/[O]perativa: D   
    # since :   1.8
    # update : 2.0
    # uso   :   "Devuelve el valor de un registro SQL en forma de Lista
    # param : nIdTemp - Número ID del registro solicitado
    # return :  Un registro en forma de lista    
    def func_CargarRegistroInicial(self, nIdTemp = 0):
        """Devuelve el valor de un registro SQL en forma de Lista"""
        self.CamposInterfaz = []        
        self.MyNewR = False # Registro en selección
        SQLTemp = "SELECT * FROM "+ self.MyTabla

        # Localizar el primer registro independientemente del ID
        if nIdTemp > 0:
            SQLTemp += " WHERE Id =" +str(nIdTemp)+ " ORDER BY ID;"            
        else:
            SQLTemp += " ORDER BY ID;"
            
        try:
            self.MyCursor.execute(SQLTemp)            
            RegistroTemp = self.MyCursor.fetchone()
            if RegistroTemp != False and RegistroTemp[0] != None:                
                for CampoTemp in RegistroTemp: # Pasar los datos del registro
                    self.CamposInterfaz.append(CampoTemp)
        except: # Pasar unos valores por defecto            
            self.CamposInterfaz = [0,"Ningun registro","Ningun registro","Ningun registro",0,0]
        
        return self.CamposInterfaz

        
    # Función:  func_BorrarRegistro
    # author :
    # Estado [D]esarrollo/[O]perativa: D   
    # since :   2.1    
    # uso   :  Elimina un registro
    # param : nIdTemp - Número ID del registro solicitado
    # return :  False / True (Incorrecto / Correcta operación)
    def func_BorrarRegistro(self, nIdTemp):
        """Elimina un registro con una consulta SQL."""         
        #self.MyTabla = "BIBLIOTECA_TESTER"
        # Uso una query temporal para no repetir la operación
        SQLTemp = "DELETE FROM "+ self.MyTabla + " WHERE Id = " +str(nIdTemp) +" ;"        
        self.MyCursor.execute(SQLTemp)

        
    # Función:  fun_ActualizarRegistro
    # author :
    # Estado [D]esarrollo/[O]perativa: D   
    # since :   2.1    
    # uso   :  Actualizar un registro
    # param :
    #   nIdTemp - Número ID del registro solicitado
    #   SQLDatos - Valores para la actualización    
    def fun_ActualizarRegistro(self, nIdTemp, SQLDatos = []):
        """Actualizar un registro."""
        ultimoCampo = False # Detecta si alcanzamos el último campo
        longitud = 0 # Controlar el nº de campos en operación para fijar el último
        self.MyNewR = False # Nuevo registro en inserción
        # Naturalmente no actualizamos el id
        CamposMyQuery = ["Tematica","Titulo","Formato","Paginas","Puntuacion"]
        SQLTemp = "UPDATE " + self.MyTabla + " SET "
        for n in range(len(CamposMyQuery)):
            if str(type(SQLDatos[n])) == "<type \'str\'>":
                SQLTemp += CamposMyQuery[n] + "=" +"\"" + SQLDatos[n] + "\""
            else:
                SQLTemp += CamposMyQuery[n] + "=" + str(SQLDatos[n]) # No añadimos ajuste, campos no str (numérico)
            
            # Existen varios campos y no estamos en el último
            if len(CamposMyQuery)>0 and ultimoCampo == False: 
                SQLTemp += ", "                
                longitud = longitud + 1 # Sumar el campo al control
                if longitud == len(CamposMyQuery) - 1: # Ultimo campo? no añade la ","
                    ultimoCampo = True # Pasar del campo inicial

        SQLTemp += " WHERE Id=" +str(nIdTemp)+ " ;"

        try:
            self.MyCursor.execute(SQLTemp)
            return True
        except:
            return False
        

    def fun_Nuevo_Dominio(self, MyDominio):
        
        pass
    
    def fun_Nueva_Url(self, MyDominio, MyUrl):
        pass

    def fun_Devolver_Dominio(self, sqlWhere):
        pass
    
    def fun_Devolver_Url(self, MyDominio, sqlWhere):
        pass
    

    
    
