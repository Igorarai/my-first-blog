volume = 57
if volume < 20:
    print('Está um pouco baixo')
elif 20 <= volume < 40:
    print('Está bom para musica ambiente')
elif 40 <= volume < 60:
    print('Perfeito, posso ouvir todos os detalhes')
elif 60 <= volume < 80:
    print('Ótimo para festas!')
elif 80 <= volume < 100:
    print('Está muito alto!')
else:
    print('Meus ouvidos doem!! :( ')

#Mudar o volume caso esteja muito baixou ou muito alto
if 20 < volume < 50:
    volume = 50
    print ('Seu volume foi automaticamente alterado para 50, muito melhor assim!')