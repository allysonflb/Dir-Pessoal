#Exercício 1

numero = input("Digite um número inteiro!: ")

try:
    if int(numero)%2 == 0:
        print(f'O número digitado é par!')
    elif int(numero)%2 >= 1:
        print(f'O número digitado é impar!')
except:
    print(f'Você não digitou um número válido')


#Exercício 2

hora = input("Digite a hora: ")

if float(hora) > 0 and float(hora) < 11:
    print(f'Bom dia!!!')
elif float(hora) > 12 and float(hora) < 17:
    print(f'Boa tarde!!!')
else:
    print(f'Boa noite')

#Exercício 3

usuario = input("Digite o usuário: ")
qtd_carac = len(usuario)


if qtd_carac <= 4:
    print(f'Nome curto..')
elif qtd_carac >= 5 and qtd_carac <= 6:
    print(f'Nome normal...')
else:
    print(f'Nome grande... ')
