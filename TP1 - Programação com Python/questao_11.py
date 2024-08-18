#Faça um programa que simule o lançamento de um dado. O usuário deve escolher quantos dados jogar e o programa deve exibir os resultados.

import random

quantidade_dados = int(input("Quantos dados você quer lançar? "))

for i in range(quantidade_dados):
    resultado = random.randint(1, 6)
    print(f"Dado {i+1}: {resultado}")
