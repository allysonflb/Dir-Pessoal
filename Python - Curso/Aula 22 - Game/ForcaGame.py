#Jogo de adivinhar a palavra secreta.

palavra = 'Python'
HD = []
chances = 10

while True:
    if chances == 0:
        print(f'\nGame Over :(')
        break
    letra = input('\nDigite uma letra: ')
    if len(letra) > 1:
        print('\nVoce digitou mais de 1 letra..')
        continue
    HD.append(letra)
    if letra in palavra:
        print(f'\nVoce acertou uma letra "{letra}", ela existe na palavra.')
    elif letra not in palavra:
        print(f'\nVocê errou, a letra "{letra}" não existe na palavra. Tente novamente!')
        chances -= 1
        print(f'\nVocê ainda tem {chances} chances de acertar!')
        if chances == 0:
            continue
        HD.pop()
    sec_temp = ''
    for letra_sec in palavra:
        if letra_sec in HD:
            sec_temp += letra_sec
        else:
            sec_temp += '*'
    if sec_temp[0] != palavra[0]:
        print(f'\nDica a primeira letra é maiuscula!')
    if sec_temp == palavra:
        print(f'\nParabéns você concluiu o jogo, a palavra secreta era: {palavra}')
        break
    else:
        print(f'\nA palavra secreta está assim: "{sec_temp}"')

