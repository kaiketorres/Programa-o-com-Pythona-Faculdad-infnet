#Desenvolva um programa que aplique descontos progressivos com base no valor da compra: desconto de 10% para compras acima de R$100, 15% para compras acima de R$200, seguindo a projeção até R$500, para valores maiores do que esse, o desconto é fixado em 25%.

def calcular_desconto(valor_compra):
    if valor_compra > 500:
        desconto = 0.25
    elif valor_compra > 300:
        desconto = 0.20
    elif valor_compra > 200:
        desconto = 0.15
    elif valor_compra > 100:
        desconto = 0.10
    else:
        desconto = 0.00

    valor_descontado = valor_compra * (1 - desconto)
    return valor_descontado, desconto

valor_compra = float(input("Digite o valor da compra: R$"))

valor_final, desconto = calcular_desconto(valor_compra)

print(f"Valor original: R${valor_compra:.2f}")
print(f"Desconto aplicado: {desconto * 100:.0f}%")
print(f"Valor com desconto: R${valor_final:.2f}")
1