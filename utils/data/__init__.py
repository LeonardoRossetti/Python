def readCurrency(message):
    while True:
        value = str(input(message)).replace(',', '.').strip()
        if value.isalpha() or value == '':
            #  \033[0;31m    \033[m  is another way of including colors
            print(f'\033[0;31mValue: "{value}" is not a valid currency.\033[m')
        else:
            break
    return float(value)


def readInt(message):
    while True:
        try:
            value = int(input(message))
        except (ValueError, TypeError):
            print(f'\033[0;31mError: value is not a number.\033[m')
            continue
        except KeyboardInterrupt:
            print(f'\033[0;31mError:user interrupted the execution.\033[m')
            return 0
        else:
            return value
