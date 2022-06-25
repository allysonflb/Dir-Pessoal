while True:
    print()
    num_1 = input(f'Digite o primeiro numero: ')
    num_2 = input(f'Digite o segundo numero: ')
    operador = input(f'Digite o operador: ')
    sair = input(f'Digite [s]im para sair ou [n] para não sair')

    if sair == 's':
        break

    if not num_1.isnumeric() or  not num_2.isnumeric():
        print(f'Voce precisa digitar um numero')

    num_1 = float(num_1)
    num_2 = float(num_2)

    if operador == '+':
        print(num_1+num_2)
    elif operador == '-':
        print(num_1-num_2)
    elif operador == '*':
        print(num_1*num_2)
    elif operador == '/':
        print(num_1/num_2)