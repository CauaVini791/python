#Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
from random import randint
soma=0
n=0
def sorteia(lista):
    for c in range(5):
        lista_números.append(randint(1,100))

def somaPar(lista):
    for c in range(len(lista_números)):
        if c%2==0:
            soma+=c

lista_números=[]
sorteia(lista_números)
somaPar(lista_números)
print(lista_números,soma)