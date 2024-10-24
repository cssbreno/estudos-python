hora_digitada_pelo_user = input('Digite a hora: ')
hora_digitada_int = int(hora_digitada_pelo_user)

if hora_digitada_int >= 0 and hora_digitada_int <= 11 :
        print('Bom dia!')
elif hora_digitada_int > 11 and hora_digitada_int < 18 :
        print('Boa tarde')
elif hora_digitada_int >= 18 and hora_digitada_int < 24 :
        print('Boa noite')
else:
    print('Você não digitou uma hora válida!')
