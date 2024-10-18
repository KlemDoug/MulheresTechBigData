import random

def gerando_numeros(quantidade,valor_minimo,valor_maximo):
    return [random.randint(valor_minimo,valor_maximo) for i in range(quantidade)]

def somar(a,b):
    return a+b

def subtrair(a,b):
    return a-b

def multiplicar(a,b):
    return a*b

def dividir(a,b):
    if b != 0:
        return a/b
    else:
        return "Divisões por zero não são permitidas."