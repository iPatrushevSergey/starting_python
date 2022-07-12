# Эта программа селектирует рестораны.

vegan = input('Будет ли на ужине веганец? ')
vegetarian = input('Будет ли на ужине вегетарианец? ')
gluten_free = input('Будет ли на ужине приверженец безглютеновой диеты? ')

if vegan == 'Да' or vegan == 'да':
    vegan = True
else:
    vegan = False
if vegetarian == 'Да' or vegetarian == 'да':
    vegetarian = True
else:
    vegetarian = False
if gluten_free == 'Да' or gluten_free == 'да':
    gluten_free = True
else:
    gluten_free = False

if not vegan and not vegetarian and not gluten_free:
    print('Изысканные гамбургеры от Джо')
    print('Центральная пиццерия')
    print('Кафе за углом')
    print('Кухня шеф-повара')
    print('Блюда от итальянской мамы.')
elif not vegan and vegetarian and gluten_free:
    print('Центральная пиццерия')
    print('Кафе за углом')
    print('Кухня шеф-повара')
elif vegan and vegetarian and gluten_free:
    print('Кафе за углом')
    print('Кухня шеф-повара')
elif not vegan and vegetarian and not gluten_free:
    print('Блюда от итальянской мамы.')
    print('Кафе за углом')
    print('Кухня шеф-повара')
    print('Центральная пиццерия')
