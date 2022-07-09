# FUNCAO

from math import sqrt


def somar(a, b):
    return (a + b)

if __name__ == '__main__':
    print('teste em soma: 2 + 3', somar(2,3))




def somar(a, b):
    return (a + b)

print('teste em soma: 2 + 3', somar(2,3))


# MULTIPLICACAO PEGAR DOIS VALORES E MULTIPLICAR
def multi(a,b):
    return(a*b)

print("func de multiplicacao:", multi(2,5))
#meggy

# FUNCAO DE SUBTRACAO, PEGAR DOIS VALORES
def sub(a,b):
  return (a-b)
#aldair

# FUNCAO DE DIVISAO, PEGAR DOIS VALORES
def dividir(c,d):
    return(c/d)

print('Divisao: ',dividir(25,5))
#lucas
# FUNCAO DE PRINTAR MENSAGEM, PEGAR A MESAGEM E PRINTA.
def reverse_message(a):
    print(a[::-1])

def baskara(a,b,c):
    # b² -4ac
    delta = b**2 - 4 * a * c
    if (delta < 0):
        return([])
    else:
        x1 = (-b + sqrt(delta)) / (2 * a)
        x2 = (-b - sqrt(delta)) / (2 * a)
        return[x1,x2]
        
def primeira_letra(a):
    return a[0]

# jefferson



# funcao de exponenciacao
def exponenc(n1, n2):
    return n1**n2

def covid(pais):
    return [mortes, casos]
#Elton


# FUNCA QUE ADICIONA UM CONTEUDO EM UMA LISTA, PEGAR A LISTA E O CONTEUDO PARA POR NELA.
def injetar_lista(lista, conteudo):
    return lista.append(conteudo)


# FUNCAO PARA MOSTRAR A HORA AGORA => DATATIME <=
from datetime import _time, datetime

print(datetime.now())

#RETORNA A HORA

# FUNCAO QUE IMPRIME A PRIMEIRA LETRA DO NOME, PEGAR UM NOME COMO TEXTO


# FUNCAO QUE IMPRIME UM NOME ALEATORIO DE UMA LISTA, RECEBE A LISTA.
# 
lista = [
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

from random import sample

def sorteio(candidatos):
    print(candidatos[sample(range(len(candidatos)), k=1)[0]])

print(sorteio(lista))




