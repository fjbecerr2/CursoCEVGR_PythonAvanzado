# coding: UTF-8 
# Python Version: 2.7.3
# Fichero: clssConectMySQL_FJBecerra.py
# Versión: 1.5
# Ejercicio: Ejercicio 1 - Programación Avanzada - Víctimas de... 
# Curso: Programación avanzada en Python
# Centro: CEVUG
# Autor: Fco. J. Becerra
# email: fjbecerr@gmail.com
# Fecha: 23/05/2013
# Operativa: Crea una clase para conectar a una base de datos MySQL

import MySQLdb #Importar libreria

# Clase: clssConectMySQL
# Uso: Clase para operación de conexión a MySQL
class clssConectMySQL:
    
	# Constructor
	# since :	 1.0
	# Estado [D]esarrollo/[O]perativa: D	
	# author :
    # uso : 	Asigna los parámetros para una conexión y una query
	# param :	
	#	ConectData=[] -> Parámentros de la conexión
	# return : 	False / True (Error Conexión / Correcta)		
    def __init__(self,ConectData=[]):
		# Comprobar el número de elementos
		if len(ConectData)<5:
			return False
		else:	
			# Estableciendo parametros de conexion
			self.Myhost = ConectData[0]
			self.Mydb = ConectData[1]
			self.Myuser = ConectData[2]
			self.Mypassw = ConectData[3]
			self.MyTabla = ConectData[4]
			self.MyQuery = " "
			self.MyID = 0 # Valor inicial    
			# Descripcion: Establece una conexión MySQL
			self.MyConexion = MySQLdb.connect(host=self.Myhost, user=self.Myuser, passwd=self.Mypassw, db=self.Mydb)
			return True 

    # Función: func_Desconectar
    # Descripcion: Desconectar la conexión
    # Parámetros:
	# Estado [D]esarrollo/[O]perativa: O
    def func_Desconectar(self):
        self.MyConexion.close()
    
    # Función: func_DesconectarCursor
    # Descripcion: Desconecta un cursor
    # Parámetros: Cursor - Cursor que queremos desconectar
	# Estado [D]esarrollo/[O]perativa: O
    def func_DesconectarCursor(self):
        self.MyCursor.close();	
	
    # Función: func_EstablecerCursor
    # Descripcion: Activa un cursor para nuestra conexión
	# Estado [D]esarrollo/[O]perativa: O
    def func_EstablecerCursor(self, iTipoCursor):
        if iTipoCursor == 1: # Cursor con DictCursor            
            self.MyCursor = self.MyConexion.cursor(MySQLdb.cursors.DictCursor)                    
        else: # Cursor standard            
            self.MyCursor = self.MyConexion.cursor()        
	
    # Función: func_Insertar
    # Descripción: Genera una consulta INSERT
    # Parámetros: 
    #		SQLTabla - Tabla sobre la que insertaremos
    #		SQLCampos - Lista de campos de la operación
    #		SQLDatos - Datos asignados a los campos
	# Estado [D]esarrollo/[O]perativa: O
    def func_Insertar(self, SQLTabla, SQLCampos = [], SQLDatos = []):
        self.MyQuery = "INSERT INTO " + SQLTabla + "("        
	# Ajustar el formato a un query añadiendo comillas "" y comas "," a los campos
        CamposMyQuery = self.func_ComponerSQL(SQLCampos,0)
        ValoresMyQuery = self.func_ComponerSQL(SQLDatos,1)

        # Componer los campos de la consulta
        for campo in CamposMyQuery:
            self.MyQuery += campo
        self.MyQuery += ")"
		
	# Componer los valores de los campos de la consulta
        self.MyQuery += " VALUES ("
        for campo in ValoresMyQuery:
            self.MyQuery += campo
        self.MyQuery += ");"
		
    # Función: func_ComponerSQL
    # Descripción: Añade las "" y "," necesarias a los elementos de una consulta
    # Parámetros:
    #	Campos - Campos o Valores que queremos formatear
    #	Campo_o_Valor - Vale 0 cuando para formatear campos (sólo añade "," como separador)
    #					Vale 1 cuando para formatear valores (añade "" y ",")
	# Estado [D]esarrollo/[O]perativa: O
    def func_ComponerSQL(self, Campos = [], Campo_o_Valor = 0):
        camposTemp = [] # Temporal para la composición
        campoTemp = ""	# Temporal para la composición
        ultimoCampo = False # Detecta si alcanzamos el último campo
        longitud = 0 # Controlar el nº de campos en operación
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
                
        return camposTemp		
					
    # Función: func_Seleccionar			
    # Descripción: Formatea una consulta de selección
    # Parámetros: 
    #		SQLTabla - Tabla para la consulta
    #		SQLCampos - Lista de campos de la operación
    #		SQLWhere - Condición
	# Estado [D]esarrollo/[O]perativa: O
    def func_Seleccionar(self, SQLTabla, SQLCampos, SQLWhere):
        self.MyQuery = "SELECT " + SQLCampos
        self.MyQuery += " FROM " + SQLTabla
        self.MyQuery += " WHERE " + SQLWhere
        self.MyQuery += ";"

    # Función: func_HacerCommit
    # Descripción: Realizar un commit de la conexión
    # Parámetros:
	# Estado [D]esarrollo/[O]perativa: O
    def func_HacerCommit(self):
        self.MyConexion.commit() # Actualizar
	
    # Función: func_ExecSQL
    # Descripción: Ejecutar una consulta
    # Parámetros:
    def func_ExecSQL(self):
        self.MyCursor.execute(self.MyQuery)
	
    # Función: func_MostrarDatos
    # Descripción: Mostrar una consulta SELECT
    # Parámetros:
	# Estado [D]esarrollo/[O]perativa: O
    def func_MostrarDatos(self):
        registroTemp= self.MyCursor.fetchone()
        while registroTemp != False and registroTemp != None:
        	print registroTemp
        	registroTemp= self.MyCursor.fetchone() # Siguiente registro 

    # Función: func_MostrarDatosCol
    # Descripción: Mostrar datos formateados 
    # Parámetros:
	# Estado [D]esarrollo/[O]perativa: O
    def func_MostrarDatosCol(self):
        registrosTemp = self.MyCursor.fetchall()
        nregistrosTemp = self.MyCursor.rowcount 
        regCabecera = True
        for registroTemp in registrosTemp:

            if regCabecera == True: # Mostar la cabecera para el listado
                print " "
                print "\n Resultado de la consulta : "+ str(nregistrosTemp)
                print "-----------------------------------------------------------------"
                regCabecera = False
            
            print str(registroTemp["id"])+ " - " + registroTemp["Nombre"]+ " - " +registroTemp["Profesion"]+ " - " +registroTemp["Muerte"]

    # Función: func_ControlarID
    # Descripción: Devolver siguiente valor de ID
    # Parámetros:    
	# Estado [D]esarrollo/[O]perativa: O
    def func_ControlarID(self):
        SQLTemp = "SELECT * FROM "+ self.MyTabla+" WHERE 1 ORDER BY ID DESC;"
        self.MyCursor.execute(SQLTemp)
        # registrosTemp = self.MyCursor.fetchall()[-1:]
        registrosTemp = self.MyCursor.fetchone()
        nregistrosTemp = self.MyCursor.rowcount
        if nregistrosTemp == 0 : # No hay registros y se genera el índice desde 0
            self.MyID += 1 # Usar un variable para inicializar la tabla
            print "-- No se encontraron registros previos en la tabla"
            print "-- Se inicilizara el indice "            
        else: # Hay registros previos            
            self.MyID = registrosTemp[0]            
            #self.MyID = self.MyID[0] 
            self.MyID += 1
            

        return self.MyID

    # Función: func_BorrarRegs
    # Descripción: Eliminar los registros actuales
    # Parámetros:
	# Estado [D]esarrollo/[O]perativa: O
    def func_BorrarRegs(self):
        SQLTemp = "DELETE FROM " + self.MyTabla+ ";"
        self.MyCursor.execute(SQLTemp)

    # Función: func_DatosTest
    # Descripción: Insertar una serie de datos para pruebas
    # Parámetros: nReg - Número de registro que insertaremos
	# Estado [D]esarrollo/[O]perativa: O
    def func_DatosTest(self, nReg):        
        for n in range(nReg):
             # Asignamos los valores para la consulta
            SQLCampos = "id", "Nombre", "Profesion", "Muerte"
            SQLDatos = self.func_ControlarID(), "Zombies"+str(n),"Muertos Vivientes"+str(n),"Desmembramiento a espada"+str(n)
            self.func_Insertar(self.MyTabla, SQLCampos, SQLDatos)
            self.func_ExecSQL()

    # Función: func_ComprobarDatos
    # Descripción: Controlar la integridad de los campos datos antes de usarlos en la query
    # Parámetros: SQLDato - Tupla de los datos para la query
	# Estado [D]esarrollo/[O]perativa: O
    def func_ComprobarDatos(self,SQLDatos = []):
        campoVacio = False
        for n in range(len(SQLDatos)):
            if len(str(SQLDatos[n]))==0:
                campoVacio = True

        return campoVacio        
            
        
        
	# Función: func_Listar_Tablas
	# Descripción: Listar las tablas disponibles
	# Parámetros:
	# Estado [D]esarrollo/[O]perativa: D	
	def func_Listar_Tablas(self):
		 for (table_name,) in self.MyCursor:
			print(table_name)