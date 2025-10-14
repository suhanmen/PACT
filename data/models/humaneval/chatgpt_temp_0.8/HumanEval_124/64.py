def valid_date(date):
    if not date:
        return False

    try:
        month, day, year = map(int, date.split('-'))
    except ValueError:
        return False

    if month < 1 or month > 12:
        return False

    if month in [2]:
        if day < 1 or day > 29:
            return False
    elif month in [4, 6, 9, 11]:
        if day < 1 or day > 30:
            return False
    else:
        if day < 1 or day > 31:
            return False

    if year < 1:
        return False

    return True
