"""
Condições if, elif e else
Operadores relacionais

== > >= < <= !=

"""

numero1 = int(input("Qual é o número: "))
numero2 = int(input("Qual é o numero2: "))

if numero2 >= 20 and numero2 <= 30:
    print(f'Acesso permitido!')
else:
    print(f'Acesso negado!')

if numero1 >= 10:
    print("Maior que 10")
elif numero1 > 5:
    print("Maior que 5")
else:
    print("Menor que 5")

