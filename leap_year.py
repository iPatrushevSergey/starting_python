# Эта программа определяет количество дней в феврале.

# Именованные константы.
COEFF1 = 4
COEFF2 = 100
COEFF3 = 400

year = int(input('Введите год: '))

number1 = year / COEFF2  # Определить делится ли год на 100.
number2 = year / COEFF3  # Определить делится ли год на 400.
number3 = year / COEFF1  # Определить делится ли год на 4.

if (number1 == int(number1) and number2 == int(number2)
        or number1 != int(number1) and number3 == int(number3)):
    print(f'В {year} году в феврале 29 дней.')
else:
    print('Год не високосный.')
