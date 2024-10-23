nome = 'Breno Soares'
altura = 1.68
peso = 65
imc = peso / (altura ** 2)

#f-string
linha_1 = f'{nome} tem {altura:.2f} de altura,'
linha_2 = f'pesa {peso:.2f} quilos e seu IMC é'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)
