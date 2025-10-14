def valid_date(date):
    date_parts = date.split("-")
    
    # check if the date string is not empty
    if len(date_parts) != 3:
        return False
    
    # check if the month is valid
    month = int(date_parts[0])
    if month < 1 or month > 12:
        return False
    
    # check if the day is valid
    day = int(date_parts[1])
    if month in [1, 3, 5, 7, 8, 10, 12]:
        if day < 1 or day > 31:
            return False
    elif month in [4, 6, 9, 11]:
        if day < 1 or day > 30:
            return False
    elif month == 2:
        year = int(date_parts[2])
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            if day < 1 or day > 29:
                return False
        else:
            if day < 1 or day > 28:
                return False
    
    # check if the year is valid
    year = int(date_parts[2])
    if year < 1:
        return False
    
    # check if the date format is valid
    if not date_parts[0].isdigit() or not date_parts[1].isdigit() or not 
