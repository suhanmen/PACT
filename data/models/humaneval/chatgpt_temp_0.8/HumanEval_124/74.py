def valid_date(date):
    # Check if the date string is empty
    if not date:
        return False
    
    # Split the date string into month, day, and year
    month, day, year = date.split("-")
    
    # Convert the month, day, and year to integers
    try:
        month = int(month)
        day = int(day)
        year = int(year)
    except ValueError:
        return False
    
    # Check if the month is valid
    if month < 1 or month > 12:
        return False
    
    # Check if the day is valid for the given month
    if month in [1, 3, 5, 7, 8, 10, 12]:
        if day < 1 or day > 31:
            return False
    elif month in [4, 6, 9, 11]:
        if day < 1 or day > 30:
            return False
    elif month == 2:
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            if day < 1 or day > 29:
                return False
        else:
            if day < 1 or day > 28:
                return False
    
    # Check if the year is valid
    if year < 1:
        return 
