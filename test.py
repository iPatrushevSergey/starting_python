SAUSAGES = 10
BUNS = 8
PACK = 1
ZERO = 0

participants = int(input('Введите количество учатсников пикника: '))
hot_dogs = int(input('Введите количество хот-догов каждому участнику: '))

total_hot_dogs = hot_dogs * participants
if total_hot_dogs >= SAUSAGES:
    sausages_pack = total_hot_dogs // SAUSAGES
    buns_pack = total_hot_dogs // BUNS
    remains_sausages = total_hot_dogs % SAUSAGES
    remains_buns = total_hot_dogs % BUNS
    print(f'Минимально необходимое количество '
          f'упаковок с сосисками: {sausages_pack}')
    print(f'Минимально необходимое количество '
          f'упаковок с булочками: {buns_pack}')
    if remains_sausages and remains_buns == 0:
        print('Сосисок и булочек не останется.')
    elif remains_sausages == 0:
        print('Сосисок не останется.')
        print(f'Количество оставшихся булочек: {remains_buns}')
    elif remains_buns == 0:
        print(f'Количество оставшихся сосисок: {remains_sausages}')
        print('Булочек не останется.')
    else:
        print(f'Количество оставшихся сосисок: {remains_sausages}')
        print(f'Количество оставшихся булочек: {remains_buns}')
elif total_hot_dogs >= BUNS:
    sausages = SAUSAGES - total_hot_dogs
    buns_pack = total_hot_dogs // BUNS
    remains_buns = total_hot_dogs % BUNS
    if remains_buns > ZERO:
        buns_pack += PACK
        remains_buns = buns_pack * BUNS - total_hot_dogs
    print('Необходима одна упаковка с сосисками.')
    print(f'Минимально необходимое количество '
          f'упаковок с булочками: {buns_pack}')
    print(f'Количество оставшихся сосисок: {sausages}')
    print(f'Количество оставшихся булочек: {remains_buns}')
else:
    sausages = SAUSAGES - total_hot_dogs
    buns = BUNS - total_hot_dogs
    print('Необходима одна упаковка с сосисками.')
    print('Необходима одна упаковка с булочками.')
    print(f'Количество оставшихся сосисок: {sausages}')
    print(f'Количество оставшихся булочек: {buns}')
