#Neste exercício, você deverá escrever um programa em Python que verifique se um número fornecido pelo usuário é par ou ímpar. Imprima uma mensagem indicando se o número é par ou ímpar

numero = int(input("Digite um número: "))

if numero % 2 == 0:
    print(f"O número {numero} é par.")
else:
    print(f"O número {numero} é ímpar.")
