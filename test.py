MONTHS_PER_YEAR = 12

years = int(input('Введите количество лет: '))

all_precipitation = 0.0

for i in range(years):
    for i in range(MONTHS_PER_YEAR):
        precipitation = float(input('Введите количество осадков в месяце: '))
        all_precipitation += precipitation
months = years * MONTHS_PER_YEAR
average = all_precipitation / months

print(f'{months} месяцев, {all_precipitation} мм дождевых осадков, '
      f'{average} мм средняя толщина слоя дождевых осадков в месяц.')
