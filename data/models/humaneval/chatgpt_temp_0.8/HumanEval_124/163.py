def valid_date(date):
    """Validates a given date string and returns True if the date is valid, otherwise False."""
    # Check if date string is empty
    if not date:
        return False
    
    # Split date string into month, day, and year components
    try:
        month, day, year = date.split('-')
    except ValueError:
        return False
    
    # Check if month is a valid integer between 1 and 12
    if not month.isdigit() or int(month) < 1 or int(month) > 12:
        return False
    
    # Check if day is a valid integer between 1 and 31 for certain months
    if month in {'01', '03', '05', '07', '08', '10', '12'}:
        max_days = 31
    elif month in {'04', '06', '09', '11'}:
        max_days = 30
    elif month == '02':
        # Check for leap year
        if int(year) % 4 == 0 and (int(year) % 100 != 0 or int(year) % 400 == 0):
            max_days = 29
        else:
            max_days = 28
    else:
        return False
    
    # Check if day is a valid integer between 1 and ma
