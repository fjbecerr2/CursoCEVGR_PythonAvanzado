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
    # since :    1.0
    # Estado [D]esarrollo/[O]perativa: D    
    # author :
    # uso :     Asigna los parámetros para una conexión y una query
    # param :   
    #   ConectData=[] -> Parámentros de la conexión
    # return :  False / True (Error Conexión / Correcta)        
    def __init__(self,ConectData=[]):
        """Realiza la conexión a una BBDD MySQL. Toma como parametros
        los datos de conexión con tupla [Host,DB,User,Password,Tabla]."""
        self.Version = "1.5" # Versión Activa
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
        self.MyCursor.close();  
    
    # Función:  func_EstablecerCursor
    # author :
    # Estado [D]esarrollo/[O]perativa: O    
    # since :   1.0             
    # uso   :   Activa un cursor para nuestra conexión
    # param :   iTipoCursor -> Entero permite especificar el tipo   
    def func_EstablecerCursor(self, iTipoCursor):
        if iTipoCursor == 1: # Cursor con DictCursor            
            self.MyCursor = self.MyConexion.cursor(MySQLdb.cursors.DictCursor)                    
        else: # Cursor standard            
            self.MyCursor = self.MyConexion.cursor()        
    
    # Función:  func_Insertar
    # author :
    # Estado [D]esarrollo/[O]perativa: O    
    # since :   1.0         
    # uso   :   Genera una consulta INSERT
    # param :
    #       SQLTabla - Tabla sobre la que insertaremos
    #       SQLCampos - Lista de campos de la operación
    #       SQLDatos - Datos asignados a los campos 
    # return :  handlers
    def func_Insertar(self, SQLTabla, SQLCampos = [], SQLDatos = []):
        """Genera una query INSERT... Se le pasan: el nombre de la tabla, 
        los nombres de campos como una tupla y los datos como otra tupla."""
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
        
    # Función:  func_ComponerSQL
    # author :
    # Estado [D]esarrollo/[O]perativa: O    
    # since :   1.0             
    # uso   :   Añade las "" y "," necesarias a los elementos de una consulta
    # param :
    #   Campos - Campos o Valores que queremos formatear
    #   Campo_o_Valor - Vale 0 cuando para formatear campos (sólo añade "," como separador)
    #                   Vale 1 cuando para formatear valores (añade "" y ",")   
    # return :  La tupla con los campos adaptados a SQL
    def func_ComponerSQL(self, Campos = [], Campo_o_Valor = 0):
        """Realiza el formateo de una tupla para ajustarla a la sintaxis SQL."""
        camposTemp = [] # Temporal para la composición
        campoTemp = ""  # Temporal para la composición
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
        """Compone una query SELECT... Se la pasan: el nombre de la tabla, 
        los campos y la condición de WHERE."""
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
        self.MyCursor.execute(self.MyQuery)
    
    # Función:  func_MostrarDatos
    # author :
    # Estado [D]esarrollo/[O]perativa: O    
    # since :   1.0             
    # uso   :   Mostrar una consulta SELECT
    def func_MostrarDatos(self):
        """Muestra los registros apuntados por un cursor."""
        registroTemp= self.MyCursor.fetchone()
        while registroTemp != False and registroTemp != None:
            print registroTemp
            registroTemp= self.MyCursor.fetchone() # Siguiente registro 

    # Función:  func_MostrarDatosCol
    # author :
    # Estado [D]esarrollo/[O]perativa: O    
    # since :   1.0             
    # uso   :   Mostrar datos formateados 
    def func_MostrarDatosCol(self):
        """Muestra en columnas los datos apuntados por el cursor."""
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
    
    # Función:  func_ControlarID
    # author :
    # Estado [D]esarrollo/[O]perativa: O    
    # since :   1.0             
    # uso   :   Devolver siguiente valor de ID
    # return :  Valor calculado del nuevo ID
    def func_ControlarID(self):
        """Devuelve un ID para un campo clave. Si no existe ningún registro previo 
        los genera, si existen registros previos toma el mayor valor y lo aumenta."""
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

    # Función:  func_BorrarRegs
    # author :
    # Estado [D]esarrollo/[O]perativa: O    
    # since :   1.0             
    # uso   :   Eliminar los registros actuales
    def func_BorrarRegs(self):
        """Realiza un DELETE sobre una tabla."""
        SQLTemp = "DELETE FROM " + self.MyTabla+ ";"
        self.MyCursor.execute(SQLTemp)

    # Función:  func_DatosTest
    # author :
    # Estado [D]esarrollo/[O]perativa: O    
    # since :   1.0             
    # uso   :   Insertar una serie de datos para pruebas
    # param :   nReg - Número de registro que insertaremos
    def func_DatosTest(self, nReg):
        """Genera registros en número igual al argumento pasado."""
        for n in range(nReg):
             # Asignamos los valores para la consulta
            SQLCampos = "id", "Nombre", "Profesion", "Muerte"
            SQLDatos = self.func_ControlarID(), "Zombies"+str(n),"Muertos Vivientes"+str(n),"Desmembramiento a espada"+str(n)
            self.func_Insertar(self.MyTabla, SQLCampos, SQLDatos)
            self.func_ExecSQL()

    # Función:  func_ComprobarDatos
    # author :
    # Estado [D]esarrollo/[O]perativa: O    
    # since :   1.0             
    # uso   :   Controlar la integridad de los campos datos antes de usarlos en la query
    # param :   SQLDato - Tupla de los datos para la query          
    # return :  False / True si el campo está vacío
    def func_ComprobarDatos(self,SQLDatos = []):
        """Comprueba que no se pasen valores vacíos en campos. Los datos se 
        pasan como una tupla."""
        campoVacio = False
        for n in range(len(SQLDatos)):
            if len(str(SQLDatos[n]))==0:
                campoVacio = True

        return campoVacio        
            
    # Función:  func_Listar_Tablas
    # author :
    # Estado [D]esarrollo/[O]perativa: O    
    # since :   1.5             
    # uso   :   Listar las tablas disponibles
    def func_Listar_Tablas(self):
        """Muestra las tablas disponibles en una BBDD."""
        for (table_name,) in self.MyCursor:
            print(table_name)
