def esBisiesto(year):
	if(year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
		return "SI"
	else:
		return "NO"

year = input ("ingrese anno? ")
print esBisiesto(year)
