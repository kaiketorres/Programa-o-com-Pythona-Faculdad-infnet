#Crie um programa que classifique as palavras inseridas pelo usuário como curtas (menos de 5 letras) ou longas (5 letras ou mais).

entrada = input("Digite algumas palavras separadas por espaço: ")

palavras = entrada.split()

for palavra in palavras:
    if len(palavra) < 5:
        print(f"'{palavra}' é uma palavra curta.")
    else:
        print(f"'{palavra}' é uma palavra longa.")
