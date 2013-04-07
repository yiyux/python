nombre_archivo = raw_input("nombre del archivo? ")
if nombre_archivo != "":
	archivo = open (nombre_archivo, "r")
else:
	exit ()
	
total_linea = 0
total_char = 0

for linea in archivo:
	total_linea +=1
	for caracter in linea:
		total_char += 1

print "total lineas", total_linea
print "total caracteres", total_char