"""
interando strings com while
"""

frase = 'o rato roeu a roupa do rei de roma'
t_frase = len(frase)
count = 0
nova_string = ''

while count < t_frase:
    nova_string += frase[count]
    print(nova_string)
    count += 1