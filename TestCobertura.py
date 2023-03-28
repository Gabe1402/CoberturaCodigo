from CoberturaCodigo import Palabras

def test_vocales():
    cobertura = Palabras()
    assert cobertura.vocales("Hola") == 2

def test_palabras():
    cobertura = Palabras()
    assert cobertura.numeroLetras("12345") == 5

