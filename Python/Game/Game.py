import random

num = int(input('Digite um numero de 0 a 10: '))
num1 = random.randint(1,10)
if num == num1:
    print('PARABÉNS!!! VocÊ acertou o desafio!!')
else:
    print ('Você ERROU!!!')

print ('\033[4;30;42mEND GAME\033[m')
print ('\033[1;31mFIM DE JOGO\033[m')

