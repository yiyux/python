def getsexo(alumno):
	return alumno/100

def edad(alumno):
	return alumno%100


alumno = 1
porcentaje = 0
total = 0
tot_m = 0
tot_ed = 0
while alumno > 0:
	alumno = input("codigo?")
	if alumno == 0:
		break
	total += 1
	if(edad(alumno) >= 35 and edad(alumno) <= 45):
		porcentaje += 1
	if getsexo(alumno) == 2:
		tot_m += 1
		tot_ed = tot_ed + edad(alumno)
if total > 0:
	print "porcentaje = ", porcentaje*100/total, " %"
else:
	exit ()
	print "porcentaje = 0 %"
if tot_m > 0 :
	print "mujeres = ", tot_ed/tot_m, " annos"
else:
	print "mujeres = 0 annos"		