#NOME E APELIDOS - CURSO - GRUPO- ACTIVIDADE7

print('Canta xente está invitada á festa fin de curso?')

num_persoas= int(input())

if num_persoas >= 5: #caso entre 5 e 30
    if num_persoas <= 30:
        print('Número de persoas correcto. Pódese celebrar a festa') #caso entre 5 e 30
    else:
        print('Número de persoas excesivo. Non se pode celebrar a festa') #caso maior de 30
else:
    print('Número de persoas insuficiente. Non se pode celebrar a festa') #caso menor que 5