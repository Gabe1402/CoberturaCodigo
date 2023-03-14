from ParImpar import ParImpar

def test_add():
    PaIm = ParImpar()
    PaIm.add(2)
    PaIm.add(3)
    PaIm.add(10)
    PaIm.add(5)

def test_sumarPar():
    PaIm = ParImpar()
    assert PaIm.sumaPar() == 12

def test_sumarImpar():
    PaIm = ParImpar()
    assert PaIm.sumaImpares() == 8

def test_cuadradoLista():
    NList = [4, 9, 100, 25]
    PaIm = ParImpar()
    assert PaIm.cuadradoLista() == NList

