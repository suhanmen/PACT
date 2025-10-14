def valid_date(date):
    if len(date) != 10:
        return False
    try:
        month, day, year = map(int, date.split('-'))
    except ValueError:
        return False
    if not (1 <= month <= 12):
        return False
    if month in [4, 6, 9, 11] and not (1 <= day <= 30):
        return False
    if month == 2:
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            if not (1 <= day <= 29):
                return False
        else:
            if not (1 <= day <= 28):
                return False
    if month in [1, 3, 5, 7, 8, 10, 12] and not (1 <= day <= 31):
        return False
    return True
