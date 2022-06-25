"""
While no python
"""

#Exemplo

aux = True
#continue dentro do while faz com que ele interrompa a sua execucao e vá para o próximo while
#break dentro do while finaliza a cadeia de loop e sai do while totalmente
while aux == True:
    nome = input('Digite seu nome: ')
    if not nome.isdigit():
        print(f'Olá {nome}')
        aux = False
    else:
        print(f'Você não digitou um nome')

x = 0

while x <= 150:
    print(x)
    x = x + 1