# Эта программа считает сложный процент.
HUNDRED_PERCENT = 100
COEFF = 1

initial_amount = float(input(
    'Укажите сумму, внесённую на сберегательный счёт '))
annual_percentage = float(input('Введите годовую процентную ставку '))
count_accruals = int(input('Введите количество начислений процентов в год '))
count_year = float(input('Укажите количество лет вклада '))
annual_percentage = annual_percentage / HUNDRED_PERCENT
total_amount = initial_amount * (
    COEFF + annual_percentage / count_accruals) ** (
        count_accruals * count_year
    )
print(f'Итоговая сумма денежных средств на счёте на конец периода: '
      f'{total_amount:.2f}')
