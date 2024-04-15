list = ['Hambúrguer',10,10.2,True]
numbers = [1,3,4,5,6]

print(type(list))

print(numbers)

#adiciona elemento no final
numbers.append(6)

print(numbers)

#na posição 1 adiciona o 2
numbers.insert(1, 2)

print(numbers)

#remover item pela o índice, sem argumento elimina o último item
numbers.pop(1)
print(numbers)

#remover item pela a chave
# numbers.remove('nome_chave')

#remover item pela o valor
numbers.remove(4)
print(numbers)

#verifica se existe o valor na lista
if 2 in numbers:
    print('existe 2 na lista')
else:
    print('não existe 2 na lista')

#criar lista com o método list()
disordered_numbers = [8,2,4,1,3,5,7,6]
print(disordered_numbers)
print(disordered_numbers.__len__())

#retorna uma nova lista ordenada
ordered_numbers = sorted(disordered_numbers)
print(ordered_numbers)

#ordena modificando a lista original
disordered_numbers.sort()
print(disordered_numbers)


#iterando com for com valor e chave
for c, v in enumerate(numbers):
    print(f'Na posição {c} o valor é: {v}')
print('Terminei a iteração')


#dessa forma ao alterar a lista B que recebe a as duas serão alteradas
a = [10,20,30]
b = a
b[0] = 90
print(a)
print(b)

#dessa forma as listas ficam independentes
c = [121,149,178]
d = c[:]
d[0] = 543
print(c)
print(d)

