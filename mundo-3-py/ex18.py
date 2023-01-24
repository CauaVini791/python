#Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
lista_geral=[]
lista_individual=[]
pergunta=0
outra_pergunta=0
while True:
    lista_individual.append(input("Nome: "))
    lista_individual.append(float(input("Nota 1: ")))
    lista_individual.append(float(input("Nota 2: ")))
    lista_individual.append((lista_individual[1]+lista_individual[2])/2)
    lista_geral.append(lista_individual[:])
    lista_individual.clear()
    pergunta=input("Deseja continuar? [S/N] ").upper()
    if pergunta=="S":
        continue
    else:
        break
for c in range(len(lista_geral)):
    print(f"{c+1} - Nome: {lista_geral[c][0]} -> Média = {lista_geral[c][3]}")
while True:
    outra_pergunta=int(input("Deseja ver as notas de qual aluno? (999 para encerrar o programa) "))
    if outra_pergunta!=999:
        print(f"As notas de {lista_geral[outra_pergunta-1][0]} foram {lista_geral[outra_pergunta-1][1]} e {lista_geral[outra_pergunta-1][2]}")
    else: 
        print("Programa encerrado.")
        break