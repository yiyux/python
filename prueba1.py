import math

def capitalFinal(ci, ti, y):
	return ci*(pow((1+float(ti)/100),y))

def calcularIntereses(ci, cf, y):
	a = float(cf/ci)
	b = 1/float(y)
	return pow(a,b)


cap_ini = input ("Capital Inicial?")
tasa_interes = input ("Tasa de interes (porcentaje)?")
years = input ("Numero de annos?")
cap_final = capitalFinal(cap_ini,tasa_interes,years)
print "El capital final es $", cap_final

print "Comprobando tasa de intereses..."
print "Capital Inicial $", cap_ini, " Capital Final: $", cap_final,
print "Annos: ", years, " Tasa de Interes:", 
print calcularIntereses(cap_ini,cap_final,years), " %"  

# mail fadi dayoub 
# fadidayoubpseli@gmail.com

	
