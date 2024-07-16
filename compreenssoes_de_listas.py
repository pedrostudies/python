# numeros = [1,4,7,9,10,12,21]

# quadrados = [num**2 for num in numeros]
# print(quadrados)

# pares = [num for num in range(1200) if num % 2 == 0]
# print(pares)

# frase = 'A lógica é apenas o princípio da sabedoria, e não o seu fim.'
# vogais = ['a', 'e', 'i', 'o', 'u', 'á', 'é', 'í', 'ó', 'ú']

# listas_vogais = [v for v in frase if v in vogais]
# print(f'A frase possui {len(listas_vogais)} vogais: ')
# print(listas_vogais)

# distributiva = [k * m for k in [2,3,5] for m in [10,20,30]]
# print(distributiva)

k = [2,3,5] 
m = [10,20,30]

for x in k:
    for y in m: 
       r = x * y
    for z in r:
        lista = [z]
       
print(lista)