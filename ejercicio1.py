__author__ = 'yiyux'

# Tarea, teniendo la siguiente pista
# K -> M
# O -> Q
# E -> G
# que significa el siguiente texto

# g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp.
# bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle.
# sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.

def buscarLetra(letraBuscar, diccionario):
    for letra in diccionario:
        if letra == letraBuscar:
            encontrado = True
            break
        else:
            encontrado = False
    return encontrado


diccionario = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r",
               "s", "t", "u", "v", "w", "x", "y", "z"]
salto = 2
#print diccionario.index("c")
texto = raw_input("ingrese texto?")
palabra = ""
for letra in texto:
    if buscarLetra(letra, diccionario):
        indice = diccionario.index(letra) + salto
        if indice > (len(diccionario) - 1):
            indice -= len(diccionario)
        palabra += diccionario[indice]
        #print diccionario.index(letra),
    else:
        palabra += letra

print palabra

