#Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.                                  
#Ex:                                                                                                                                                                        
#escreva(‘Olá, Mundo!’) Saída:                                                                                                                         
#~~~~~~~~~~~                                                                                                                                                           
#Olá, Mundo!                                                                                                                                                         
#~~~~~~~~~~~        

def escreva(palavra):
    print(len(palavra)*"=")   
    print(palavra)
    print(len(palavra)*"=")               

while True:
    palavra=input("Digite: ")
    escreva(palavra)