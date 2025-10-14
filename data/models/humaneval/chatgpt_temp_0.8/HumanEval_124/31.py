def valid_date(date):
    # Check if the date string is not empty
    if not date:
        return False
    
    # Split the date string into month, day, and year
    split_date = date.split('-')
    if len(split_date) != 3:
        return False
    
    month, day, year = split_date
    
    # Check if the month is a valid integer between 1 and 12
    try:
        month = int(month)
        if month < 1 or month > 12:
            return False
    except ValueError:
        return False
    
    # Check if the day is a valid integer between 1 and 31 and is valid for the given month
    try:
        day = int(day)
        if month in [1, 3, 5, 7, 8, 10, 12]:
            if day < 1 or day > 31:
                return False
        elif month in [4, 6, 9, 11]:
            if day < 1 or day > 30:
                return False
        elif month == 2:
            if day < 1 or day > 29:
                return False
    except ValueError:
        return False
    
    # Check if the year is a valid integer with 4
