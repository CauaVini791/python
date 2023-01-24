#Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
dict_informações={}
lista_gols=[]
lista_informações=[]
pergunta=0
outra_pergunta=0
while True:
    dict_informações['Nome']=input("Digite o nome do jogador: ")
    partidas=int(input("Quantas partidas ele jogou? "))
    for c in range(partidas):
        lista_gols.append(int(input("Quantos gols ele fez na partida " + str(c+1) + "? ")))
    dict_informações['Gols']=lista_gols[:]
    dict_informações['Total_Gols']=sum(lista_gols)
    lista_informações.append(dict_informações.copy())
    dict_informações.clear()
    lista_gols.clear()
    pergunta=input("Deseja continuar? [S/N] ").upper()
    if pergunta=="S":
        continue
    else:
        break
print("-"*50)
for i,c in enumerate(lista_informações):
    print(f"{i+1} - {c['Nome']} -> Gols: {c['Gols']} -> Total: {c['Total_Gols']}")
while True:
    outra_pergunta=int(input("Mostrar dados de qual jogador? (999 para parar) "))
    if outra_pergunta>len(lista_informações):
        print("ERRO! Não existe jogador com esse código.")
        outra_pergunta=int(input("Mostrar dados de qual jogador? (999 para parar) "))
        continue
    elif outra_pergunta==999:
        print("Programa encerrado! Volte sempre.")
        break
    else:
        print(f"LEVANTAMENTO DO JOGADOR: {lista_informações[outra_pergunta-1]['Nome']}")
        for i,c in enumerate(lista_informações[outra_pergunta-1]['Gols']):
            print(f"No jogo {i+1} fez {c} gols.")