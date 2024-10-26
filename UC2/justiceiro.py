import random

# Gerar uma lista de números de 1 a 19
numeros = list(range(1, 20))

# Embaralhar os números aleatoriamente
random.shuffle(numeros)

# Dividir os números em grupos de 4 ou 5
grupos = []
tamanho_grupo = 4

while numeros:
    # Alterna entre grupos de 4 e 5 membros para manter a distribuição
    if tamanho_grupo == 4 and len(numeros) >= 5:
        tamanho_grupo = 5
    elif tamanho_grupo == 5 and len(numeros) >= 4:
        tamanho_grupo = 4
    grupo = numeros[:tamanho_grupo]
    grupos.append(grupo)
    numeros = numeros[tamanho_grupo:]

# Exibir os grupos formados
for i, grupo in enumerate(grupos, start=1):
    print(f"Grupo {i}: {grupo}")

 

