#aça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
parâmetros=[]
maior=0
def maior(n):
    for c in range(len(parâmetros)):
        if c==0:
            maior=parâmetros[0]
        else:
            if parâmetros[c]>maior:
                maior=parâmetros[c]
    print(f"O maior número digitado foi o {maior}")

while True:
    parâmetros.append(float(input("Digite: ")))
    pergunta=input("Deseja continuar? [S/N] ").upper()
    if pergunta=="N":
        break
    elif pergunta=="S":
        continue
    else: 
        print("ERRO! Digite S ou N.")
        pergunta=input("Deseja continuar? [S/N] ").upper()
maior(parâmetros)