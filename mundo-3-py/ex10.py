#Crie um programa que vai ler vários números e colocar em uma lista.                  
#Depois disso, mostre:                                                                                                                                                
#A) Quantos números foram digitados.                                      
#B) A lista de valores, ordenada de forma decrescente.
#C) Se o valor 5 foi digitado e está ou não na lista.
lista_números=[]
n=0
while True:
    lista_números.append(float(input("Digite um número:")))
    n+=1
    pergunta=input("Deseja continuar (S/N)?").upper()
    if pergunta=="S":
        continue
    else:
        lista_números.sort(reverse=True)
        print(f"Você digitou {n} elementos.")
        print(f"Os valores em ordem decrescente são {lista_números}")
        if 5 in lista_números:
            print("O valor 5 faz parte da lista.")
        else:
            print("O número 5 não foi encontrado na lista.")
        break