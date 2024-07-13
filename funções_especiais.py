# Funções lambda (anônimas)
# Sintaxe:
# lambda arguemntos: expressão

# quadrado = lambda x: x**2

# for i in range(1, 11):
#     print(quadrado(i))

# par = lambda x: x %2 == 0
# print(par(9))

# f_c = lambda f: (f - 32) * 5/9
# print(f_c(32))

# Função map()
# Sintaxe
# map(função, iterável)

# num = [1,2,3,4,5,6,7,8]
# dobro = list(map(lambda x: x*2, num))
# print(dobro)

# palavras = ['Python', 'é', 'uma', 'linguagem', 'de', 'programação']
# maiusculas = list(map(str.upper, palavras))
# print(maiusculas)

# Função filter()
# Sintaxe
# filter(função, sequencia)

# def numeros_pares(n):
#     return n % 2 == 0

# numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13]

# num_par = list(filter(numeros_pares, numeros))
# print(num_par)

numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13]

num_impar = list(filter(lambda x: x % 2 != 0, numeros))
print(num_impar)
