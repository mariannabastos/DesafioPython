# -*- coding: utf-8 -*-
import os
import random

nome = input('Olá! Qual é seu nome? ')
print('\nBoas vindas,',nome,'! Vamos começar o nosso jogo da forca?')

listaDePalavras = ['programador', 'codigo', 'python', 'desafio']
palavra = random.choice(listaDePalavras).upper()
tamanho = len(palavra)
codigo = ['_'] * tamanho
numeroDeErros = 0

print(f'\nA palavra secreta tem {tamanho} letras!')

while '_' in codigo and numeroDeErros < 7:
  print(f'\nQuantidade de erros: {numeroDeErros}, o limite de erros é 7!')
  for i in codigo:
    print(i, end = ' ')
  print()
  
  letraEscolhida = input('\nDigite uma letra: ').upper()
  acerto = False
  for i in range(tamanho):
    if letraEscolhida == palavra[i]:
      codigo [i] = letraEscolhida
      acerto = True

  if acerto == True:
    print(f'\nVocê acertou a letra!')
  else:
    print('\nQue pena, você errou a letra!')
    numeroDeErros = numeroDeErros + 1

if numeroDeErros == 7:
  print('\nGame over! Infelizmente você perdeu :(')
else:
  print(f'\nParabéns, {nome}, você ganhou! :D')
  
print(f'A palavra secreta é {palavra}!')