#Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
termo=primeiro_termo=float(input("Informe o primeiro termo da P.A:"))
razão=float(input("Informe a razão da P.A:"))
último_termo=primeiro_termo+(10*razão)
n=1
while n<10:
    print(termo)
    termo=termo+razão
    n=n+1
print(termo)