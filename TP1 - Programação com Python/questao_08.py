#Crie um programa que pergunte a idade do usuário e verifique se ele é maior de idade ou não.

def VerificarIdade():
  
  idade = int(input('Qual e sua idade: '))
  
  if idade < 18:
    print(f'Voce tem {idade} anos de idade voce e menor de idade')
  else :
    print(f'Voce tem {idade} anos de idadde voce e maior de idade')

VerificarIdade()