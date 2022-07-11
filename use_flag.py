# Программа расчитывает стоимость с учётом скидок.
PACK = 99  # Стоимость 1 пака программного обеспечения.

packs = int(input('Введите количество приобретенных пакетов: '))
price = packs * PACK
if packs < 10:
    discount = False  # Флаг.
elif packs >= 10 and packs <= 19:
    discount = 0.10
elif packs >= 20 and packs <= 49:
    discount = 0.20
elif packs >= 50 and packs <= 99:
    discount = 0.30
elif packs >= 100:
    discount = 0.40
if discount:
    total_price = price - price * discount
    print(f'Total price {total_price}')
else:
    print(f'Total price {price}')
