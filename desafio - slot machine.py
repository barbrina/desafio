from random import randint
from time import sleep
print('-$'*40)
print(f'{"$LOT MACHINE":^70}')
print('-$'*40)
print('Digite o valor da sua aposta, menu para ver as regras ou fim para sair.'
      '\nSe o crédito de R$1000 reais acabar, o jogo termina.')
escolha = list()
dinheiro = cont = mult = jogou = 0
credito = 1000
while True:
    opcao = input('Qual sua opção? ').lower()
    if opcao.isdigit():
        num = float(opcao)
        print('Grau de dificuldade:')
        dificuldade = str(input('Digite F, M ou D: ')).upper()
        jogou += 1
        print(f'Sua aposta é de R${num}')
        print('-$'*40)
        if dificuldade == 'F':
            for c in range(0, 3):
                random = randint(1, 3)
                escolha.append(random)
                print(f'[{escolha[c]:^10}]', end=' ')
                sleep(1)
            if escolha[0] == escolha[1] == escolha[2]:
                print('\nVocê Ganhou!')
                mult = num*0.03
                print(F'$$$$$ VOCÊ GANHOU MAIS R${mult:.2f} REAIS $$$$$')
                cont += 1
                credito += num
            else:
                dinheiro += num
                credito -= num
                print('\nVocê perdeu!')
                print(f'Você tem {credito:.2f} reais de crédito.')
            if credito <= 0:
                cont -= 1
                break
            escolha.clear()
        if dificuldade == 'M':
            for c in range(0, 3):
                random = randint(1, 5)
                escolha.append(random)
                print(f'[{escolha[c]:^10}]', end=' ')
                sleep(1)
            if escolha[0] == escolha[1] == escolha[2]:
                print('\nVocê Ganhou!')
                mult = (num*0.2)
                print(F'$$$$$ VOCÊ GANHOU MAIS R${mult:.2f} REAIS $$$$$')
                cont += 1
                credito += num
            else:
                dinheiro += num
                credito -= num
                print('\nVocê perdeu!')
                print(f'Você tem {credito:.2f} reais de crédito.')
            if credito <= 0:
                cont -= 1
                break
            escolha.clear()
        if dificuldade == 'D':
            for c in range(0, 3):
                random = randint(1, 7)
                escolha.append(random)
                print(f'[{escolha[c]:^10}]', end=' ')
                sleep(1)
            if escolha[0] == escolha[1] == escolha[2]:
                print('\nVocê Ganhou!')
                mult = num*0.4
                print(F'$$$$$ VOCÊ GANHOU MAIS R${mult:.2f} REAIS $$$$$')
                cont += 1
                credito += num
            else:
                dinheiro += num
                credito -= num
                print('\nVocê perdeu!')
                print(f'Você tem {credito:.2f} reais de crédito.')
            if credito <= 0:
                cont -= 1
                break
            escolha.clear()
    else:
        while opcao not in 'menu' and opcao not in 'fim':
            break
        if opcao == 'menu':
            print('No $LOT MACHINE não há configurações, não há regras complicadas e não há controlos avançados.'
                  '\nTudo o que é necessário do jogador é digitar o valor de sua aposta.'
                  '\nDepois de digitar a aposta, começa a rotação. Se depois de parar, três números idênticos forem'
                  '\ngerados, você ganha e multiplica o valor da sua aposta pela % estabelecida no grau de dificuldade.'
                  '\nNo caso oposto, não ganha nada. Após a rotação terminar, "Qual sua opção?" aparecerá e você'
                  '\npoderá recomeçar o jogo com uma nova aposta ou digitar "Fim" para terminar o jogo.'
                  '\nO grau de dificuldade é F - fácil (3%), M - médio (20%) ou D - difícil (40%).  ')
            print('~~'*40)
        if opcao == 'fim':
            break
print(f'FIM DO JOGO!')
if jogou > 0:
    if cont < 0:
        print(f'Você está devendo {credito:.2f} reais.')
    if cont == 0:
        print(f'VOCÊ PERDEU R${dinheiro:.2f} REAIS.')
    if cont > 0:
        print(f'VOCÊ GANHOU {mult:.2f} REAIS.')
