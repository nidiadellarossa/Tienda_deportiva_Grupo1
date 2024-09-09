from .aritmetica import sumar, restar, multiplicar, dividir, sumar_n, promedio_n

import random

def generate_captcha():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operacion = random.choice(['sumar', 'restar', 'multiplicar', 'dividir', 'sumar_n_numeros', 'promedio_n' ])
    operando = ""

    if operacion == 'sumar':
        resultado = sumar(num1, num2)
        operando = f"{num1} + {num2}"
    elif operacion == 'restar':
        resultado = restar(num1, num2)
        operando = f"{num1} - {num2}"
    elif operacion == "multiplicar":
        resultado = multiplicar(num1, num2)
        operando = f"{num1} * {num2}"
    elif operacion == "dividir":
        try:
            resultado = dividir(num1, num2)
        except ValueError as e:
            print(str(e))
            return False
        operando = f"{num1} / {num2}"
    elif operacion == "sumar_n_numeros":
        numeros = [random.randint(1, 10) for _ in range(random.randint(2, 5))]
        resultado = sumar_n(*numeros)
        operando = f"Suma de {', '.join(map(str, numeros))}"
    else:
        numeros = [random.randint(1, 10) for _ in range(random.randint(2, 5))]
        resultado = promedio_n(numeros)
        operando = f"Promedio de {', '.join(map(str, numeros))}"

    return operando, resultado

