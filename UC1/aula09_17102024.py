#FUNÇÕES (continuação)

#ATIVIDADE ASSISTIDA: (criação de um módulo personalizado)

# Criem quatro funções para cada uma das operações aritméticas fundamentais (soma, subtração, multiplicação e divisão). Cada função
# deve receber dois números como parâmetros e retornar o resultado apropriado.

# Em seguida, todas as funções devem ser integradas em um único programa: criem uma nova função para gerar números aleatórios e aplicá-los 
# às operações anteriores.

#Resolução:
 
#Funções Matemáticas:

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

print(somar(40,20))
print(subtrair(40,20))
print(multiplicar(40,20))
print(int(dividir(40,20))) #toda divisão em python, por padrão, nos fornece um resultado float.

import random

def gerando_numeros(quantidade,valor_minimo,valor_maximo): #for na forma 'condensada' ou 'compacta'
    return [random.randint(valor_minimo,valor_maximo) for i in range(quantidade)]

# def doisnum_aleatorios(qtd,numero_minimo,numero_maximo): #for na forma 'tradicional'
#     for i in range(qtd):
#         return random.randint(numero_minimo,numero_maximo)

numeros=gerando_numeros(2,1,100)
n1,n2= numeros[0],numeros[1]

print(numeros)
print(f"Números gerados:{n1} e {n2}.")
print(f"Soma:{somar(n1,n2)}")
print(f"Subtração:{subtrair(n1,n2)}")
print(f"Multiplicação:{multiplicar(n1,n2)}")
print(f"Divisão:{dividir(n1,n2)}")

import UC1.calculadora as calculadora
from UC1.calculadora import somar
print(somar(2,5))

##################################################################################################

#TRATAMENTO DE EXCEÇÕES (TRY e EXCEPT)

#Reformulando a função de divisão:
def dividir(a,b):
    try:
        resultado=a/b
    except ZeroDivisionError:
        print("Erro: não é possível dividir por zero!")
    else:
        print(f"O resultado da divisão é {resultado}.")
    finally:
        print("Operação finalizada.")

#Testando a função reformulada:
dividir(20,2)
dividir(20,0)
dividir(2,5)

#ATIVIDADE: (github)

#Leia três pares de números inteiros fornecidos pelo usuário, calcule e imprima a soma de cada par separadamente. Utilize 
#tratamento de erros para garantir que os valores inseridos sejam válidos e, se o número for ÍMPAR, ter uma exceção personalizada.


