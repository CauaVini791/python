#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
lista_números=[]
while True:
    número=float(input("Digite um número:"))
    if número not in lista_números:
        lista_números.append(número)
        print("Valor adicionado com sucesso...")
    else:
        print("Valor duplicado. Não vou adicionar...")
    pergunta=input("Deseja continuar (S/N)?").upper()
    if pergunta=="S":
        continue
    else:
        break
lista_números.sort()
print(f"Você digitou os valores {lista_números}")