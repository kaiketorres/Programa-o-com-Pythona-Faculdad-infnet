#Desenvolva um programa que verifique se uma palavra ou frase inserida pelo usuário é um palíndromo (lê-se igual de trás para frente).

entrada = input("Digite uma palavra ou frase: ")

entrada_limpa = entrada.replace(" ", "").lower()

if entrada_limpa == entrada_limpa[::-1]:
    print("É um palíndromo!")
else:
    print("Não é um palíndromo.")
