class Palabras:
    def vocales(self, palabra):
        numerovocales = 0
        for i in palabra:
            if (i == "a") or (i == "e") or (i == "i") or (i == "o") or (i == "u"):
                numerovocales += 1

        return numerovocales

    def numeroLetras(self, palabra):
        numeropalabras = 0
        for i in palabra:
            numeropalabras +=1
        return numeropalabras


