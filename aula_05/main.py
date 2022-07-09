# FUNCOES

def somar(a,b=0):
    return a+b

soma = somar(30)

# print(soma)


# FACA UMA FUNCAO QUE SOMA OS VALORES E RECEBE VALORES ILIMITADOS

# def func(x, *args):
#     print(x)
#     print(args)

# func(1, 2, 3, 4, 5)

# def soma(*balinha):
#     somatorio = 0
#     for x in balinha:
#         somatorio += x
#     return somatorio

# print (soma(1,2,3,4 ))


# ARGS ; KARGS

def soma(*args):
    somatorio = 0
    for x in args:
        somatorio += x
    return somatorio


# FUNCAO QUE PRECISA CALCULAR O JUROS

# def calcular_juros(**kargs):
#     preco = kargs['preco']
#     juros = kargs['juros']

#     p_juros = preco * juros /100

#     print(preco + p_juros)
    

# calcular_juros(preco=100, juros=20) 

# def soma(a, b):
#     print(a + b)
    
# print(soma(4, 8))

# print('==========' * 10)

#-----------------------------------------------------


# def ehPar(n):
#     return n % 2 == 0

# print(ehPar(3))
# print(ehPar(8))


import pandas


# AMBIENTE DE DESENVOLVIMENTO
#ENV

# VARIAVEIS
# COLECOES (LIST, TUPLAS, DICT) 
# IF
# LOOP (FOR, WHILE)
# FUNCAO ()
# CLASSES ()

# BANCOS DE DADOS
# CONSTRUIR API  ===== 



# CLASSES ==> 




class Pessoa:
    def __init__(self, nome, idade=0, peso=0, altura=0.0):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def get_dados(self):
        return [self.nome, self.idade, self.peso, self.altura]
    
    def set_dados(self, data): 
        # data = [nome,idade,peso,altura] {nome: joao, idade: 19, peso: 40, altura: 1.5} (nome,idade,peso,altura)
        for pessoa in data:
            arquivo = open('dados.txt', 'w')
            for x in data:
                for y in x:
                    arquivo.write(f'{y}; ')
                arquivo.write(f'\n')
            arquivo.close()
            return 'setouuuu'

    def get_dados(self):
        arquivo = open('dados.txt', 'r')
        return arquivo




    def nome_em_maiusculo(self):
        return self.nome.upper()

    def __nome_minusculo(self):
        return self.nome.lower()


    

    
pessoa_2 = Pessoa('Julio', '33 991542651')

print(pessoa_2.get_dados())
# print(pessoa_2.__nome_minusculo())


class Calculador:
    def __init__(self, num1, num2 = 10):
        self.num1 = num1
        self.num2 = num2

    def sum(self):
        return self.num1 + self.num2

    def sub(self):
        return self.num1 - self.num2
    
    def mult(self):
        return self.num1 * self.num2
    
    def div(self):
        return self.num1 / self.num2

    def get_dados():
        return ''
    


valor = Calculador(10,20)

# print(valor.sum(20))








pessoa_3 = Pessoa('Ricardo', '11 92928394')


