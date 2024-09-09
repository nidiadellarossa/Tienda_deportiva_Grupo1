def sumar(a, b):
    return round(a + b, 2)

def restar(a, b):
    return round(a - b, 2)

def dividir(a, b):
    try:
        return round(a / b, 2)
    except ZeroDivisionError:
        raise ValueError("No se puede dividir por cero")

def multiplicar(a, b):
    return round(a * b, 2)

def sumar_n(*args):
    return round(sum(args), 2)

def promedio_n(numeros = []):
    if not numeros:
        raise ValueError("No se pueden calcular promedios sin números")
    return round(sum(numeros) / len(numeros), 2)