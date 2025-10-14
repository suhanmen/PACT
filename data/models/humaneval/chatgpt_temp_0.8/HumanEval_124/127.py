def valid_date(date):
    # Check if the date string is empty
    if not date:
        return False
    
    # Split the date string into month, day, and year
    parts = date.split('-')
    if len(parts) != 3:
        return False
    
    month, day, year = parts
    
    # Check if the month and day are integers
    try:
        month = int(month)
        day = int(day)
        year = int(year)
    except ValueError:
        return False
    
    # Check if the month is valid
    if month < 1 or month > 12:
        return False
    
    # Check if the day is valid
    if month in [1, 3, 5, 7, 8, 10, 12]:
        max_day = 31
    elif month in [4, 6, 9, 11]:
        max_day = 30
    else:
        # February
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            max_day = 29
        else:
            max_day = 28
    
    if day < 1 or day > max_day:
        return False
    
    # Check if the year is valid
    if year < 1:
        return False
    
    # Check if the date is in t
