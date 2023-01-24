#Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
numero=int(input("Informe um número:"))
for c in range(0,11):
    print(f"{numero} x {c} = {numero*c}")