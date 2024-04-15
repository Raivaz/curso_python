#CALCULA SALARIO COM MAIS 15%
salario = float(input('Digite seu salário: '))

quinzePorCento = (salario*15)/100
salarioComAumento = salario + quinzePorCento

print('O seu salário de {} com 15% de aumento que representa {:.2f} ficaria em {:.2f}'.format(salario, quinzePorCento, salarioComAumento))