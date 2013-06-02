#!/usr/bin/python
# -*- coding: utf-8 -*-
# coding: UTF-8 
# Python Version: 2.7.3
# Ejercicio: Identificar_Fecha_FjBecerra.py
# Versión: 
# Curso: Programación avanzada en Python
# Centro: CEVUG
# Autor: Fco. J. Becerra
# email: fjbecerr@gmail.com
# Fecha: 02/06/2013
# Operativa: Patrones de filtro usando Expresiones Regulares

import re

# Ejemplo de formato válido "Granada 5/Ago/2012 2:23 AM "
Ejemplo_Patron = "Granada 05/Ago/2012 02:23 AM "
patron_ciudad = "^([a-zA-Z\s]+)"              # Cualquier ciudad, válidos sólo los espacios
   
patron_dia_fecha = "([0-2]{1}[0-9]{1}|[3]{1}[0-1]{1})" # 1 o 2 dígitos hasta 31 días
patron_ano_fecha = "[2]{1}[0-9]{3}[\s]"     # 4 dígitos y mayor que 2000
patron_separador_fecha = "[/]"
patron_meses_fecha = "(Ene|Feb|Mar|Abr|May|Jun|Jul|Ago|Sep|Oct|Nov|Dic)" # 3 Primeras letras y sólo meses que existan
patron_fecha = patron_dia_fecha + patron_separador_fecha + patron_meses_fecha + patron_separador_fecha + patron_ano_fecha

patron_hora_hora = "[0-2]{1}[0-9]{1}"       # 1 o 2 dígitos
patron_separador_hora = "[:]"               # 
patron_minutos_hora = "[0-5]{1}[0-9]{1}"    # 1 o 2 dígitos
patron_final_hora = "[\s](AM|PM)$"          # Teminar con AM o PM

patron_horas = patron_hora_hora + patron_separador_hora + patron_minutos_hora + patron_final_hora
patron = patron_ciudad + patron_fecha + patron_horas

# --------- Programa --------------

print "Tendra que introducir 5 Fechas para testear el funcionamiento"
print "Introduzca segun el ejemplo: " + Ejemplo_Patron
for n in range(0,5):
    cadena = raw_input("\tCadena para horas? ")
    if re.search(patron,cadena):
        print "OK"
    else:
        print "No OK"
