#CALCULA A ÁREA DE UMA PAREDE E RETORNA A QUANTIDADE DE LATAS DE TINTAS NECESSÁRIAS PARA PINTAR A PAREDE

altura = float(input('Altura da parede: '))
largura = float(input('Largura da parede: '))

area = altura * largura
lataTinta = area / 2

print('Para pintar uma parede com área de {:.2f} metros quadrados você precisará de {:.1f} litros de tintas'.format(area, lataTinta))