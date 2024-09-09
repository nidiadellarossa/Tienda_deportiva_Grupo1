import aritmetica

def test_sumar():
    assert aritmetica.sumar(2, 3) == 5.00
    assert aritmetica.sumar(-2, 3) == 1.00
    assert aritmetica.sumar(0, 0) == 0.00

def test_restar():
    assert aritmetica.restar(5, 3) == 2.00
    assert aritmetica.restar(-2, 3) == -5.00
    assert aritmetica.restar(0, 0) == 0.00

def test_dividir():
    assert aritmetica.dividir(6, 3) == 2.00
    assert aritmetica.dividir(-6, 3) == -2.00
    try:
        aritmetica.dividir(6, 0)
        assert False, "No se debe permitir la división por cero"
    except ValueError:
        pass

def test_multiplicar():
    assert aritmetica.multiplicar(2, 3) == 6.00
    assert aritmetica.multiplicar(-2, 3) == -6.00
    assert aritmetica.multiplicar(0, 0) == 0.00

def test_sumar_n():
    assert aritmetica.sumar_n(1, 2, 3) == 6.00
    assert aritmetica.sumar_n(-1, -2, -3) == -6.00
    assert aritmetica.sumar_n(0, 0, 0) == 0.00

def test_promedio_n():
    assert aritmetica.promedio_n([1, 2, 3]) == 2.00
    assert aritmetica.promedio_n([-1, -2, -3]) == -2.00
    try:
        aritmetica.promedio_n()
        assert False, "No se debe permitir calcular promedio sin números"
    except ValueError:
        pass

if __name__ == "__main__":
    test_sumar()
    test_restar()
    test_dividir()
    test_multiplicar()
    test_sumar_n()
    test_promedio_n()