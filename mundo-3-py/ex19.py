#Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.
dicionário_escola={}
dicionário_escola["Nome"]=input("Nome do aluno: ")
dicionário_escola["Média"]=float(input("Média do aluno: "))
if dicionário_escola["Média"]>=7:
    print(f"""Nome: {dicionário_escola[0]['Nome']}
Média: {dicionário_escola['Média']}
Situação: Aprovado""")
elif 5<=dicionário_escola["Média"]<7:
    print(f"""Nome: {dicionário_escola['Nome']}
Média: {dicionário_escola['Média']}
Situação: Recuperação""")
else: 
    print(f"""Nome: {dicionário_escola['Nome']}
Média: {dicionário_escola['Média']}
Situação: Reprovado""")