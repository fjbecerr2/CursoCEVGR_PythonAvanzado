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
import time
import re

__version__ = "0.0" # Versión Activa

# func_Generar_Scrapy_Proyecto
# since :    0.0
# Estado [D]esarrollo/[O]perativa: O   
# author :
# uso :     Genera un  proyecto Scrapy
# return: False / True (Operacion Termino)
def func_Generar_Scrapy_Proyecto():
    """Genera un proyecto Scrapy."""
    print "Generando un proyecto"
    MyProyecto = "scrapy startproject Proyscrapytemp"
    if os.system(MyProyecto) == 0: # Error de sistema
        return False            
    else:
        return True
            
# fun_DefinirItem_Scrapy_Proyecto
# since :    0.0
# Estado [D]esarrollo/[O]perativa: O   
# author :
# uso :     Añade los items al fichero generado por Scrapy
# return: False / True (Operacion Termino)          
def fun_DefinirItem_Scrapy_Proyecto():
    """Añade los item al fichero items.py generado por Scrapy."""
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

    # Sustituir el contenido del fichero
    itemFile = open(dir_scrapy,"w") 
    for linea in itemFile_Temp: 
        itemFile.write(str(linea))
    itemFile.close()
   
    
 # func_Generar_ScrapySpiders_Fichero
# since :    0.0
# Estado [D]esarrollo/[O]perativa: O   
# author :
# uso :     Crea un fichero para el spider
# return: False / True (Operacion Termino)             
def func_Generar_ScrapySpiders_Fichero():
    # Localizar los directorios
    dir_aplicacion = os.getcwd()
    dir_scrapy = dir_aplicacion 
    MySistemaOP = os.name # Sistema operativo
    
    # Localizar el directorio de spiders
    if MySistemaOP == "nt": # Presumiblemente Windows
        dir_scrapy = dir_aplicacion + '\\Proyscrapytemp\\Proyscrapytemp\\spiders'
            
    if MySistemaOP == "posix": # Presumiblemente Linux
        dir_scrapy = dir_aplicacion + '/Proyscrapytemp/Proyscrapytemp/spiders'          
        
    os.chdir(dir_scrapy) # Posicionarse en el directorio
    # Crear el fichero
    spiderFile = open("dmoz_spider.py","w")
    spiderFile.write("from scrapy.spider import BaseSpider\n")
    spiderFile.write("from scrapy.selector import HtmlXPathSelector\n\n")
    spiderFile.write("class DmozSpider(BaseSpider):\n")
    spiderFile.write("\tname = \"dmoz\"\n")
    spiderFile.write("\tallowed_domains = [\"dmoz.org\"]\n")
    spiderFile.write("\tstart_urls = [\n")
    spiderFile.write("\t\t\"http://www.dmoz.org/Computers/Programming/Languages/Python/Books/\",\n")
    spiderFile.write("\t\t\"http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/\"\n")
    spiderFile.write("\t]\n\n")
    spiderFile.write("\tdef parse(self, response):\n")
    spiderFile.write("\t\thxs = HtmlXPathSelector(response)\n")
    spiderFile.write("\t\tsites = hxs.select(\'//ul/li\')\n")
    spiderFile.write("\t\tfor site in sites:\n")
    spiderFile.write("\t\t\ttitle = site.select('a/text()').extract()\n")
    spiderFile.write("\t\t\tlink = site.select('a/@href').extract()\n")
    spiderFile.write("\t\t\tdesc = site.select('text()').extract()\n\n")
    spiderFile.close() 
    os.chdir(dir_aplicacion)
    
def func_Generar_ScrapyPider_Resultados():
    os.system("scrapy crawl dmoz")


    
    
    
        
    
        

