numero_digitado_pelo_user = input('Digite um número inteiro: ')
numero_digitado_int = int(numero_digitado_pelo_user)

try:
    if numero_digitado_int % 2 == 0 :
        print('Você digitou um número par')
    else :
        print('Você digitou um número impar')
except :
    print('Você não digitou um número inteiro!')
