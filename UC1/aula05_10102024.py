### ESTRUTURAS DE REPETIÇÃO ###

# FOR: sabemos a quantidade de vezes que o laço de repetição foi executado.

for i in range(5):
    numero=int(input('Digite um número:'))
    print(f'Dobro:{numero*2}')

# WHILE: queremos a repetição quando a condição for verdadeira.

#Exemplo1:
contador=0
while True:
    numero=int(input('Digite um número:'))
    print(f'Triplo:{numero*3}')
    contador=contador+1

#Exemplo2:
num=5
while num<3:
    print('teste')

# DO WHILE: similar ao 'WHILE', mas garante que o bloco seja lido ao menos 1 vez
# antes da verificação da condição.

num=5
while True:
    print('teste')
    if not(num<3):
        pass
