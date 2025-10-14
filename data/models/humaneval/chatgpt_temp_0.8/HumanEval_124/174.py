def valid_date(date):
    """Validates a given date string and returns True if the date is valid, otherwise False."""
    try:
        # Check if the date string is not empty
        if not date:
            return False
        
        # Split the date string into month, day, and year components
        month, day, year = date.split('-')
        
        # Convert the components to integers
        month = int(month)
        day = int(day)
        year = int(year)
        
        # Check if the month is valid
        if month < 1 or month > 12:
            return False
        
        # Check if the day is valid for the given month and year
        if month in [1, 3, 5, 7, 8, 10, 12]:
            max_day = 31
        elif month in [4, 6, 9, 11]:
            max_day = 30
        elif year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            max_day = 29
        else:
            max_day = 28
        
        if day < 1 or day > max_day:
            return False
        
        # Check if the 
