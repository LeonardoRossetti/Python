import utils.mesage


def increase(value, tax, _format=False):
    """
    Increase a tax into a value
    :param value: value to apply the tax
    :param tax: tax to be used
    :param _format: return a currency formatted value
    """
    result = value + (value * tax / 100)
    return result if not _format else formatCurrency(result)


def decrease(value, tax, _format=False):
    """
    Decrease a tax into a value
    :param value: value to apply the tax
    :param tax: tax to be used
    :param _format: return a currency formatted value
    """
    result = value - (value * tax / 100)
    return result if not _format else formatCurrency(result)


def half(value, _format=False):
    """
    Return a half of a value
    :param value: value to be used
    :param _format: return a currency formatted value
    """
    result = value / 2
    return result if not _format else formatCurrency(result)


def double(value, _format=False):
    """
    Return a double of a value
    :param value: value to be used
    :param _format: return a currency formatted value
    """
    result = value * 2
    return result if not _format else formatCurrency(result)


def formatCurrency(value, currency='$'):
    """
    Format value
    :param value: value to be formatted
    :param currency: currency to be used
    """
    return f'{currency}{value:.2f}'.replace('.', ',')


def resume(value=0, taxIncrease=5, taxDecrease=5):
    utils.mesage.showMessage('RESUME'.center(30), '-', 30)
    print(f'Value: {formatCurrency(value)}')
    print(f'The half is \t\t{half(value, True)}')
    print(f'Decreasing in {taxDecrease}% \t{decrease(value, taxDecrease, True)}')
    print(f'Increasing in {taxIncrease}% \t{increase(value, taxIncrease, True)}')
    print(f'The double is \t\t{double(value, True)}')
