n1 = 0.0 
n2 = 0.0
media = 0.0

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

media = (n1 + n2) / 2

if (media >= 7.5):
    print('Resultado: Aprovado!')
    print('Parabéns, você foi aprovado!')

print(f'A sua média é {media}')

