nome = 'Allyson'
idade = 25
altura = 1.60
e_maior = idade > 18
peso = 68
imc = peso/(altura*altura)

print('Nome:', nome)
print('Idade:', idade)
print('Altura:', altura)
print('É maior:', e_maior)


print(nome, 'tem', idade, 'de idade e seu imc é: ', imc)

#utilizando f strings

print(f'{nome} tem {idade} anos de idade e seu imc é: {imc:.2f}')

print('{} tem {} anos de idade e seu imc é: {:.2f}'.format(nome,idade,imc))

print('{0} tem {1} anos de idade e seu imc é: {2:.2f}'.format(nome,idade,imc))