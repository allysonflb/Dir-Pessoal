num1 = input("Digite um número: ")
num2 = input("Digite outro número: ")

if num1.isnumeric():
    print(f'Numero 1 foi digitado corretamente!')
else:
    print(f'Numero 1 foi digitado errado!')

if num2.isnumeric():
    print(f'Numero 2 foi digitado corretamente!')
else:
    print(f'Numero 2 foi digitado errado!')


#try and except