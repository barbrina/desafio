galera = list()
pessoa = list()
maior = menor = 0
print('--'*30)
print(f'{"TABELA DE PESO":^55}')
print('--'*30)
while True:
    pessoa.append(str(input('Nome: ')))
    pessoa.append(float(input('Peso: ')))
    galera.append(pessoa[:])
    pessoa.clear()
    cont = str(input('Quer continuar [S/N]? ')).upper()
    while cont not in 'SN':
        cont = str(input('Quer continuar [S/N]? ')).upper()
    if cont == 'N':
        break
print(f'Ao todo, você cadastrou {len(galera)} pessoas.')
print('-='*20)
print(f'{"NOME":<20}{"PESO":<10}')
print('--'*20)
for p in range(len(galera)):
    print(f'{galera[p][0]:<20}{galera[p][1]:<10}')
    if p == 0:
        maior = menor = galera[p][1]
    else:
        if galera[p][1] > maior:
            maior = galera[p][1]
        elif galera[p][1] < menor:
            menor = galera[p][1]
print('-='*20)
print(f'O maior peso foi de {maior}Kg. Peso de ', end='')
for p in galera:
    if p[1] == maior:
        print(p[0], end=' ')
print(f'\nO menor peso foi de {menor}Kg. Peso de ', end='')
for p in galera:
    if p[1] == menor:
        print(p[0], end=' ')
