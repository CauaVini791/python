#Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
#resposta1
dict_perguntas={"Nome": input("Digite seu nome: "),
"Idade": 2022-int(input("Digite seu ano de nascimento: ")),
"Carteira": int(input("Digite o número da sua carteira de trabalho: "))}
if dict_perguntas["Carteira"]!=0:
    dict_perguntas["Ano_Cont"]=int(input("Digite o ano de contratação: "))
    dict_perguntas["Salário"]=float(input("Digite o salário: "))
    dict_perguntas["Ano_Apos"]=(dict_perguntas["Ano_Cont"]+35)-(2022-dict_perguntas["Idade"])
print(f"""Nome: {dict_perguntas['Nome']}
Idade: {dict_perguntas['Idade']}
Carteira: {dict_perguntas['Carteira']}""")
if dict_perguntas["Carteira"]!=0:
    print(f'''Ano de contratação: {dict_perguntas['Ano_Cont']}
Salário: {dict_perguntas['Salário']:.2f}
Idade para se aposentar: {dict_perguntas['Ano_Apos']} anos''')

#resposta2
dict_perguntas={}
while True:
    dict_perguntas['Nome']=input("Digite seu nome: ")
    if dict_perguntas['Nome']=="":
        print("Prgorama encerrado!")
        break
    dict_perguntas["Idade"]=2022-int(input("Digite seu ano de nascimento: "))
    dict_perguntas["Carteira"]=int(input("Digite o número da sua carteira de trabalho: "))
    if dict_perguntas["Carteira"]!=0:
        dict_perguntas["Ano_Cont"]=int(input("Digite o ano de contratação: "))
        dict_perguntas["Salário"]=float(input("Digite o salário: "))
        dict_perguntas["Ano_Apos"]=(dict_perguntas["Ano_Cont"]+35)-(2022-dict_perguntas["Idade"])
    print(f"""Nome: {dict_perguntas['Nome']}
    Idade: {dict_perguntas['Idade']}
    Carteira: {dict_perguntas['Carteira']}""")
    if dict_perguntas["Carteira"]!=0:
        print(f'''Ano de contratação: {dict_perguntas['Ano_Cont']}
    Salário: {dict_perguntas['Salário']:.2f}
    Idade para se aposentar: {dict_perguntas['Ano_Apos']} anos''')
    dict_perguntas.clear()