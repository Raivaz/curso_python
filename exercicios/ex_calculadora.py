n1 = int(input('Digite o primeiro número: '))
op = input('Escolha a operação digitando, - + * /: ')
n2 = int(input('Digite o segundo número: '))

def calc(operation, number1, number2):
    if operation == '-':
        result = number1 - number2
        print('A subtração entre {} e {}, é: {}'.format(number1, number2, result))
    elif operation == '+':
        result = number1 + number2
        print('A soma entre {} e {}, é: {}'.format(number1, number2, result))
    elif operation == '*':
        result = number1 * number2
        print('A multiplicação entre {} e {}, é: {}'.format(number1, number2, result))
    elif operation == '/':
        result = number1 / number2
        print('A divisão entre {} e {}, é: {}'.format(number1, number2, result))
    else:
        print('Operador inválido digite novamente')
        op = input('Escolha a operação digitando, - + * /: ')
        calc(op, n1, n2)


calc(op, n1, n2)

    