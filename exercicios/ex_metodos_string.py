valor = input("Digite algo: ")

print('-'*20)
print('O tipo primitivo é? ', type(valor))
print('-'*20)
print('Só tem espaço? ', valor.isspace())
print('-'*20)
print('É um número? ', valor.isnumeric())
print('-'*20)
print('É alfanumérico? ', valor.isalnum())
print('-'*20)
print('Está em maiúscula? ', valor.isupper())
print('-'*20)
print('Está em minúscula? ', valor.islower())
print('-'*20)
print('Está capitalizada? ', valor.istitle())
print('-'*20)
print('É alfabético? ', valor.isalpha())
