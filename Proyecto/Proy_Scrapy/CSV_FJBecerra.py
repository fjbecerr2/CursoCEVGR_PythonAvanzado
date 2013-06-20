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

__version__ = "0.0" # Versión Activa

# func_Limpiar_FicheroFuente
# since :    0.0
# Estado [D]esarrollo/[O]perativa: O   
# author :
# uso :     Formatear fichero temporal Scrapy
def func_Limpiar_FicheroFuente():
    """Formatea el fichero temporal extraido por scrapy."""
    # Tomas los directorios para localizar los archivos 
    dir_aplicacion = os.getcwd()
    dir_scrapy = dir_aplicacion 
    MySistemaOP = os.name   # Sistema Operativo
    
    # Localizar los directorios y ficheros creados por Scrapy
    if MySistemaOP == "nt": # Presumiblemente Windows
        dir_scrapy = dir_aplicacion + '\\Proyscrapytemp\\scrapycsv.txt'
            
    if MySistemaOP == "posix": # Presumiblemente Linux
        dir_scrapy = dir_aplicacion + '/Proyscrapytemp/scrapycsv.txt'

    # Leer el contenido del fichero
    fileFuente = open(dir_scrapy,"r")   
        
    csvTabla = [] # Lista de todas las líneas    
    listHtlm = ["<li>","</li>","<strong>","</strong>","'>","\u20ac"]
        
    # Esta operación es para los títulos
    for txtLinea in fileFuente.readlines(): 
            if txtLinea.find("data="): # Localizar la posición del separador                
                csvLineaTemp = txtLinea[txtLinea.find("data=")+7:] # Asignar el dato hasta el separador            
            csvTabla.append(csvLineaTemp) # Añadir los datos de la primera línea

    # Eliminar los elementos de código HTML
    for contador in range(len(csvTabla)): # Recorrer el fichero
        csvLineaTemp = csvTabla[contador]
        for eHtml in listHtlm:            
            csvLineaTemp  = csvLineaTemp.replace(str(eHtml),"")
        
        # Límpias Unicode  (!sin tiempo para afinarlo!)
        csvLineaTemp  = csvLineaTemp.replace("\\xe1","a")    
        csvLineaTemp  = csvLineaTemp.replace("\\xe9","e")    
        csvLineaTemp  = csvLineaTemp.replace("\\xed","i")        
        csvLineaTemp  = csvLineaTemp.replace("\\xf3","o")    
        csvTabla[contador] = csvLineaTemp  
        
    #for elemento in csvTabla:
        #print  elemento, len(csvTabla)
    
    # Generar Columnas
    Columna_Titulo = []
    Columna_Autor = []
    Columna_Precio = []  
    limite = len(csvTabla) / 3 # Calcular el salto entre datos
        
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
        if contador <=  limite-1: # 1/3 Titulo            
            Columna_Titulo.append(csvTabla[contador])            
        if contador >= limite and contador < (limite+limite): # 2/3 Autor            
            Columna_Autor.append(csvTabla[contador] )        
        if contador > (limite+limite)-1: # 3/3 Precio            
            Columna_Precio.append(csvTabla[contador] )
    
    # Recomponer la tabla de datos
    csvTabla = []
    
    #for contador in range(len(Columna_Titulo)):
        #temp = Columna_Titulo[contador] 
    csvTabla.append(Columna_Titulo)
    csvTabla.append(Columna_Autor)
    csvTabla.append(Columna_Precio)
   
    # Limpiar los \n residuales
    for elemento in csvTabla:   
        for contador in range(len(elemento)):
            temp =  str(elemento[contador])
            temp = temp.replace("\n","")
            elemento[contador] = temp
    
    TablaTemp = []
    TablaFin = []
    print len(csvTabla)
    print len(csvTabla[0])
    
    for exterior in range(0,len(csvTabla[0])):
        for interior in range(0,3):
            TablaTemp.append(csvTabla[interior][exterior])      
        TablaFin.append(TablaTemp)
        TablaTemp = []
    
    
    #print TablaFin
    for elemento in TablaFin:
        print  elemento
    
    fileFuente.close()
    os.chdir(dir_aplicacion)            
#<HtmlXPathSelector xpath='/html/body/div/div[4]/div/div[2]/div/div/div[2]/h2/a/@title' data=u'Redes. Administraci\xf3n Y Mantenimiento De'>
#<HtmlXPathSelector xpath='/html/body/div/div[4]/div/div[2]/div/div/div[2]/ul/li[1]' data=u'<li>Meyers, Mike</li>'>
#<HtmlXPathSelector xpath='//html//body//div//div[4]//div//div[2]//div//div//div[2]//ul//li[3]/strong' data=u'<strong>72,50\u20ac</strong>'>
