#Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
numero=int(input("Informe um número:"))
print("Escolha a forma de conversão de acordo com a tabela abaixo:")
print("[1] para converter em BINÁRIO")
print("[2] para converter em OCTAL")
print("[3] para converter em HEXADECIMAL")
conversão=int(input("Qual será a base de conversão?"))
if conversão==1:
    print("O {} convertido em binário fica {}.".format(numero,bin(numero)[2:]))
elif conversão==2:
    print("O {} convertido em octal fica {}.".format(numero,oct(numero)[2:]))
elif conversão==3:
    print("O {} convertido em hexadecimal fica {}.".format(numero,hex(numero)[2:]))
else:
    print("Opção inválida. Tente novamente!")