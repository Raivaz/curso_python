#importa a modulo inteiro import math ou from math import sqrt, floor
import math
import random
import emoji

number = int(input('Digite um número: '))
numberRandom = random.randint(1, 10)

result = number * numberRandom
raiz = math.sqrt(number)

print(emoji.emojize('Python is :thumbs_up:'))



print('A raiz quadrada é {} e a multiplicação por {} é {}'.format(raiz, numberRandom, result))













