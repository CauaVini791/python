#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
import random
a1=input("Informe o nome do primeiro aluno:")
a2=input("Informe o nome do segundo aluno:")
a3=input("Informe o nome do terceiro aluno:")
a4=input("Informe o nome do quarto aluno:")
lista=[a1,a2,a3,a4]
escolhido=random.choice(lista)
print(escolhido)