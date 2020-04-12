import os
from time import sleep
nome = list()
usuario = list()
senha = list()
c = 3
achou = salvo = ''
while True:
    print('-=' * 30)
    print(f'{"SISTEMA DE LOGIN":^55}')
    print('-=' * 30)
    primeira = str(input('Primeira vez? [S/N] ')).upper()
    while primeira == 'S':
        print('~~' * 30)
        print(f'{"REGISTRO":^55}')
        print('~~' * 30)
        nome.append(str(input('Nome Completo: ')))
        name = str(input('Nome de Usuário: ')).lower().strip()
        while len(name) <= 4:
            print('Seu nome de usuário deve ter mais de 4 caracteres.')
            name = str(input('Nome de Usuário: ')).lower().strip()
        if len(name) > 4:
            nome.append(name)
        sen = (str(input('Senha: '))).strip()
        while len(sen) < 7:
            print('Sua senha deve ter mais de 7 caracteres.')
            sen = (str(input('Senha: '))).strip()
        if len(sen) >= 7:
            senha.append(sen)
            nome.append(senha[:])
        if len(usuario) > 0:
            for x in range(len(usuario)):
                if nome[1] == usuario[x][1]:
                    print('Usuário já cadastrado. Tente Novamente.')
        if len(usuario) >= 0:
            usuario.append(nome[:])
            nome.clear()
            senha.clear()
            print('Cadastrando usuário...')
            for c in range(0, 3):
                print('.', end='')
                sleep(1)
            print('Pronto! Você será redirecionado a página de login.')
            sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')
        break
    while primeira == 'N':
        if len(usuario) <= 0:
            print('Não há usuário cadastrados!')
        else:
            print('~~' * 30)
            print(f'{"LOGIN":^55}')
            print('~~' * 30)
            login = str(input('Nome de usuário:')).strip()
            password = str(input('Senha: ')).strip()
            for x in range(len(usuario)):
                if login != usuario[x][1] or password != usuario[x][2][0]:
                    achou = 'N'
                elif login == usuario[x][1] and password == usuario[x][2][0]:
                    achou = 'S'
                    salvo = usuario[x][0]
            if achou == 'N' and achou != 'S':
                print('!' * 10)
                print('Usuário ou senha incorreto!')
                print(f'{c} Tentativas restantes.')
                c -= 1
                if c <= 0:
                    print('Acesso Negado')
            if achou == 'S':
                print('Acesso Concedido!')
                sleep(1)
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f'Bem Vindo {salvo}!')
                sleep(30)
                print('Você saiu do sistema por inatividade.')