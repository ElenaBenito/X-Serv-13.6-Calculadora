#!/usr/bin/python3

import math
import sys

def sumar(sumando1, sumando2):
	"""Sums two integer/floats
	Returns integer/float."""
	return sumando1 + sumando2

def restar(sumando1, sumando2):
	"""Subtracts two integer/floats
	Returns integer/float."""
	return sumando1 - sumando2

def multiplicar(factor1, factor2):
	"""Multiplies two integer/floats
	Returns integer/float."""
	return factor1 * factor2

def dividir(factor1, factor2):
	"""Divides two integer/floats
	Returns integer/float."""
	return factor1 / factor2

name = str(sys.argv[1])

try:
	if name == "sumar":
		try:
			first = int(sys.argv[2])
			second = int(sys.argv[3])
			print(sumar(first, second))
		except ValueError:
			print("Por favor introduce números enteros")
	elif name == "restar":
		try:
			first = int(sys.argv[2])
			second = int(sys.argv[3])
			print(restar(first,second))
		except ValueError:
			print("Por favor introduce números enteros")
	elif name == "multiplicar":
		try:
			first = int(sys.argv[2])
			second = int(sys.argv[3])
			print(multiplicar(first, second))
		except ValueError:
			print("Por favor introduce números enteros")
	elif name == "dividir":
		try:
			first = int(sys.argv[2])
			second = int(sys.argv[3])
			print(dividir(first, second))
		except ValueError:
			print("Por favor introduce números enteros")	
		except ZeroDivisionError:
			print ("No se puede divir entre 0")
	else:
		print("Función no contemplada, opciones: sumar, restar, multiplicar y dividir")
except IndexError:
	print ("Faltan datos, por favor escribe de la forma 'python3 calculadora.py funcion op1 op2'")
