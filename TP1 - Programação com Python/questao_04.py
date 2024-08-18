#Desenvolva um programa que peça ao usuário para escolher uma operação (adição, subtração, multiplicação, divisão) e dois números, e então execute a operação escolhida com os números.

def caluladora():
    if operacao == 1:
        print(f'A soma entre {n1} e {n2} e igual a {n1 + n2}')
    elif operacao == 2:
        print(f'A subtração entre {n1} e {n2} e igual a {n1 - n2}')
    elif operacao == 3:
        print(f'A multiplicação entre {n1} e {n2} e igual a {n1 * n2}')
    elif operacao == 4:
        print(f'A divisão entre {n1} e {n2} e igual a {n1 / n2}')
 

operacao = int(input(f'Escolha uma Operacao para utilizar: \n  \nAdição = 1\nSubtração = 2 \nMultiplicação = 3 \nDivisão = 4 \n \nDigite:'))

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))

caluladora()


