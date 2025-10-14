def valid_date(date):
    """Validates a given date string and returns True if the date is valid otherwise False."""
    # Check if the date string is empty
    if not date:
        return False
    
    # Split the date string into month, day, and year strings
    date_parts = date.split('-')
    if len(date_parts) != 3:
        return False
    month, day, year = date_parts
    
    # Check if the month is between 1 and 12
    if not month.isdigit() or int(month) < 1 or int(month) > 12:
        return False
    
    # Check if the day is valid for the given month and year
    if not day.isdigit():
        return False
    day = int(day)
    if month in ['01', '03', '05', '07', '08', '10', '12']:
        if day < 1 or day > 31:
            return False
    elif month in ['04', '06', '09', '11']:
        if day < 1 or day > 30:
            return False
    elif month == '02':
        if day < 1 or day > 29:
            return False
        if not (int(year) % 4 == 0 and (int(year) % 100 != 0 or int(year) %
