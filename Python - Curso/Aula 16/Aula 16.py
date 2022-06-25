"""
Formatação de valores

:s - Texto(strings)
:d - Inteiros(int)
:f - Números de ponto flutuante (float)
:.(numero)f - quantidade de casas decimais (float)
:(caractere) > ou < ou ^ (quantidade)(tipo - s, d ou f)

> - Esquerda
< - Direita
^ - Centro
"""

num1 = 10
num2 = 3
divisao = num1 / num2
nome =  'Allyson'

print('{:.2f}'.format(divisao))

# Ou

print(f'{divisao:.2f}')

print(f'{num1:0<10}')
print(f'{num1:.10f}')
print(f'{nome:*^20}')

print(nome.lower()) #tudo minusculo
print(nome.upper()) #tudo maiusculo
print(nome.title()) #As primeiras letras maiusculas

