__author__ = 'Karl Fischer'


def leerArchivo(archivo):
    if archivo != "":
        L = []
        for linea in open(archivo, "r"):
            L.append(linea.split(":"))
        return L
    else:
        return ""


def buscarCurso(alumnos, cursos, ramo):
    Listado = []
    for curso in cursos:
        if curso[1] == ramo+"\n" or curso[1] == ramo:
            for alumno in alumnos:
                if curso[0] == alumno[0]:
                    Listado.append(alumno[1])
    return Listado

archivo_nombres = leerArchivo("nombres.txt")
archivo_curso = leerArchivo("cursos.txt")
ramo = raw_input("Codigo del curso?")
print buscarCurso(archivo_nombres, archivo_curso, ramo)


