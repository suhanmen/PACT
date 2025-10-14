def valid_date(date):
    if not date:
        return False

    try:
        month, day, year = map(int, date.split('-'))
    except ValueError:
        return False

    if not (1 <= month <= 12):
        return False

    if month in {4, 6, 9, 11}:
        if not (1 <= day <= 30):
            return False
    elif month == 2:
        leap_year = (year % 4 == 0 and year % 100 != 0) or year % 400 == 0
        if not (1 <= day <= 29 if leap_year else 1 <= day <= 28):
            return False
    else:
        if not (1 <= day <= 31):
            return False

    return True
