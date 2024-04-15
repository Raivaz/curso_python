# RETORNA CENTÍMETRO DE MILÍMETRO DE METROS

metro = float(input('Digite quantos metros: '))
msg = 'metros' if metro > 1 else 'metro'

print('{} {} tem {:.0f} centímetro e {:.0f} milímetros'.format(metro, msg, metro*100, metro*1000))