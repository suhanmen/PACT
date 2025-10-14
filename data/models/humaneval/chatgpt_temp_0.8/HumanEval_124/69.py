def valid_date(date):
    # Check if the date string is not empty
    if not date:
        return False
    
    # Check if the date is in the format mm-dd-yyyy
    if not re.match(r'^\d{2}-\d{2}-\d{4}$', date):
        return False
    
    # Parse the date string into month, day and year
    month, day, year = map(int, date.split('-'))
    
    # Check if the month is in range 1-12
    if month < 1 or month > 12:
        return False
    
    # Check if the day is in range 1-31 for months with 31 days
    if month in [1, 3, 5, 7, 8, 10, 12] and (day < 1 or day > 31):
        return False
    
    # Check if the day is in range 1-30 for months with 30 days
    if month in [4, 6, 9, 11] and (day < 1 or day > 30):
        return False
    
    # Check if the day is in range 1-29 for February (leap year is not considered)
    if month == 2 and (day < 1 or day > 29):
        return False
    
    # If all checks pass, return True
    return True
