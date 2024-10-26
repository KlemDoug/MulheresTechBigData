###ESTRUTURAS DE CONDIÇÃO###

#IF ELSE x SWITCH CASE

#1) IF ELSE
mes=int(input('Digite um número entre 1 e 12:'))

if mes==1:
    print('Janeiro')
elif mes==2:
    print('Fevereiro')
elif mes==3:
    print('Março')
elif mes==4:
    print('Abril')
elif mes==5:
    print('Maio')
elif mes==6:
    print('Junho')
elif mes==7:
    print('Julho')
elif mes==8:
    print('Agosto')
elif mes==9:
    print('Setembro')
elif mes==10:
    print('Outubro')
elif mes==11:
    print('Novembro')
elif mes==12:
    print('Dezembro')
else:
    print('Por favor forneça um número válido.')
    mes=int(input('Digite um número entre 1 e 12:'))

#2) SWITCH CASE
   
mes=int(input('Digite um número entre 1 e 12:'))

meses={1:'Janeiro',2:'Fevereiro'}

#Atividades práticas com if/else e switch/case:

# 1) Escreva um programa para calcular e imprimir o número de lâmpadas necessárias para iluminar um determinado cômodo de uma residência. 
# Dados de entrada: a potência da lâmpada utilizada (em watts), as dimensões (largura e comprimento, em metros) do cômodo. Considere que 
# a potência necessária é de 3 watts por metro quadrado e a cada 3 m² existe um bocal para uma lâmpada;

# variáveis simples - são as que calculam a entrada de dados
lampada_potencia=float(input('Digite a potência da lâmpada (watts):')) 
largura_comodo=float(input('Digite a largura do cômodo:'))
comprimento_comodo=float(input('Digite o comprimento do cômodo:'))

#variáveis para o cálculo de área e de potência
area_comodo=largura_comodo*comprimento_comodo
potencia_real=3*lampada_potencia

#variáveis para o cálculo do número de lâmpadas e de bocais
numero_lampadas=int(potencia_real/lampada_potencia)
bocais=int(area_comodo/3)

#exibição dos resultados (quaisquer das formatações são válidas)
print('lâmpadas:',numero_lampadas)
print(f"Número de lâmpadas necessárias:{numero_lampadas}")
print(f"Número de bocais necessários:{bocais}" )


# 2) Escreva um programa para ler as dimensões de uma cozinha retangular (comprimento, largura e altura), calcular e escrever a quantidade de 
# caixas de azulejos para se colocar em todas as suas paredes (considere que não será descontada a área ocupada por portas e janelas). Cada caixa 
# de azulejos possui 1,5 m²;

# 3) Um motorista de táxi deseja calcular o rendimento de seu carro na praça. Sabendo-se que o preço do combustível é de R$ 4,87, escreva um 
# programa para ler: a marcação do odômetro (km) no início do dia, a marcação (km) no final do dia, o número de litros de combustível gasto e o 
# valor total (R$) recebido dos passageiros. Calcular e escrever: a média do consumo em km/L e o lucro (líquido) do dia;

# 4) Escreva um programa que leia o código de origem de um produto e imprima na tela a região de sua procedência, conforme a tabela que foi passada.
 
# Observação: caso o código não seja nenhum dos especificados, o produto deve ser encarado como “Importado”;

# 5) Escreva um programa que leia as notas das duas avaliações normais e a nota da avaliação optativa dos estudantes de uma turma. Caso o estudante não tenha feito a optativa, deve ser fornecido o valor -1. Calcular a média do semestre considerando que a prova optativa substitui a 
# nota mais baixa entre as duas primeiras avaliações. Escrever a média e mensagens que indiquem se o estudante foi aprovado, reprovado ou se 
# está em exame, de acordo com as informações abaixo: 
# Aprovado: média >= 6.0, Reprovado: média < 3.0, Exame: média >= 3.0 e < 6.0;

nota1=float(input('Primeira Nota:'))
nota2=float(input('Segunda Nota:'))
nota_opt=float(input('Nota Optativa:'))

if nota_opt != -1: 
    menor_nota=min(nota1,nota2)
    if nota_opt>menor_nota:
        if nota1==menor_nota:
            nota1=nota_opt
        else:
            nota2=nota_opt

media=(nota1+nota2)/2
print(f'Média:{media}')

if media >= 6.0:
    print("Aprovado")
elif media < 3.0:  

    print("Reprovado")
else:
    print("Exame de Recuperação")


# 6) Escreva um programa para ler um valor e escrever se é positivo ou negativo. Considere o valor zero como positivo.