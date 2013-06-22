# -*- coding: utf-8 -*-
# coding: UTF-8 
# Python Version: 2.7.3
# Ejercicio: CRUD_Main_FJBecerra.py
# Versión: 0
# Curso: Programación avanzada en Python
# Centro: CEVUG
# Autor: Fco. J. Becerra
# email: fjbecerr@gmail.com
# Fecha: 18/06/2013
# Operativa: Proyecto

import Proy_GTK		# Paquete GTK


__version__ = "1.0" # Versión Activa

# Datos Generales BBDD
MyDatosConexion = ["localhost","BDSCRAPY_SEARCH","scrapyUser","scrapypw","TBSCRAPY_SEARCH_URLS"]

if __name__ == "__main__":
    app = Proy_GTK.GUI(MyDatosConexion)        
    app.main()
	
