###AULA06 - 11/10/2024###

#RESOLUÇÃO EXERCÍCIO 5:

# Definindo o número de alunos
# num_alunos = 20

# # Estrutura de repetição para processar as notas de cada aluno
# for i in range(1, num_alunos + 1):
#     print(f"Aluno {i}:")
    
#     # Entrada de dados
#     nota1 = float(input("Digite a nota da primeira avaliação: "))
#     nota2 = float(input("Digite a nota da segunda avaliação: "))
#     nota_optativa = float(input("Digite a nota da avaliação optativa (ou -1 se não fez): "))

#     # Substituir a menor nota pela optativa, se ela for maior
#     if nota_optativa != -1:
#         menor_nota = min(nota1, nota2)
#         if nota_optativa > menor_nota:
#             if nota1 == menor_nota:
#                 nota1 = nota_optativa
#             else:
#                 nota2 = nota_optativa

#     # Cálculo da média
#     media = (nota1 + nota2) / 2

#     # Exibindo resultado e status
#     print(f"Média do semestre: {media:.2f}")
    
#     if media >= 6.0:
#         print("Aprovado")
#     elif media < 3.0:
#         print("Reprovado")
#     else:
#         print("Exame")

#ATIVIDADE DE FIXAÇÃO:

# Desenvolva um programa que guarde os dados de 10 pessoas que estão se candidatando a uma vaga de emprego, sabendo que candidatos 
# menores de 18 anos não podem participar. Os dados coletados são: nome, data de nascimento, telefone, e-mail, formação acadêmica e 
# experiência profissional.

#RESOLUÇÃO:
        
        # Variável para armazenar os candidatos válidos
# candidatos = []
# contador = 0  # Contador para garantir que 10 candidatos sejam processados

# # Enquanto não atingirmos 10 candidatos válidos
# while contador < 10:
#     nome = input("Digite o nome do candidato: ")
#     idade = int(input("Digite a idade do candidato: "))
    
#     # Verificar se o candidato tem idade mínima de 18 anos
#     if idade < 18:
#         print("Candidato menor de idade. Não pode participar.")
#     else:
#         telefone = input("Digite o telefone: ")
#         email = input("Digite o e-mail: ")
#         formacao = input("Digite a formação acadêmica: ")
#         experiencia = input("Digite a experiência profissional: ")
        
#         # Armazenar os dados do candidato
#         candidatos.append({
#             'nome': nome,
#             'idade': idade,
#             'telefone': telefone,
#             'email': email,
#             'formacao': formacao,
#             'experiencia': experiencia
#         })
        
#         contador += 1  # Incrementa o contador para processar o próximo candidato

# # Exibe a quantidade de candidatos válidos cadastrados
# print(f"{len(candidatos)} candidatos cadastrados com sucesso.")

#ESTRUTURAS DE ARMAZENAMENTO

#LISTAS 'conversão:list()'
candidatos=[] #lista vazia
lista1=[2,4,6,8,10] #type(list1)=list
print(lista1)
print(lista1[0])
print(lista1[1])
print(lista1[2])
print(lista1[4])
print(lista1[-1])
print(lista1[-2])
lista1.append(20)
lista1.insert(26,3)
lista1.insert(2,33)
print(lista1)
print(len(lista1))

#TUPLAS 'conversão:tuple()'
senhas=() #tupla vazia

#DICIONÁRIOS  'conversão:dict()'
estados_uf={} #dicionário vazio