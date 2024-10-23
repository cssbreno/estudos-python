seu_nome = input("Digite seu nome: ")
sua_idade = input("Digite sua idade: ")

if seu_nome and sua_idade != '':
    print(f'Seu nome é {seu_nome}')
    print(f'Seu nome invertido é {seu_nome[::-1]}')
    
    if ' ' in seu_nome:
        print(f'Seu nome contém espaços')
    else :
        print(f'Seu nome não contém espaços')
        
    print(f'Seu nome tem {len(seu_nome)} letras')
    print(f'A primeira letra do seu nome é {seu_nome[0]}')
    print(f'A última letra do seu nome é {seu_nome[-1]}')
    
else: 
    print('Desculpe, você deixou campos vazios.')
