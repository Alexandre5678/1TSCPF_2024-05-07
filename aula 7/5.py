print('Potenciação')
print('-------------')


base = int(input('entre com a base: '))
exponencial = int(input('entre com o exponencial: '))

total = 1
if base <= 1 or exponencial < 2:
    print('A base deve ser maior que 1 e o exponencial maior igual a 2')
else:
    for _ in range(exponencial):
        total = total * base
    print(f'{base} elevado ao {exponencial} é igual a {total}')
