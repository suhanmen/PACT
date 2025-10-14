def valid_date(date):
    # Check if date string is empty
    if not date:
        return False
    
    # Split date string into month, day, and year
    date_parts = date.split("-")
    if len(date_parts) != 3:
        return False
        
    # Check if month is between 1 and 12
    try:
        month = int(date_parts[0])
        if month < 1 or month > 12:
            return False
    except ValueError:
        return False
        
    # Check if day is valid based on month and year
    try:
        day = int(date_parts[1])
        year = int(date_parts[2])
        if day < 1:
            return False
        elif month in [4, 6, 9, 11] and day > 30:
            return False
        elif month == 2:
            if ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0) and day > 29:
                return False
            elif day > 28:
                return False
        elif day > 31:
            return False
    except ValueError:
        return False
        
    # Check if year is valid
    i
