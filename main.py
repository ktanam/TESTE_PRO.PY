from random import randint
from time import sleep
print('-=-'*30)
computador = randint(0, 10)
print('-='*50)
print('VOU PENSAR EM UM NÚMERO ENTRE 0 E 10. TENTE ADIVINHAR...')
jogador = int(input('EM QUE NÚMERO EU PENSEI?..'))
print('PROCESSANDO...')
sleep(3)
if jogador==computador:
    print('PAREBÉNS!! Vc deve ser o jogador número um!!')
else:
    print('QUE PENA!! Pensei no {} e não no {}'.format(computador,jogador))
print('-=-'*30)
# UM PEQUENO JOGO DE ADVINHAÇÃO