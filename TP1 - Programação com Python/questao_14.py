#Escreva um programa que permita ao usuário votar em três opções diferentes e, no final, exiba o número de votos de cada opção.

votos_opcao1 = 0
votos_opcao2 = 0
votos_opcao3 = 0

for i in range(5): 
    voto = int(input("Vote em uma opção (1, 2 ou 3): "))
    if voto == 1:
        votos_opcao1 += 1
    elif voto == 2:
        votos_opcao2 += 1
    elif voto == 3:
        votos_opcao3 += 1
    else:
        print("Opção inválida. Vote novamente.")


print(f"Opção 1 recebeu {votos_opcao1} votos.")
print(f"Opção 2 recebeu {votos_opcao2} votos.")
print(f"Opção 3 recebeu {votos_opcao3} votos.")
