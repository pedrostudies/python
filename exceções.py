# Exceção é um objeto que representa um erro que ocorreu ao executar o programa.
# Blocos try ... except

# n1 = int(input('Digite um numero: '))
# n2 = int(input('Digite outro numero: '))

# try:

#     r = round(n1 / n2, 2)

# except  ZeroDivisionError:
#     print(f'Não é possivel dividir por zero')

# else:
#     print(r)

def div(k, j):
    return round(k/j, 2)

if __name__ == '__main__':
    while True:
        try:
            n1 = int(input('Digite um numero: '))
            n2 = int(input('Digite outro numero: '))
            break
        except ValueError:
            print('Ocorreu um erro, tente novamente')

    try:
        r = div(n1,n2)
    except ZeroDivisionError:
        print('Divisão por zero não é aceitavel')
    except:
        print('Erro desconhecido')
    else:
        print(r)
    finally:
        print('Fim do Cálculo')



