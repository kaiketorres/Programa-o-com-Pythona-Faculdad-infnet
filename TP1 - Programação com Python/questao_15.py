#Crie um programa que apresente ao usuário uma série de escolhas (como em uma história) e conduza a diferentes resultados com base nessas escolhas.

print("Você está em uma floresta mágica. Escolha o que fazer:")
print("1. Ir para a direita")
print("2. Ir para a esquerda")

escolha = input("Digite 1 ou 2: ")

if escolha == '1':
    print("Você encontrou uma cabana. Você decide entrar ou voltar.")
    print("1. Entrar na cabana")
    print("2. Voltar para a floresta")
    escolha2 = input("Digite 1 ou 2: ")
    
    if escolha2 == '1':
        print("Dentro da cabana, você encontra um tesouro!")
    elif escolha2 == '2':
        print("Você volta para a floresta e encontra uma saída.")
    else:
        print("Escolha inválida. Você fica perdido na floresta.")
    
elif escolha == '2':
    print("Você encontra um rio. Você decide atravessar ou seguir ao longo do rio.")
    print("1. Atravessar o rio")
    print("2. Seguir ao longo do rio")
    escolha2 = input("Digite 1 ou 2: ")
    
    if escolha2 == '1':
        print("Você atravessa o rio e encontra uma aldeia.")
    elif escolha2 == '2':
        print("Você segue ao longo do rio e encontra uma ponte.")
    else:
        print("Escolha inválida. Você fica parado na margem do rio.")
    
else:
    print("Escolha inválida. Você fica perdido na floresta.")
2
