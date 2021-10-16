import random

# Набор доступных символов
array_symbols = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'A', 'B', 'C', '!', '@']

# Количество символов в пароле.
CONST_COUNT_SYMBOLS = 4

custom_count_symbols = int(input('Введите количество символов в пароле:'))
if custom_count_symbols > 0:
    COUNT_SYMBOLS = custom_count_symbols
else:
    count_symbols = CONST_COUNT_SYMBOLS

count_variant = len(array_symbols) ** COUNT_SYMBOLS


# Функция случайных символов.
def random_symbols():
    return array_symbols[
        random.randint(0, len(array_symbols) - 1)
    ]


print(f'Количество доступных символов: {len(array_symbols)}')
print(f'Количество доступных символов: {count_variant}')

# Массив символов.
password_array = [i for i in range(0, COUNT_SYMBOLS)]

print(f'Количество доступных символов: {len(array_symbols)}')
print(f'Количество доступных символов: {count_variant}')

password = ''

for i in password_array:
    password = password + f'{random_symbols()}'

    printf(f'Сгенерированный пароль: {password}')

with open('password.txt', 'a') as password_string:
    password_string.write('{}\n'.format(f'{password}'))
