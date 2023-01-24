#Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
#a) Os 5 primeiros times.
#b) Os últimos 4 colocados.
#c) Times em ordem alfabética.
#d) Em que posição está o time da Chapecoense.
tupla="CORINTHIANS","PALMEIRAS","SANTOS","GRÊMIO","CRUZEIRO","FLAMENGO","VASCO","CHAPECOENSE","ATLÉTICO","BOTAFOGO","ATLÉTICO-PR","BAHIA","SÃO PAULO","FLUMINENSE","SPORT","VITÓRIA","CORITIBA","AVAÍ","PONTE PRETA","ATLÉTICO-GO"
print(f"Os 5 primeiros colocador são: {tupla[0:5]}.")
print(f"Os 4 últimos colocados são: {tupla[16:]}.")
print(f"Os times em ordem alfabética ficam assim: {sorted(tupla)}.")
print(f"A Chapecoense está na {tupla.index('CHAPECOENSE')+1} colocação.")