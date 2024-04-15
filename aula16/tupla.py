#TUPLAS SÃO IMUTÁVEIS
frutas = ('Banana', 'uva', 'maçã','abacate','limão','acerola','manga')
odd_numbers = (1,3,5,7,1)
even_numbers = (2,4,6,8)
all_numbers = odd_numbers + even_numbers
lanche = ['suco','Hambúrguer','pudim']
pessoa = {'nome':'Raí vaz','peso':72.4,'idade':26}
pessoas = [
    {'nome':'Raí vaz','peso':72.4,'idade':26},
    {'nome':'Miralva vaz','peso':80.5,'idade':36},
    {'nome':'Ednalva vaz','peso':70.1,'idade':32}
]

print(type(frutas))

print(frutas)

# soma de tupla
print(f'{25*'='} soma de tuplas {25*'='}')
print(all_numbers)

#verifica quantas vezes valor aparece na tupla
print(f'{25*'='} verifica quantas vezes valor aparece na tupla {25*'='}')
print(all_numbers.count(1))

#retorna o index na tupla
print(f'{25*'='} retorna a posição na tupla {25*'='}')
print(all_numbers.index(5))


#verifica quantas vezes valor aparece na tupla a partir de uma posição
print(f'{25*'='} verifica quantas vezes valor aparece na tupla a partir de uma posição {25*'='}')
print(all_numbers.index(1,2))

#organiza em ordem alfabética
print(sorted(frutas))

#retorna o último valor da tupla
print(f'{25*'='} frutas[-1] {25*'='}')
print(frutas[-1])

#retorna o penúltimo valor da tupla
print(f'{25*'='} frutas[-2] {25*'='}')
print(frutas[-2])

#retorna do elemento 1 ao 2 ele desconsidera o último valor
print(f'{25*'='} frutas[1:3] {25*'='}')
print(frutas[1:3])

#da posição até o final
print(f'{25*'='} print(frutas[2:]) {25*'='}')
print(frutas[2:])

#da posição 0 a posição 1
print(f'{25*'='} print(frutas[:2]) {25*'='}')
print(frutas[:2])

#do penúltimo até o final
print(f'{25*'='} print(frutas[-2:]) {25*'='}')
print(frutas[-2:])

for fruta in frutas:
    print(f'E vou comer: {fruta}')
print('Comi tudo!')

print(30*'-')

for l in lanche:
    print(f'Hoje eu vou comer: {l}')
print('Agora só no outro final de semana')

print(30*'-')

for cara in pessoa:
    print(f'Minhas características: {pessoa[cara]}')
print('Esse sou eu')

print(30*'-')

for pessoa in pessoas:
    print(f'Nome: {pessoa['nome']}')
    print(f'Peso: {pessoa['peso']}')
    print(f'Idade: {pessoa['idade']}')


