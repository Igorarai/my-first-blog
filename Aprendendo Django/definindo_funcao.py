print('Digite seu nome:')
name = input()
def hi(name):
    if name == 'Ola':
        print('Olá Ola!')
    elif name == 'Sonja':
        print('Olá Sonja!')
    #Caso não seja nenhum dos nomes conhecidos, chamar de estranho;
    else:
        print('Olá Estranho!')

hi(name)