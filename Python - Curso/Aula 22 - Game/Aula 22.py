"""
Listas (array) em python
fatiaamento
append, insert, pop, del, clear, extend, +
min, max
range
"""

l5 = list(range(1,10))
print(l5)

for valor in l5:
    if valor == 5:
        print(l5[valor])

lista = ['A', 'B', 'C', 'D', 'E']
lista[4] = 'Teste'

print(lista[0:3])


l1 = [1,2,3]
l2 = [4,5,6]
l3 = l1+l2 #concatenar
l1.extend(l2) #extende a l1 com os valores da l2
l1.extend('a') #extende a l1 com um a no final
l2.append(20) #insere um novo valor no final da lista
l2.insert(0, 30) #insere um novo valor no indice designado

print(l1)
print(l2)

l2.pop(0) #deleta o valor inserido no indice designado

print(l2)

print(max(l2))
print(min(l2))

