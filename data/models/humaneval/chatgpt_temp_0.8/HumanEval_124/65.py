def valid_date(date):
    if len(date) != 10:
        return False
    if not date[0:2].isdigit() or not date[3:5].isdigit() or not date[6:].isdigit():
        return False
    month = int(date[0:2])
    day = int(date[3:5])
    year = int(date[6:])
    if month < 1 or month > 12:
        return False
    if month in [1, 3, 5, 7, 8, 10, 12]:
        if day < 1 or day > 31:
            return False
    elif month in [4, 6, 9, 11]:
        if day < 1 or day > 30:
            return False
    elif month == 2:
        if year % 4 == 0:
            if day < 1 or day > 29:
                return False
        else:
            if day < 1 or day > 28:
                return False
    else:
        return False
    return True
