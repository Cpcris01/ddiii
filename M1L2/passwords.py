from random import *

elements = '+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

try:

    num = int(input('Que tan larga quieras la contraseña? ->  '))

except ValueError:

    print('Intruduzca un numero valido, Error:', ValueError)

password = ''

for i in range(num):
    password += choice(elements)


print(password)

