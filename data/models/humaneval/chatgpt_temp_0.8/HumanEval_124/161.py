def valid_date(date):
    if not date:
        return False
    
    # split the date string into month, day, and year
    month, day, year = date.split('-')
    
    # convert the month, day, and year to integers
    month = int(month)
    day = int(day)
    year = int(year)
    
    # check if the month is valid
    if month < 1 or month > 12:
        return False
    
    # check if the day is valid
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
    
    # check if the year is valid
    if year < 1:
        return False
    
    # check if the date is in the correct format
    if len(str(month)) != 2 or len(str(day)) != 2 or len(str(year
