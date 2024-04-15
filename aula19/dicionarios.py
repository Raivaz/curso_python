pessoa = {
    'nome': 'Raí vaz',
    'idade': 26,
    'peso': 71.2,
    'endereço':{
        'rua':'Nove de julho',
        'numero': 100
    }
}


#adiciona um elemento no dicionário
pessoa['email'] = 'email@gmail.com'


#apaga o elemento endereço
del pessoa['endereço']

#altera o valor da chave nome 
pessoa['nome'] = 'João silva'

#retorna os valores de um dicionário
print(pessoa.values())

print(100*'-')

#retorna as chaves
print(pessoa.keys())

print(100*'-')

#retorna valores e chave do dicionário
for k, v in pessoa.items():
    print(f'Na chave {k} o valor é: {v}')

print(100*'-')

#faz uma iteração com as chaves
for k in pessoa.keys():
    print(f'chaves: {k}')

print(100*'-')

#faz uma iteração com os valores
for v in pessoa.values():
    print(f'valores: {v}')

print(100*'-')

carros = [
    {'modelo':'Strada', 'marca':'Fiat','categoria':'caminhonete'},
    {'modelo':'Focus', 'marca':'Ford','categoria':'hat'},
    {'modelo':'I30', 'marca':'Hyundai','categoria':'hat'},
    {'modelo':'Civic', 'marca':'Honda','categoria':'sedan'}
]

#retorna o modelo do elemento da posição 1
print(carros[0]['modelo'])

carros.append(
    {
        'modelo':'Toro',
        'marca':'Fiat',
        'categoria':'caminhonete'
    }
)

print(100*'-')

print(carros)

print(100*'-')

print(carros[4])

brasil = []
estado = {}

#salva uma cópia da lista no dicionário
for e in range(0, 2):
    estado['estado'] = input('Digite o nome do estado: ')
    estado['uf'] = input('Digite a sigla: ')
    brasil.append(estado.copy())
print(brasil)
print(estado)

