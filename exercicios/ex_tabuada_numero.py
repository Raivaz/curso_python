# FAZ A CALCULADORA DE UM NÚMERO

numeroCalc = int(input('Digite um número para calcular: '))

contador = 1
while contador <= 10:
    ts = ' =' if contador < 10 else '='
    print('{} X {} {} {}'.format(numeroCalc, contador, ts, numeroCalc * contador))
    contador+=1