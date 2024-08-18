#Faça um programa que converta um número fornecido de minutos em horas e minutos, e depois faça o inverso, convertendo horas e minutos de volta para minutos totais.

minutos = int(input('Digite o número de minutos: '))

horas = minutos // 60
minutos_restantes = minutos % 60

print(f'{minutos} minutos é igual a {horas} horas e {minutos_restantes} minutos.')

horas = int(input('Digite o número de horas: '))
minutos = int(input('Digite o número de minutos: '))

minutos_totais = (horas * 60) + minutos

print(f'{horas} horas e {minutos} minutos é igual a {minutos_totais} minutos totais.')
