class ParImpar:
    numeros=[]

    def add(self, n:int):
        self.numeros.append(n)

    def sumaPar(self):
        n:int = 0
        for i in self.numeros:
            if i%2 == 0:
                n += i
        return n

    def sumaImpares(self):
        n:int = 0
        for i in self.numeros:
            if i%2 != 0:
                n += i
        return n

    def cuadradoLista(self):
        powN =[]
        for i in self.numeros:
            powN.append(i*i)
        return powN
