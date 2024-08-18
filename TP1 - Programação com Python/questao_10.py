import random

personagens = ['um astronauta', 'uma princesa', 'um dragão']
acoes = ['encontrou um mapa', 'salvou o mundo', 'descobriu um segredo']
locais = ['em um planeta distante', 'em um castelo encantado', 'em uma floresta misteriosa']


personagem = random.choice(personagens)
acao = random.choice(acoes)
local = random.choice(locais)


historia = f"{personagem} {acao} {local}."


print(historia)
