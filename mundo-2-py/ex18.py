#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
frase=input("Informe uma frase:").upper()
frase_sem_espaços=frase.replace(" ","")
frase_inversa=frase_sem_espaços[::-1]
if frase_sem_espaços==frase_inversa:
    print("É PALÍNDROMO.")
else:
    print("NÃO É PALÍNDROMO.")