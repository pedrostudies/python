# def validar_email():
#     email = input("Digite seu email: ")
#     arroba = email.find('@')
#     usuario = email[0:arroba]
#     dominio = email[arroba+1:]
#     print(usuario.title())
#     print(dominio.title())

# validar_email()

# Função com argumentos

# def soma(a, b):
#     print(a+b)

# soma(12,7)

# def mult(x, y):
#     return x*y

# a = 12
# b = 10
# c = mult(a, b)
# print(f'O produto de {a} x {b} é {c}')

# def div(k, j):
#     if j != 0:
#         return k / j
#     else:
#         return 'Impossivel dividir por zero'

# if __name__ == '__main__':
#     a = int(input('Digite um numero:'))
#     b = int(input('Digite outro numero:'))
    
#     r = div(a, b)
#     print(f'{a} divido por {b} é {r}')

def quadrado(val):
    quadrados = []
    for x in val:
        quadrados.append(x ** 2)
    return quadrados

if __name__ == '__main__':
    valores = [2,4,5,6,7,8]
    resultados = quadrado(valores)
    for g in resultados:
        print(g)