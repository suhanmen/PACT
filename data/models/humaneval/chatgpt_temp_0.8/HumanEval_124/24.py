def valid_date(date):
    if not date:
        return False
    
    try:
        month, day, year = map(int, date.split('-'))
    except ValueError:
        return False
    
    if month < 1 or month > 12:
        return False
    
    if month in [4, 6, 9, 11] and (day < 1 or day > 30):
        return False
    
    if month == 2:
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            if day < 1 or day > 29:
                return False
        elif day < 1 or day > 28:
            return False
    elif day < 1 or day > 31:
        return False
    
    return True
