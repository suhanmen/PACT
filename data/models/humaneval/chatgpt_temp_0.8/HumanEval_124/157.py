def valid_date(date):
    if len(date) != 10:
        return False
    
    month, day, year = date.split('-')
    
    try:
        month = int(month)
        day = int(day)
        year = int(year)
    except ValueError:
        return False
    
    if month < 1 or month > 12:
        return False
    
    if month == 2:
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            if day < 1 or day > 29:
                return False
        else:
            if day < 1 or day > 28:
                return False
    elif month in [4, 6, 9, 11]:
        if day < 1 or day > 30:
            return False
    else:
        if day < 1 or day > 31:
            return False
    
    return True
