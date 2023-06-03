## QUESTÃO 02 TRABALHO AV2 Paradigmas em Python
## Aluno: Andrew Luiz Santos Carvalho

'''Considere um sistema Python onde os dados são armazenados em
dicionários. Nesse sistema existe um dicionario principal e o dicionário de backup. Cada vez
que o dicionário principal atinge tamanho 5, ele imprime os dados na tela e apaga o seu conteúdo.
Crie um programa que insira dados em um dicionário, realizando o backup a cada dado e
excluindo os dados do dicionário principal quando ele atingir tamanho 5. (1,0 ponto).
'''


def salvando_dados(dicionario, dicionario2):
    dicionario2.update(dicionario)
    dicionario.clear()


def inserindo_dados(dicionario, dicionario2, k, v):
    dicionario[k] = v
    if len(dicionario) == 5:
        print("Realizando backup dos dados:")
        salvando_dados(dicionario, dicionario2)
        print("Backup concluído.")




dicionario = {}
dicionario2 = {}
cont = 0
for i in range(1,6):
    k = input("Digite a keys: ")
    v = input("Digite o values: ")

    cont +=1
    if cont == 5:
        print(f'Dicionário principal: ', dicionario)

    inserindo_dados(dicionario, dicionario2, k, v)

for i in range (1,101):
    print(f'Esvaziando dicionário principal.....{i}%')

print(f"Dicionário 100% Vazio {dicionario}")

print("Dicionário de backup: ")
print(dicionario2)