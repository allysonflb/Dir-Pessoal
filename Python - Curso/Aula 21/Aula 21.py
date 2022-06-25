"""
For no python
Iterando strings com for
função range (start=0, stop, step=1)
"""

texto = 'Python'
nova_string = ''

for letra in texto:
    print(letra)

print(f'#################')

for letra in texto:
    if letra == 't':
        nova_string = nova_string + letra.upper()
    elif letra == 'h':
        nova_string += letra.upper()
    else:
        nova_string += letra

print(nova_string)

for numero in range(1, 11, 1):
    print(numero)

print(f'#################')

for n in range(100):
    if n % 2 == 0:
        print(n)


#****************************
# continue e break
#continue pula para o próximo laço
#break quebra o laço