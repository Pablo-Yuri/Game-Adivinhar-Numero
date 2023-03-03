from random import randint
print('\n',
    '\033[31m= = '*15,'\n',
      '\033[1;36m  Pensei em um número de 1 a 5 tente adivinhar qual foi!\n',
    '\033[31m= = '*15,'\n',
      '')
num = int(input('\033[1;33mQual número eu escolhi? '))
sorteado = randint(1,5)
if num == sorteado:
    print('\033[1;34m PARABÉNS VOCÊ ACERTOU!!\n',
          'O NÚMERO PENSADO FOI O {}'.format(sorteado))
elif num < sorteado:
    print('\033[1;32mÉ um número maior!: ')
    a = int(input('\033[1;35mÉ o número?: '))
    if a == sorteado:
        print('\033[1;34mPARABÉNS VOCÊ ACERTOU!!\n'
              'O NÚMERO PENSADO FOI O {}!'.format(sorteado))
    else:
        espaco = '\033[1;36m*'
        print('\n',
              '\033[1;36m*' * 42, '\n',
              '* \033[1;31mINFELISMENTE VOCÊ ERROU!!', '{:>21}'.format(espaco), '\n',
              '\033[1;36m* \033[1;31mO NÚMERO PENSADO ERA O {}!'.format(sorteado), '{:>21}'.format(espaco), '\n',
              '\033[1;36m* \033[1;31mREENICIE O PROGRAMA E TENTE NOVAMENTE!\033[1;36m *\n',
              '\033[1;36m*' * 42)
elif num > sorteado:
    print('\033[1;32mÉ um número menor!: ')
    a = int(input('\033[1;35mÉ o número?: '))
    if a == sorteado:
        print('\033[1;34mPARABÉNS VOCÊ ACERTOU!!\n'
              'O NÚMERO PENSADO FOI O {}'.format(sorteado))
    else:
        espaco = '\033[1;36m*'
        print('\n',
              '\033[1;36m*'*42,'\n',
              '* \033[1;31mINFELISMENTE VOCÊ ERROU!!','{:>21}'.format(espaco),'\n',
              '\033[1;36m* \033[1;31mO NÚMERO PENSADO ERA O {}!'.format(sorteado),'{:>21}'.format(espaco),'\n',
              '\033[1;36m* \033[1;31mREENICIE O PROGRAMA E TENTE NOVAMENTE!\033[1;36m *\n',
              '\033[1;36m*'*42)