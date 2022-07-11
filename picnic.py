# Эта программа считает необходимое количество упаковок с сосисками
# и булочками для пикника, а также их остаток.

# Именованные константы.
SAUSAGES = 10  # Количество сосисок в одной упаковке.
BUNS = 8  # Количество булочек в одной упаковке.
PACK = 1  # Одна упаковка.
ZERO = 0  # Ноль.

participants = int(input('Введите количество участников пикника: '))
hot_dogs = int(input('Введите количество хот-догов каждому участнику: '))

# Вычислить общее количество хот-догов.
total_hot_dogs = hot_dogs * participants
# Если хот-догов больше или равно, чем сосисок в 1 упаковке.
if total_hot_dogs >= SAUSAGES:
    sausages_pack = total_hot_dogs // SAUSAGES
    remains_sausages = total_hot_dogs - sausages_pack * SAUSAGES
    if remains_sausages != ZERO:
        sausages_pack += PACK
        remains_sausages = sausages_pack * SAUSAGES - total_hot_dogs
    buns_pack = total_hot_dogs // BUNS
    remains_buns = total_hot_dogs - buns_pack * BUNS
    if remains_buns != ZERO:
        buns_pack += PACK
        remains_buns = buns_pack * BUNS - total_hot_dogs
    print(f'Минимально необходимое количество '
          f'упаковок с сосисками: {sausages_pack}')
    print(f'Минимально необходимое количество '
          f'упаковок с булочками: {buns_pack}')
    if remains_sausages == ZERO and remains_buns == ZERO:
        print('Сосисок и булочек не останется.')
    elif remains_sausages == ZERO:
        print('Сосисок не останется.')
        print(f'Количество оставшихся булочек: {remains_buns}')
    elif remains_buns == ZERO:
        print(f'Количество оставшихся сосисок: {remains_sausages}')
        print('Булочек не останется.')
    else:
        print(f'Количество оставшихся сосисок: {remains_sausages}')
        print(f'Количество оставшихся булочек: {remains_buns}')
# Если хот-догов больше или равно, чем булочек в 1 упаковке.
elif total_hot_dogs >= BUNS:
    remains_sausages = SAUSAGES - total_hot_dogs
    buns_pack = total_hot_dogs // BUNS
    remains_buns = total_hot_dogs - buns_pack * BUNS
    if remains_buns != ZERO:
        buns_pack += PACK
        remains_buns = buns_pack * BUNS - total_hot_dogs
    print('Необходима одна упаковка сосисок.')
    print(f'Минимально необходимое количество '
          f'упаковок с булочками: {buns_pack}')
    print(f'Количество оставшихся сосисок: {remains_sausages}')
    if remains_buns == ZERO:
        print('Булочек не останется.')
    else:
        print(f'Количество оставшихся булочек: {remains_buns}')
else:  # Если хот-догов меньше, чем булочек в 1 упаковке.
    remains_sausages = SAUSAGES - total_hot_dogs
    remains_buns = BUNS - total_hot_dogs
    print('Необходима одна упаковка с сосисками.')
    print('Необходима одна упаковка с булочками.')
    print(f'Количество оставшихся сосисок: {remains_sausages}')
    print(f'Количество оставшихся булочек: {remains_buns}')
