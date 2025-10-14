def valid_date(date):
    # Check if the date string is not empty
    if not date:
        return False
    
    # Split the date string into day, month, and year
    parts = date.split('-')
    if len(parts) != 3:
        return False
    month, day, year = parts
    
    # Check if the month is valid
    if not month.isdigit() or int(month) < 1 or int(month) > 12:
        return False
    
    # Check if the day is valid
    if not day.isdigit():
        return False
    day = int(day)
    if month in ['04', '06', '09', '11'] and day > 30:
        return False
    elif month == '02':
        if day > 29:
            return False
        elif day == 29 and (not year.isdigit() or int(year) % 4 != 0 or (int(year) % 100 == 0 and int(year) % 400 != 0)):
            return False
    elif day > 31:
        return False
    
    # Check if the year is valid
    if not year.isdigit() or len(year) != 4:
        return False
    
    # If all checks pass, return True
    return True
