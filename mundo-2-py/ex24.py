#Crie um programa que leia dois valores e mostre um menu na tela:
#[1] somar
#[2] multiplicar
#[3] maior
#[4] novos números
#[5] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.
valor_1=float(input("Informe o primeiro valor:"))
valor_2=float(input("Informe o segundo valor:"))
while True:
    print("""Agora, escolha uma das opções abaixo:
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa""")
    opção=int(input("Informe sua opção:"))
    if opção==1:
        print(f"A soma desses dois números é igual a {valor_1+valor_2}.")
        print("-"*50)
    elif opção==2: 
        print(f"Multiplicando esses números temos {valor_1*valor_2}.")
        print("-"*50)
    elif opção==3:
        if valor_1>valor_2: 
            print(f"O maior valor digitado foi {valor_1}.")
            print("-"*50)
        elif valor_1<valor_2: 
            print(f"O maior valor digitado foi {valor_2}.")
            print("-"*50)
        else: 
            print(f"O maior valor digitado foi {valor_1}.")
            print("-"*50)
    elif opção==4:
        print("-"*50)
        valor_1=float(input("Informe o primeiro valor:"))
        valor_2=float(input("Informe o segundo valor:"))
    elif opção==5: 
        print("Programa encerrado.")
        break