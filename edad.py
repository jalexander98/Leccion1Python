#!/usr/bin/env python
# -*-  coding: utf-8  -*-
nombre = raw_input ("nombre de usuario")
actual = input ( "ingrese año actual")
nacimiento =input ("ingrese año de nacimiento")
edad = actual-nacimiento
print nombre + "su edad es de :"+ str(edad) 
if edad <=12:
	print "niño"
else:
	print  "joven"