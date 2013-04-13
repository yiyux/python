__author__ = 'Karl Fischer'


class Matriz:

    def __init__(self, n, m):
        self.M = []
        self.dim = [n, m]
        for i in range(1, n, 1):
            a = []
            for j in range(1, m, 1):
                a.append(0)
            self.M.append(a)

    def get(self, i, j):
        a = self.M[i - 1]
        b = a[j - 1]
        return b

    def set(self, i, j, valor):
        a = self.M[i - 1]
        a.insert(j - 1, valor)

    def __add__(self, m1):
        if self.dim == m1.dim:
            aux = Matriz(self.dim[0], self.dim[1])
            for i in range(1, self.dim[0], 1):
                for j in range(1, self.dim[1], 1):
                    valor = self.get(i, j) + m1.get(i, j)
                    aux.set(i, j, valor)
            return aux
        else:
            return None

    def __str__(self):
        aux = ""
        for i in range(1, self.dim[0], 1):
            aux += "[ "
            for j in range(1, self.dim[1], 1):
                aux += str(self.get(i, j)) + " "
            aux += "]"
        return aux

matriz1 = Matriz(2, 2)
matriz1.set(1, 2, 69)
print matriz1
matriz2 = Matriz(2, 2)
matriz2.set(1, 2, 1)
print matriz2
print matriz1.get(1, 2)
print matriz2.get(1, 2)
matriz3 = matriz1.__add__(matriz2)
print matriz3