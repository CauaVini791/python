#Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.
termo=primeiro_termo=int(input("Informe o primeiro termo da P.A:"))
razão=int(input("Informe a razão da P.A:"))
último_termo=primeiro_termo+(10*razão)
n=1
total=0
mais=10
while mais!=0:
    total=total+mais
    while n<=total:
        print(termo, end=" ")
        termo=termo+razão
        n=n+1
    print(termo)
    mais=int(input("Você quer mostrar mais quantos termos?"))