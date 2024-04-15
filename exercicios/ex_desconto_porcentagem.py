valorProduto = float(input('Digite o valor do produto: '))
valorPorcentagem = int(input('Digite apenas o valor do desconto: '))

conDesconto = (valorProduto*valorPorcentagem)/100

print('{} com {}% de desconto ficaria {}'.format(valorProduto, valorPorcentagem, valorProduto - conDesconto))