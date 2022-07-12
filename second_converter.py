# Эта программа преобразовывает секунды в дни, часы, минуты и секунды.

# Именованные константы.
SEC_MIN = 60  # Количество секунд в минуте.
MIN_HOUR = 60  # Количество минут в одном часе.
HOUR_DAY = 24  # Количество часов в одном дне.
SEC_HOUR = 3600  # Количество секунд в одном часе.
SEC_DAY = 86400  # Количество секунд в одном дне.

seconds = int(input('Введите количество секунд: '))

if seconds >= SEC_MIN and seconds < SEC_HOUR:
    total_minutes = seconds // SEC_MIN
    total_seconds = seconds % SEC_MIN
    print(f'В результате преобразования получилось '
          f'{total_minutes} minutes, {total_seconds} seconds.')

elif seconds >= SEC_HOUR and seconds < SEC_DAY:
    total_hours = seconds // SEC_HOUR
    total_minutes = seconds // SEC_MIN % MIN_HOUR
    total_seconds = seconds % SEC_MIN
    print(f'В результате преобразования получилось '
          f'{total_hours} hours, {total_minutes} minutes, '
          f'{total_seconds} seconds.')

elif seconds > SEC_DAY:
    total_days = seconds // SEC_DAY
    total_hours = seconds // SEC_HOUR % HOUR_DAY
    total_minutes = seconds // SEC_MIN % MIN_HOUR
    total_seconds = seconds % SEC_MIN
    print(f'В результате преобразования получилось '
          f'{total_days} days {total_hours} hours '
          f'{total_minutes} minutes {total_seconds} seconds.')
