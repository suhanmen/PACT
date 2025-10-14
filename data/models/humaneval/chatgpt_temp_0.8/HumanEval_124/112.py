def valid_date(date):
    # Check if the date string is not empty
    if not date:
        return False
    
    # Check if the date is in the format mm-dd-yyyy
    if len(date) != 10 or date[2] != '-' or date[5] != '-':
        return False
    
    # Parse the month, day, and year from the date string
    month = int(date[0:2])
    day = int(date[3:5])
    year = int(date[6:10])
    
    # Check if the month is between 1 and 12
    if month < 1 or month > 12:
        return False
    
    # Check if the day is valid for the given month and year
    if month in [1, 3, 5, 7, 8, 10, 12]:
        if day < 1 or day > 31:
            return False
    elif month in [4, 6, 9, 11]:
        if day < 1 or day > 30:
            return False
    elif month == 2:
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            if day < 1 or day > 29:
                return False
        else:
            if day < 1 or day > 28:
                return False
    
    # If all checks pass, the date is valid
