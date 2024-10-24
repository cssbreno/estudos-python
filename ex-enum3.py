nome_digitado_pelo_user = input('Digite seu primeiro nome: ')

if len(nome_digitado_pelo_user) <= 4 :
    print('Seu nome é muito curto')
elif len(nome_digitado_pelo_user) == 5 or len(nome_digitado_pelo_user) == 6:
    print('Seu nome é normal')
else :
    print('Seu nome é muito grande')