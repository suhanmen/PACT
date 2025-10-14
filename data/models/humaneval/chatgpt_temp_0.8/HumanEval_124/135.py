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
    
    if month in [4, 6, 9, 11] and (day < 1 or day > 30):
        return False
    elif month == 2 and (day < 1 or day > 29):
        return False
    elif day < 1 or day > 31:
        return False
    
    return True
