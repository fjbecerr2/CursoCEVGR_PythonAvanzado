# -*- coding: utf-8 -*-
# coding: UTF-8 
# Python Version: 2.7.3
# Ejercicio: Scrapy_FJBecerra.py
# Versión: 0
# Curso: Programación avanzada en Python
# Centro: CEVUG
# Autor: Fco. J. Becerra
# email: fjbecerr@gmail.com
# Fecha: 18/06/2013
# Operativa: Proyecto

import os
import re

__version__ = "1.0" # Versión Activa

# func_Generar_Scrapy_Proyecto
# Estado [D]esarrollo/[O]perativa: O   
# uso :     Genera un  proyecto Scrapy
# return: False / True (Operacion Termino)
def func_Generar_Scrapy_Proyecto():
    """Genera un proyecto Scrapy desde la consola."""
    MyProyecto = "scrapy startproject Proyscrapytemp"    
    if os.system(MyProyecto) == 0: 
        return True           
    else:
        return False # Error de sistema
            
# fun_DefinirItem_Scrapy_Proyecto
# Estado [D]esarrollo/[O]perativa: O   
# uso :     Añade los items al fichero generado por Scrapy
# return: False / True (Operacion Termino)          
def fun_DefinirItem_Scrapy_Proyecto():
    """Añade los item al fichero items.py generado por Scrapy."""
    try:
        # Tomas los directorios para localizar los archivos 
        dir_aplicacion = os.getcwd()
        dir_scrapy = dir_aplicacion 
        MySistemaOP = os.name   # Sistema Operativo
    
        # Localizar los directorios y ficheros creados por Scrapy
        if MySistemaOP == "nt": # Presumiblemente Windows
            dir_scrapy = dir_aplicacion + '\\Proyscrapytemp\\Proyscrapytemp\\items.py'
            
        if MySistemaOP == "posix": # Presumiblemente Linux
            dir_scrapy = dir_aplicacion + '/Proyscrapytemp/Proyscrapytemp/items.py'

        # Leer el contenido del fichero
        itemFile = open(dir_scrapy,"r")    
        itemFile_Temp = itemFile.readlines()
        itemFile.close()
    
        # Recorrer el contenido del fichero
        for contador in range(len(itemFile_Temp)):
            # Usar una expresión regular para localizar la última línea  por defecto "pass"
            if re.match("^([a-zA-Z\s]+)pass",itemFile_Temp[contador]) :
                # Sustituir el pass y añadir las línea de los items
                itemFile_Temp[contador]  = "\ttitle = Field()\n"
                itemFile_Temp.append("\tlink = Field()\n")
                itemFile_Temp.append("\tdesc = Field()\n")

        # Sustituir el contenido del fichero por las líneas formateadas
        itemFile = open(dir_scrapy,"w") 
        for linea in itemFile_Temp: 
            itemFile.write(str(linea))
    
        itemFile.close()
        os.chdir(dir_aplicacion)  # Regesar al directorio superior
        return True
    except:
        os.chdir(dir_aplicacion)  # Regesar al directorio superior
        return False

# func_Generar_AgapeaSpiders_Fichero
# Estado [D]esarrollo/[O]perativa: O   
# uso :     Crea un fichero para el spider
# param: 
#       MyProyecto - Directorio del proyecto
#       MyUrl - Url para generar los div
# return: False / True (Operacion Termino)             
def func_Generar_AgapeaSpiders_Fichero(MyProyecto, MyUrl = "http://www.agapea.com/Informatica-cn142p1i.htm"):
    """Generar un fichero de spider para la url que pasamos."""
    # Localizar los directorios
    dir_aplicacion = os.getcwd()
    dir_scrapy = dir_aplicacion 
    MySistemaOP = os.name # Sistema operativo
    
    # Localizar el directorio de spiders
    if MySistemaOP == "nt": # Presumiblemente Windows
        dir_scrapy = MyProyecto + '\\spiders'
            
    if MySistemaOP == "posix": # Presumiblemente Linux
        dir_scrapy = MyProyecto + '/spiders'          

    # Comprobar si se genero el proyecto
    if not os.path.isdir(MyProyecto):
        print "El proyecto no existe"
        return False
    
    
    os.chdir(dir_scrapy) # Posicionarse en el directorio
    try:
        # Crear el fichero
        spiderFile = open("agapea_spider.py","w")
        spiderFile.write("from scrapy.spider import BaseSpider\n")
        spiderFile.write("from scrapy.selector import HtmlXPathSelector\n")
        spiderFile.write("from scrapy.http import Request\n\n")
        spiderFile.write("class agapeaSpider(BaseSpider):\n")
        spiderFile.write("\tname = \"agapea\"\n")
        spiderFile.write("\tallowed_domains = [\"agapea.com\"]\n")
        spiderFile.write("\tstart_urls = [\n")
        spiderFile.write("\t\t\""+MyUrl+"\",\n")
        spiderFile.write("\t]\n\n")
        spiderFile.write("\tdef parse(self, response):\n")
        # Fichero Origen para CSV
        spiderFile.write("\t\tficheroCSV=open(\"scrapycsv.txt\",\"w\")\n")
    
        spiderFile.write("\t\thxs = HtmlXPathSelector(response)\n")
        spiderFile.write("\t\t# Titulo\n")   
        spiderFile.write("\t\tsites = hxs.select('/html/body/div/div[4]/div/div[2]/div/div/div[2]/h2/a/@title')\n")
        spiderFile.write("\t\tfor site in sites:\n")
        # Código para guardar en un fichero CSV 
        spiderFile.write("\t\t\tstrTemp = str(site)\n") 
        spiderFile.write("\t\t\tstrTemp+=\"\\n\"\n")
        spiderFile.write("\t\t\tficheroCSV.write(strTemp)\n")       
        spiderFile.write("\t\t# Autor\n")           
        spiderFile.write("\t\tsites = hxs.select('/html/body/div/div[4]/div/div[2]/div/div/div[2]/ul/li[1]')\n")
        spiderFile.write("\t\tfor site in sites:\n")    
        # Insertar código para guardar en un fichero CSV        
        spiderFile.write("\t\t\tstrTemp = str(site)\n") 
        spiderFile.write("\t\t\tstrTemp+=\"\\n\"\n")    
        spiderFile.write("\t\t\tficheroCSV.write(strTemp)\n")       
        spiderFile.write("\t\t# Precio\n") 
        spiderFile.write("\t\tsites = hxs.select('//html//body//div//div[4]//div//div[2]//div//div//div[2]//ul//li[3]/strong')\n")
        spiderFile.write("\t\tfor site in sites:\n")
        spiderFile.write("\t\t\tstrTemp = str(site)\n") 
        spiderFile.write("\t\t\tstrTemp+=\"\\n\"\n")
        spiderFile.write("\t\t\tficheroCSV.write(strTemp)\n") 
        spiderFile.write("\t\tficheroCSV.close()\n")    
    
        os.chdir(dir_aplicacion) 
        return True
    except:
        os.chdir(dir_aplicacion) 
        return False
           

# func_Generar_ScrapyPider_Resultados
# Estado [D]esarrollo/[O]perativa: O   
# uso :     Estrae los datos usando el spider
# return: False / True (Operacion Termino)             
def func_Generar_ScrapyPider_Resultados():
    """Genera extracción de datos usando spider desde consola."""
    # Localizar los directorios
    dir_aplicacion = os.getcwd()
    dir_scrapy = dir_aplicacion 
    MySistemaOP = os.name # Sistema operativo
    
    # Localizar el directorio de spiders
    if MySistemaOP == "nt": # Presumiblemente Windows
        dir_scrapy = dir_aplicacion + '\\Proyscrapytemp'
            
    if MySistemaOP == "posix": # Presumiblemente Linux
        dir_scrapy = dir_aplicacion + '/Proyscrapytemp'          
        
    os.chdir(dir_scrapy) # Posicionarse en el directorio
    if os.system("scrapy crawl agapea") == 0:
        os.chdir(dir_aplicacion)  
        return True
    else:
        return False # Error al lanzarlo
        
    


    
    
    
        
    
        

