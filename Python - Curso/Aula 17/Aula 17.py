"""
Manipulando strings
* String indices
* Fatiamento de strings [inicio:fim:passo]
* Funções built-in len, abs, type, print etc

link documentação oficial python
"""

texto = 'Python s2'
nova_string = texto[0:6] #Fatiamento de string
print(texto[2])
print(nova_string)
print(texto[0::3]) #Passo

#Primeiro for

for letra in texto:
    print(letra)