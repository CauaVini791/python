#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
ano_nascimento=int(input("Digite o seu ano de nascimento:"))
idade=2022-ano_nascimento
faltam_anos=18-idade
passou_anos=idade-18
if ano_nascimento>2004:
    print("Acalme-se! Ainda não é sua hora de se alistar. Você só será obrigado se alistar daqui {} ano(s).".format(faltam_anos))
elif ano_nascimento==2004:
    print("Chegou sua hora de se alistar!")
else:
    print("Já passou do tempo de se alistar! Era pra você ter se alistado há {} ano(s).".format(passou_anos))