import os
from time import sleep
print('-='*30)
print(f'\033[1m{"DIÁRIO DE CLASSE":^60}\033[m')
print('-='*30)
lista = list()
nome = list()
nota = []
print('Menu:'
      '\n[1] Para adicionar aluno;'
      '\n[2] Remover aluno;'
      '\n[3] Ver notas;'
      '\n[4] Limpar Terminal;'
      '\n[5] Sair do Programa.')
while True:
    menu = int(input('Qual sua opção? '))
    while menu not in range(1, 6):
        menu = int(input('Qual sua opção? '))
    print('-'*60)
    if menu == 1:
        nome.append(str(input('Nome: ')))
        nota.append(float(input('Nota 1: ')))
        nota.append(float(input('Nota 2: ')))
        nota.append((nota[0]+nota[1])/2)
        nome.append(nota[:])
        lista.append(nome[:])
        lista.sort()
        nome.clear()
        nota.clear()
        print('Aluno Cadastrado!')
        print('-'*60)
    if menu == 2:
        if len(lista) == 0:
            print('\033[33mNão é possível remover alunos. Não há alunos cadastrados no sistema.\033[m')
        else:
            print(f'Alunos Cadastrados:')
            for c in range(len(lista)):
                print(f'{c} - {lista[c][0]}')
            while True:
                num = int(input('Qual aluno você gostaria de remover? nº '))
                while num not in range(len(lista)):
                    print('Número não cadastrado. Tente novamente.')
                    break
                else:
                    lista.pop(num)
                    break
            print('Aluno(a) removido!')
        print('-'*60)
    if menu == 3:
        if len(lista) == 0:
            print('\033[33mNão é possível ver notas. Não há alunos cadastrados no sistema.\033[m')
        else:
            media = int(input('Qual a média para aprovação do aluno? '))
            print(f'{"No.":<5}{"NOME":<15}{"NOTA 1":<8}{"NOTA 2":<8}{"MÉDIA":<8}{"SITUAÇÃO":<7}')
            for c in range(len(lista)):
                if lista[c][1][2] >= media:
                    situ = '\033[33mAprovado\033[m'
                else:
                    situ = '\033[34mReprovado\033[m'
                print(f'{c:<5}{lista[c][0]:<15}{lista[c][1][0]:<8}{lista[c][1][1]:<8}{lista[c][1][2]:<8}{situ}')
        print('-' * 60)
    if menu == 4:
        os.system('cls' if os.name == 'nt' else 'clear')
    if menu == 5:
        break
print('Finalizando...')
sleep(1)
print('Programa "DIÁRIO DE CLASSE" Finalizado')
