def valid_date(date):
    # Check if date string is empty
    if not date:
        return False
    
    # Check if date is in the correct format
    if not re.match(r'\d{2}-\d{2}-\d{4}', date):
        return False
    
    # Split date into month, day, year
    month, day, year = map(int, date.split('-'))
    
    # Check if month and day are within valid ranges
    if month < 1 or month > 12:
        return False
    if day < 1 or (month == 2 and day > 29) or (month in [4, 6, 9, 11] and day > 30) or (month in [1, 3, 5, 7, 8, 10, 12] and day > 31):
        return False
    
    # Check if year is a valid 4-digit number
    if year < 1000 or year > 9999:
        return False
    
    return True
