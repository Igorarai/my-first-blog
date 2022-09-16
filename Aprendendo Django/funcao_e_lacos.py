def hi(name):
    print('Olá ' + name + '!')

girls = []

name = girls.append('Digite um nome, ou pressione ENTER para continuar: ')

while name : 
    print('Digite um nome, ou pressione ENTER para continuar: ')
    girls.insert(name)

for name in girls:
        hi(name)