## QUESTÃO 01 TRABALHO AV2 Paradigmas em Python
## Aluno: Andrew Luiz Santos Carvalho

'''
(Dados Aglomerados) Desenvolva um programa em Python que cadastre informações de várias
pessoas (nome, idade e CPF) e depois coloque em um dicionário. Depois remova todas as
pessoas menores de 18 anos do dicionário e coloque em outro dicionário. (1,0 ponto
'''

def cadastro_pessoas():
    nome = input(f"Digite o nome da {i}ª pessoa: ")
    idade = int(input(f"Digite a idade da {i}ª pessoa: "))
    if idade >= 1 and idade <= 17:
        menor_idade = idade
    cpf = input(f"Digite o CPF da {i}ª pessoa: ")
    pessoa = {"idade": idade, "cpf": cpf}
    menores_idade = {"idade": menor_idade, "cpf": cpf}
    return nome, pessoa, menores_idade, idade


pessoas = {}
menor = {}
cont = int(input('Qnts pessoas que deseja cadastrar ? '))

for i in range(1, cont + 1):
    nome, pessoa, menores_idade, idade = cadastro_pessoas()
    pessoas[nome] = pessoa
    menor[nome] = menores_idade

if (idade <= 17):

    print("\n\nPessoas menores de 18 anos:")
    for nome, pessoa in menor.items():
        print(f"Nome: {nome}, Idade: {pessoa['idade']}, CPF: {pessoa['cpf']}")

print("\n\nPessoas maiores de 18 anos:")
for nome, pessoa in pessoas.items():
    print(f"Nome: {nome}, Idade: {pessoa['idade']}, CPF: {pessoa['cpf']}")
