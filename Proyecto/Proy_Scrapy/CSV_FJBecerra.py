# -*- coding: utf-8 -*-
# coding: UTF-8 
# Python Version: 2.7.3
# Ejercicio: CSV_FJBecerra.py
# Versión: 0
# Curso: Programación avanzada en Python
# Centro: CEVUG
# Autor: Fco. J. Becerra
# email: fjbecerr@gmail.com
# Fecha: 18/06/2013
# Operativa: Proyecto - Obtener un fichero operativo CSV de los datos Scrapy

import os
import unicodedata

__version__ = "0.0" # Versión Activa df

# func_Limpiar_FicheroFuente
# since :    0.0
# Estado [D]esarrollo/[O]perativa: O   
# author :
# uso :     Formatear fichero temporal Scrapy
# param: TablaDatos - List para devolver los datos formateados
def func_Limpiar_FicheroFuente(MyScrapyCsv,TablaDatos = [], MyDominio ="Dominio", MyUrl="MyUrl"):
    """Formatea el fichero temporal extraido por scrapy."""
    # Ejemplo de origen de datos antes de procesar
    #<HtmlXPathSelector xpath='/html/body/div/div[4]/div/div[2]/div/div/div[2]/h2/a/@title' data=u'Redes. Administraci\xf3n Y Mantenimiento De'>
    #<HtmlXPathSelector xpath='/html/body/div/div[4]/div/div[2]/div/div/div[2]/ul/li[1]' data=u'<li>Meyers, Mike</li>'>
    #<HtmlXPathSelector xpath='//html//body//div//div[4]//div//div[2]//div//div//div[2]//ul//li[3]/strong' data=u'<strong>72,50\u20ac</strong>'>
    
    csvTabla = [] # Lista de todas las líneas   
        
    # Leer el contenido del fichero
    fileFuente = open(MyScrapyCsv,"r")   
    
        
    # Esta operación es para los títulos
    for txtLinea in fileFuente.readlines(): 
            if txtLinea.find("data="): # Localizar la posición del separador                
                csvLineaTemp = txtLinea[txtLinea.find("data=")+7:] # Asignar el dato hasta el separador            
            csvTabla.append(csvLineaTemp) # Añadir los datos de la primera línea
    # Eliminar los elementos de código HTML
    fun_Reformatear(csvTabla)
        
   
    # Crear las columnas para cada tipo de datos    
      # Generar Columnas
    Columna_Dominio = []
    Columna_url = []
    Columna_Titulo = []
    Columna_Autor = []
    Columna_Precio = []  
    limite = len(csvTabla) / 3 # Calcular el salto entre grupos de datos (son tres datos por registro)
        
    for contador in range(len(csvTabla)):
        # Tenemos tres datos en el contenedor con el formato
        #  Titulo
        #   Titulo
        # ...
        # Autor
        # Autor
        # ....
        # Precio
        # Precio
        # ...
        #
        # De manera que dividiremos los registros en tres para crear columans y luego agruparlas
        # El primer 1 de 3 de las líneas totales son Titulo            
        if contador <=  limite-1: 
            Columna_Titulo.append(csvTabla[contador]) 
            Columna_Dominio.append(MyDominio)
            Columna_url.append(MyUrl)
        # El siguiente grupo 2 de 3 de las línea son Autor                      
        if contador >= limite and contador < (limite+limite): 
            Columna_Autor.append(csvTabla[contador] )        
        # Grupo final 3 de 3 de las línea son Precio                
        if contador > (limite+limite)-1: 
            Columna_Precio.append(csvTabla[contador] )
    
    # Recomponer la tabla de datos
    csvTabla = []
    
    # Añadirle las columna ya preparadas    
    csvTabla.append(Columna_Dominio)
    csvTabla.append(Columna_url)
    csvTabla.append(Columna_Titulo)
    csvTabla.append(Columna_Autor)
    func_Formatear_Precios(Columna_Precio) # Convertir en float
    csvTabla.append(Columna_Precio)
    
    TablaTemp = [] # Para agrupar cada registro Título, Autor, Precio
    #TablaDatos = [] # Para contener todos los registros
    
    for exterior in range(0,len(csvTabla[0])): # Número total de registros
        for interior in range(0,5): # Agrupados de cinco en cinco
            TablaTemp.append(csvTabla[interior][exterior])  # Crea un registro     
        TablaDatos.append(TablaTemp) # Añade el registro generado
        TablaTemp = [] # Límpia para componer el siguiente registro
    
    # Ejemplo de resultado 
    # [["Titulo1", "Autor1, 20.10],
    # ["Titulo1", "Autor1, 20.10]]
       
    fileFuente.close()
    

# func_Limpiar_FicheroFuente
# since :    0.0
# Estado [D]esarrollo/[O]perativa: O   
# author :
# uso :     Formatear fichero temporal Scrapy
# param: TablaDatos - List para devolver los datos formateados
def fun_Reformatear(TablaDatos = []):
    """Formatea los datos extraidos con scrapy."""
    
    # Código residual a la extracción que tendremos que limpiar
    listHtlm = ["<li>","</li>","<strong>","</strong>","'>","\u20ac","\xa6","</l"]
    
    for contador in range(len(TablaDatos)): # Recorrer los datos
        csvLineaTemp = TablaDatos[contador]
        for eHtml in listHtlm:            
            csvLineaTemp  = csvLineaTemp.replace(str(eHtml),"")
        # Límpias Unicode, como los acentos (!sin tiempo para afinarlo!)
        csvLineaTemp  = csvLineaTemp.replace("\\xe1","a")
        csvLineaTemp  = csvLineaTemp.replace("\\xc1","A")
        
        csvLineaTemp  = csvLineaTemp.replace("\\xe9","e") 
        csvLineaTemp  = csvLineaTemp.replace("\\xc9","E")       
        
        csvLineaTemp  = csvLineaTemp.replace("\\xed","i")        
        csvLineaTemp  = csvLineaTemp.replace("\\xf3","o")   
        csvLineaTemp  = csvLineaTemp.replace("\\xa6"," ") 
        csvLineaTemp  = csvLineaTemp.replace("\\xaa"," ") 
        csvLineaTemp  = csvLineaTemp.replace("\\xf1","ñ") 
        csvLineaTemp  = csvLineaTemp.replace("\\xc3\xb1","ñ") 
        
        
        
        TablaDatos[contador] = csvLineaTemp  

    # Limpiar los \n residuales
    for contador in range(len(TablaDatos)):
        temp =  str(TablaDatos[contador])
        temp = temp.replace("\n","")
        TablaDatos[contador] = temp
 
# func_Formatear_Precios
# since :    0.0
# Estado [D]esarrollo/[O]perativa: O   
# author :
# uso :     Convertir los precios a float
# param: PrecioOrigen - List para devolver los datos formateados 
def func_Formatear_Precios(PrecioOrigen = []):
    """Formate los precios y los convierte en float."""
    precioTemp = []
    for contador in range(len(PrecioOrigen)):
        temp = PrecioOrigen[contador]
        temp = temp.replace(",",".")
        PrecioOrigen[contador] = temp
        
    for contador in range(len(PrecioOrigen)):
        temp = 0
        try:
            temp = float(PrecioOrigen[contador])
        except:
            temp = 0
        PrecioOrigen[contador] = temp
        
    
                
   
    
