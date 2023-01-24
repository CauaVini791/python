#Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:                                                                                                                                                                            
#a) de 1 até 10, de 1 em 1                                                                                                                                              
#b) de 10 até 0, de 2 em 2                                                                                                                                            
#c) uma contagem personalizada

from time import sleep
def contador(i,f,p):
    if i<f:
        for c in range(i,f,p):
            print(c,end=" ",flush=True)
            sleep(0.5)
        print("FIM!")
        contador()
    else:
        if p>0:
            for c in range(i,f,-p):
                print(c,end=" ",flush=True)
                sleep(0.5)
            print("FIM!")
            contador()
        else:
            for c in range(i,f,p):
                print(c,end=" ",flush=True)
                sleep(0.5)
            print("FIM!")
            contador()

contador(1,10,1)
contador(10,0,2)
contador(int(input("Digite o início: ")),int(input("Digite o fim: ")),int(input("Digite o passo: ")))