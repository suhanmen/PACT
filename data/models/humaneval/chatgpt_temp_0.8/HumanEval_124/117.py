def valid_date(date):
    # Check if the date string is not empty.
    if not date:
        return False
    
    # Check if the date is in the format: mm-dd-yyyy.
    parts = date.split('-')
    if len(parts) != 3:
        return False
    month, day, year = parts
    
    # Check if the year is a valid number.
    if not year.isdigit():
        return False
    
    year = int(year)
    if year < 1:
        return False
    
    # Check if the month is a valid number.
    if not month.isdigit():
        return False
    
    month = int(month)
    
    if month < 1 or month > 12:
        return False
    
    # Check if the day is a valid number.
    if not day.isdigit():
        return False
    
    day = int(day)
    
    if month in [1, 3, 5, 7, 8, 10, 12]:
        if day < 1 or day > 31:
            return False
    elif month in [4, 6, 9, 11]:
        if day < 1 or day > 30:
            return False
    elif month == 2:
        leap_year = False
        if year % 4 == 0:
            leap_year = Tru
