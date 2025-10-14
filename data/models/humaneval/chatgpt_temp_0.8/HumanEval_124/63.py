def valid_date(date):
    """
    Validates a given date string and returns True if the date is valid otherwise False.
    """
    try:
        # Split the date string into month, day and year strings
        month, day, year = date.split('-')
        
        # Check if the month is between 1 and 12
        if not 1 <= int(month) <= 12:
            return False
        
        # Check the number of days based on the month
        days_in_month = [31, 28 if int(year) % 4 != 0 or (int(year) % 100 == 0 and int(year) % 400 != 0) else 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if not 1 <= int(day) <= days_in_month[int(month) - 1]:
            return False
        
        # Check if the date string is in the format mm-dd-yyyy
        if not len(date) == 10 or not date[2] == date[5] == '-':
            return False
        
        # If all checks pass, the date is valid
        return True
    
    except:
        # If any exception occurs, the date is invalid
        return False
