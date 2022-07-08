curso = {
    "nome": "Programando em python",
    "conteudos": [
        "Conceitos básicos da linguagem",
        "Biblioteca-padrão",
        "Coleções",
        "Estruturas de controle",
        "Funções e módulos",
        "Parâmetros default, variáveis e nomeados",
        "Programação funcional",
        "Classes e Objetos",
        "Herança e Polimorfismo",
        "Armazenamento de dados em arquivos",
        "Acesso a banco de dados",
        "Manipulação de API Rest",
        "Testes unitários"
                  ],
    "instrutor": {
        "Nome": "Júlio Pereira",
        "Contato": "33 99154-2651"
    },
    "alunos": [
        "Aldair Ribeiro",
        "André de Castro",
        "Danilo Pereira",
        "Elton Lima",
        "Fabio Ferraz",
        "Gideão Sudario",
        "Jefferson André",
        "Jeova Vieira",
        "Lucas Pires",
        "Marcelo São Pedro",
        "Meggy Mendes",
        "Michael Rochumback",
        "Nilza Ferreira",
        "Paulo Sergio"
    ]
}

# ========= USANDO  APENAS METHODOS, IF OU LIST COMPREENSHIONS

# CRIAR OS CONJUNTOS

# dicionario = {'produto':'maca', 'preco': 3.90}

# list_c = [x for x in dicionario.values()]
# print(list_c)

# frutas = ["apple", "banana", "cherry", "kiwi", "mango"]

# newlist = [x for x in frutas if "a" in x]
# texto_1 = 'julio'

# for x in texto_1:
#     print(x)

# if texto_1[0] == 'g':
#     print('tem')
# else:
#     print('nao')

# print(newlist)


# 1 - Lista de todas as KEYS do curso
keys_curso = [x for x in curso]

# 2 - Lista de tuplas para criar 5 relacionamento entre os alunos
# RESPOSTA => [(1,2),(3,5),(7,9),(2,2),(3,6)]
from random import sample

rel = [(sample([1,2,3,4,5], k=1)[0], sample([1,2,3,4,5], k=1)[0]) for x in range(5)]

# 3 - Lista com os nomes dos alunos
alunos = [x for x in curso["alunos"]]

# 4 - Lista com os nomes dos alunos MOSTRANDO APENAS AS TRÊS PRIMEIRAS LETRAS
"""
    DICA
    texto = 'Julio'
    print(texto[1:4]) # Imprime uli

"""
alunos_3_letras = [x[0:3] for x in curso["alunos"]]

# 5 - Lista de conteudos que COMECA COM A LETRA A
conteudo_a = [x for x in curso["conteudos"] if x[0] == 'a' or x[0] == 'A']


# ========= USANDO APENAS METHODOS, IF OU WHILE

conteudo_while = []

# 1 - Preencher o conjunto conteudo_while com uma lista de dicionarios dos conteudos conforme o exemplo:
# Exemplo: [{nome: "Conceitos básicos da linguagem", active: True}]

x = 0 

while x < len(curso["conteudos"]):
    conteudo = {'nome':curso["conteudos"][x], 'active': True}
    conteudo_while.append(conteudo)
    x += 1

# ========= USANDO APENAS METHODOS, IF OU FOR

curso_for = {}
alunos_for = []
conteudos_for = []
instrutor_for = {}

# 1 - preenche a coleção curso_for com os dados do curso e acrecenta o atributo active com valor true
for x in curso.items(): # ('chave', 'valor')
    curso_for[x[0]] = x[1]

curso_for['active'] = True

# 2 - preenche a coleção alunos_for com os nomes dos alunos.
# alunos = [x for x in curso["alunos"]]
for x in curso["alunos"]:
    alunos_for.append(x)

# 3 - preenche a coleção conteudos_for com os dados dos conteudos.
for x in curso["conteudos"]:
    conteudos_for.append(x)

# 4 - preenche a coleção instrutor_for com os dados dos instrutor e acrecentar os meios de contatos
for x in curso["instrutor"].items():
    instrutor_for[x[0]] = x[1]

instrutor_for['GitHub'] = 'http://'


# 5 - faça uma busca na coleção curso_for e imprime apenas os dados do instrutor
for x in curso_for['instrutor'].items():
    # print(x)
    pass

# 6 - faça uma busca na coleção alunos e imprime o aluno com index 5
# list_1 = ['a','b','c']
# list_1.index('c')

for x in alunos_for:
    if x == alunos_for[5]:
        print(x)

# 7 - Faça uma leitura na coleção conteudos_for ALTERANDO todos conteudos a partir do index 6 para "NÃO APLICADO"
for x in conteudos_for:
    posicao = conteudos_for.index(x)

    if posicao > 5:
        conteudos_for[posicao] = "NÃO APLICADO"
