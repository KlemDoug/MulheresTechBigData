###ASSUNTO1###
# print('string')
#  #comando para exibir meu conteúdo no terminal.
'''
Dentro dos tipos de arquivo em Python,
temos os tipo texto que são conhecidos
como STRINGS; no exemplo acima, eu utilizei
o comando PRINT para exibir uma string no meu
terminal Python.
'''
# print('morango','  banana') #string
# print(123) #1 int
# print(37438,23534) #2 int
# print(2963.44) #float
# print(True) #boolean
# print(False) #boolean
# print(None) #none
# print(['string']) #listas
# print(('string')) #tupla
# print({'string':'texto'}) #dicionário


# ###CONDICIONAIS E IDENTAÇÃO### ---04/10/2024---

# temperatura1=36 #Cada VARIÁVEL armazena apenas 1 INFORMAÇÃO por vez. Se o nome da variável for o mesmo, o Python irá SOBRESCREVER essa informação.
# temperatura2=37.5 #Por isso cada temperatura ao lado está com um nome diferente.
# temperatura3=39.6 
# print (temperatura1,temperatura2,temperatura3)

# if temperatura1<36: #Nosso primeiro teste lógico. Sempre termino com ':'
#     print("Você não está com febre.") #Aqui temos uma regra de IDENTAÇÃO: toda resposta à minha condição deve estar DENTRO do meu if (lembrem-se da tecla TAB para corrigir a identação)
# elif temperatura1==36 and temperatura1<=37.5: #Nosso segundo teste lógico. Sempre termino com ':'
#     print("Você está febril.")
# else: #Última opção condicional. É requisitada quando todas as condições anteriores deram FALSE. Haverão momentos em que o 'else' não precisará ser escrito (quando eu não desejo dar resposta ao 'else')
#     print("Você está febre.")

fruta1='jambo'
fruta2='maçã'
fruta3='uva'
fruta4='maçã'
num1=67
num2=12
num3=12.0
num4=67.1

print(fruta1==fruta3)
fruta1=fruta3
print(fruta1)

print(fruta1==fruta4) #F
print(fruta2==fruta4) #V
print(fruta3==fruta4) #F
print(num1==num2) #F
print(num1!=num2) #V
print(num1>num2) #V
print(num1<num2) #F
print(num2==num3) #V
print(num1!=num4) #V
