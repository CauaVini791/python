#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.
while True:
    sexo=input("Informe seu sexo (F/M):").upper()
    if sexo=="F" or sexo=="M":
        print("Resposta válida.")
        break
    else:
        print("Resposta inválida. Tente novamente.")
        continue