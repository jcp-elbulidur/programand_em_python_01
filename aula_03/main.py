from data import *

# Alunos
alunos = [
    {"nome": aluno_1}
]

print(alunos) # alunos com um aluno

for x in range(1,14): # 1, 2, 3
    alunos.append(globals()[f'aluno_{x}']) #A funcao GLOBALS() nao e bom usar em grandes projetos. Se usar com cautela.

print(alunos) #alunos com todos os alunos


#Atividade
atividades = [atividade_1, atividade_2]

#Status
status = (status_1, status_2, status_3)

# Curso
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
    "alunos": alunos
}

# ESTRUTURA DE REPETICAO
tamanho = len(curso["conteudos"])



# =================  ENTENDENDO O WHILE ==================
x = 0

# ler cada conteudo dos conteudos do curso
while x < 13:

    # verifica se a posicao X em conteudos e igual "Estruturas de controle"
    if curso["conteudos"][x] == "Estruturas de controle":
        #se for faz isso
        print('AQUI ESTAMOS TRABALHANDO...')
        break
    else:
        print(curso["conteudos"][x])
    x += 1
else:
    pass
    print('Estes sao os conteudos!!!')


# =================  ENTENDENDO O FOR ==================
number = [0,1,2,3]

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
    "alunos": alunos
}

for x in curso:
    if x == "conteudos":
        for c in curso[x]:
            # print(c)
            pass


hh = ('nome', 'Programando em python')

print(hh.index('nome'))

lista_modelo = [1,2,3,4,5,6]

lista_c = [h for h in lista_modelo if h == 1]

print(lista_c)
