#Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
tupla = "zero","um","dois","três","quatro","cinco","seis","sete","oito","nove","dez","onze","doze","treze","catorze","quinze","dezesseis","dezessete","dezoito","dezenove","vinte"
numero=int(input("Digite um número entre 0 e 20:"))
while True:
    if numero>=0 and numero<=20:
        print(f"O número {numero} por extenso é {tupla[numero]}.")
        break
    else:
        print("Tente novamente. ESCOLHA UM NÚMERO ENTRE 0 e 20.")
        numero=int(input("Digite um número entre 0 e 20:"))
        continue