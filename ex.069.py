cidade = 0
chomens = 0
mulheressub20 = 0
while True:
    print('-'*40)
    print('CADASTRE UMA PESSOA')
    print('-' * 40)
    idade = int(input('Idade: '))
    if idade > 18:
        cidade = cidade + 1
    sexo = str(input('Sexo: [M/F] ')).upper().strip()
    if sexo in 'Mm':
        chomens = chomens + 1
    elif idade < 20 and sexo in 'Ff':
        mulheressub20 = mulheressub20 + 1
    print('-'*40)
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        print('-'*40)
        print(f'Total de pessoas com mais de 18 anos: {cidade}')
        print(f'Ao todo temos {chomens} homens cadastrados')
        print(f'E temos {mulheressub20} mulheres com menos de 20 anos')
        print('-' * 40)
    break