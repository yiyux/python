__author__ = 'Karl Fischer'


class Cripto:
#Constructor
    def __init__(self, x):
        self.a1 = "abcdefghijklmnopqrstuvwxyz"
        self.a2 = x
        for c in self.a1:
            if not (c in x):
                self.a2 += c

    #Metodo cifrar:
    def cifrar(self, x):
        palabra_crypt = ""
        for letra in x:
            indice = self.a1.find(letra)
            if indice != -1:
                count = 0
                for letra_crypt in self.a2:
                    if count == indice:
                        palabra_crypt = palabra_crypt + letra_crypt
                    count += 1
        print palabra_crypt
        #Metodo descrifrar:

        #def descifrar(self, x):
        #completar


texto = Cripto("sur")
print texto.a1
print texto.a2
palabra = raw_input("Ingrese palabra sin espacio: ")
texto.cifrar(palabra)

