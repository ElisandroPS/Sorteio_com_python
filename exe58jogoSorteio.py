print('\033[31m-=-\033[m' * 25)
import random
import time# coloca o time e
cont = 0
mnum = -1
num = -2
while mnum != num:
    mnum = int(input('Tente adivinhar um número entre 0 e 10, sorteado pelo PC: '))
    num = random.randint(0, 10)
    print("SORTEANDO...")
    cont += (num - num) + 1
    time.sleep(1)# coloca o time em segundos
    print('\033[31m-=-\033[m'  * 25)
    if mnum == num:
        print('\033[1;36mParabéns, você adivinhou o número, o {} foi o número sorteado!\033[m'.format(num)+'.')
    else:
        if mnum > num:
            print('\033[7;31mMENOS...Tente outra vez!\033[m')#professor
        elif mnum < num:
            print('\033[7;36mMAIS...Tente outra vez!\033[m')#professor
        #print('Você não teve sorte dessa vez, seu número foi {}, o número do sorteio foi {}'.format(mnum, num)+'.')
print('\033[1;36mVocê precisou de {} tentativas para acertar!\033[m'.format(cont))
