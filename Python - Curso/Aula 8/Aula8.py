"""
Input do usuário
"""

nome = input("Qual é o seu nome? ")
idade = input("Qual é a sua idade? ")
#print(f'O usuário digitou {nome} e o tipo da variável é: 'f'{type(nome)}')
#print(f'O usuário digitou {idade} e o tipo da variável é: 'f'{type(nome)}')
ano_nascimento = 2022 - int(idade)

print(f'\n{nome} tem {idade} anos. 'f'Nasceu em: {ano_nascimento}')

""""
Entrada de dados - calculadora
"""

numero_1 = input('\nDigite um número: ')
numero_2 = input('Digite outro número: ')
soma = float(numero_1)+float(numero_2);
print(f'\na soma é: {soma}')