""""
Contagem de caracteres de strings, não funciona com tipos númericos
"""
usuario1 = "Teste"
usuario = input('Digite seu usuário: ')
qtd_caract = len(usuario+usuario1)
print(qtd_caract)


if qtd_caract < 6:
    print("Digite 6 caracteres...")
else:
    print("Cadastro feito")

print(usuario, qtd_caract,type(qtd_caract))


