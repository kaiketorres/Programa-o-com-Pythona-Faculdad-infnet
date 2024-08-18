#Faça um programa que calcule o Índice de Massa Corporal (IMC) do usuário e forneça feedback com base no valor (por exemplo, abaixo do peso, peso normal, sobrepeso).


def calculoImc():
  imc = round(peso / (altura * altura),2)
  
  if imc < 16:
    print(f'Seu imc e {imc} magreza grave')
  elif imc < 16.9:
    print(f'Seu imc e {imc} magreza moderada')  
  elif imc < 18.5:
    print(f'Seu imc e {imc} magreza leve') 
  elif imc < 24.9:
    print(f'Seu imc e {imc} peso ideal') 
  elif imc < 29.9:
    print(f'Seu imc e {imc} sobrepeso') 
  elif imc < 34.9:
    print(f'Seu imc e {imc} obesidade grau I') 
  elif imc < 39.9:
    print(f'Seu imc e {imc} obesidade grau II ou severa') 
  elif imc > 40:
    print(f'Seu imc e {imc} obesidade grau III ou mórbida') 

peso = float(input('Digite seu peso: '))

altura = float(input('Digite sua altura: '))

calculoImc()