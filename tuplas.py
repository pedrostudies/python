# halogenios = ('F', 'Cl', 'Br', 'I', 'At')
# gases_nobres = ('He', 'Ne', 'Ar', 'Xe', 'Kr', 'Rn')
# elementos = halogenios + gases_nobres

# print(elementos)

# operações não disponíveis em tuplas: .sort(), .append(), .reverse(), .pop()....

# Tuplas são imutáveis

# for elemento in elementos:
#     print(f'Elemento químico: {elemento}')

# grupo17 = list(halogenios)
# print(grupo17)

grupo1 = ['Li', 'Na', 'K', 'Rb', 'Cs', 'Fr']
alcalinos = tuple(grupo1)
print(alcalinos)

print(sorted(alcalinos))