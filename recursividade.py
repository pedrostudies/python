# Recursividade

# Fórmula geral para o fatorial
# fatorial(num) = 1, se num = 0 ou se num = 1 'Caso-Base'
# fatorial(num) = num * fatorial(num -1), para num > 1 'Caso Recursivo'
# 4! = 4 * fatorial(3) = 4 * 3 * fatorial(2) = 4 * 3 * 2 * fatorial(1)
# 4! = 4 * 3 * 2 * 1 = 24

def fatorial(numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        return numero * fatorial(numero - 1)

if __name__ == '__main__':
    while True:
        try:
            x = int(input('Digite o número que queira descobrir o fatorial: '))
            break
        except ValueError:
            print('Digite um número válido')

    try:
        res = fatorial(x)
    except RecursionError:
        print(f'O resultado do número fornecido é muito extenso ou negativo')
    else:
        print(f'o fatorial de {x} é {res}')
    