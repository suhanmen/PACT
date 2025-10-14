def valid_date(date):
    # Check if date string is not empty
    if date == "":
        return False
    
    # Split the date string into month, day, and year
    month, day, year = date.split('-')
    
    # Convert month, day, and year to integers
    month = int(month)
    day = int(day)
    year = int(year)
    
    # Check if month is between 1 and 12
    if month < 1 or month > 12:
        return False
    
    # Check if day is valid for the given month
    if month in [1, 3, 5, 7, 8, 10, 12] and (day < 1 or day > 31):
        return False
    elif month in [4, 6, 9, 11] and (day < 1 or day > 30):
        return False
    elif month == 2:
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            if day < 1 or day > 29:
                return False
        else:
            if day < 1 or day > 28:
                return False
    
    # Check if year is valid
    if year < 1:
        return False
    
    # Check if date is in the format mm-dd-yyyy
    if len(str(month)) != 2 o
