#Escreva um programa onde o usuário deve adivinhar um número secreto. O programa deve dizer se o palpite está correto, muito alto ou muito baixo.

import random

numAle = random.randint(1, 100)

def JogoPalpite():
  
  palpite = int(input('Jogo do Palpite \n \nDigite um palpite de numero: '))

  if palpite < numAle:
    print('muito baixo')
    JogoPalpite()
  elif palpite > numAle:
    print('muito alto')
    JogoPalpite()
  else:
    print('vc acertou o numero')


JogoPalpite()