# OPERADORES
# ** potência
# // divisão
# % resto da divisão

#ORDEM DE PRECEDÊNCIA 
# ()
# **
# * / // %
# + -
 
potencia = 2 ** 5

divInteira = 14 // 3

restDiv = 14 % 3

print(potencia)
print(divInteira)
print(restDiv)

print(5+3*2)
print(3*5+4**2)
print(3*(5+4)**2)

#calcular raiz quadrada
print(25**(1/2))
print(16**(1/2))

#calcular raiz cúbica
print(127**(1/3))

print('='*20)

nome = input('Qual é seu nome: ')
print('Prazer em te conhecer {:20}!'.format(nome))
print('Prazer em te conhecer {:>20}! '.format(nome))
print('Prazer em te conhecer {:<20}! '.format(nome))
print('Prazer em te conhecer {:^20}! '.format(nome))
print('Prazer em te conhecer {:=^20}! '.format(nome))

#formatando 3 número flutuante
# \n quebrar linha
# end='' não quebrar linha

print('Número \n da divisão: {:.3f}'.format(10/3), end=' ')
print('teste de concatenação')
