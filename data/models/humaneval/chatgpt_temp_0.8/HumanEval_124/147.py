def valid_date(date):
    """
    Validates a given date string and returns True if the date is valid otherwise False.
    """
    try:
        # The date should be in the format: mm-dd-yyyy
        month, day, year = date.split('-')
        
        # The date string is not empty.
        if not date:
            return False
        
        # The months should not be less than 1 or higher than 12.
        if not 1 <= int(month) <= 12:
            return False
        
        # The number of days is not less than 1 or higher than 31 days for months 1,3,5,7,8,10,12.
        # And the number of days is not less than 1 or higher than 30 days for months 4,6,9,11.
        # And, the number of days is not less than 1 or higher than 29 for the month 2.
        if month in ['01', '03', '05', '07', '08', '10', '12']:
            if not 1 <= int(day) <= 31:
                return False
        elif month in ['04', '06', '09', '11']:
            if not 1 <= int(day) <= 30:
                return False
        elif
