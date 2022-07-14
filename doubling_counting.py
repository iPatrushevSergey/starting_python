COEFF_ONE = 1
COEFF_TWO = 2
KOPECKS_PER_RUBLE = 100

days = int(input('Введите количество дней, которые вы работали: '))

total_kopecks = 0

print('Заработная плата за каждый день:')
print('--------------------------------')
for i in range(days):
    pay = COEFF_TWO ** i
    total_kopecks += pay
    print(f'{i+COEFF_ONE} день\t{pay} копеек.')
total_rubles = total_kopecks / KOPECKS_PER_RUBLE
print(f'Итоговая заработная плата составила {total_rubles} рублей.')
