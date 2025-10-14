def valid_date(date):
    # Check if date string is not empty
    if not date:
        return False
    
    # Split the date string into day, month, and year
    date_parts = date.split('-')
    if len(date_parts) != 3:
        return False
    
    # Check if month is a valid value (between 1 and 12)
    month = int(date_parts[0])
    if month < 1 or month > 12:
        return False
    
    # Check if day is a valid value based on month
    day = int(date_parts[1])
    if month in [1, 3, 5, 7, 8, 10, 12]:
        if day < 1 or day > 31:
            return False
    elif month in [4, 6, 9, 11]:
        if day < 1 or day > 30:
            return False
    elif month == 2:
        if day < 1 or day > 29:
            return False
    
    # Check if year is a valid value (4 digits)
    year = int(date_parts[2])
    if year < 1000 or year > 9999:
        return False
    
    # Check if date is in the correct format (mm-dd-yyyy)
    if date_parts[0] == '' or date_parts[1] == '' or date_parts[2] == '':
      
