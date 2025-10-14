def valid_date(date):
    """Validates a given date string and returns True if the date is valid, otherwise False."""
    try:
        # Check if the date string is not empty
        if not date:
            return False

        # Split the date into month, day, and year
        month, day, year = map(int, date.split('-'))

        # Check if the month is valid
        if not 1 <= month <= 12:
            return False

        # Check if the day is valid based on the month and year
        if month in [4, 6, 9, 11]:
            if not 1 <= day <= 30:
                return False
        elif month == 2:
            if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
                if not 1 <= day <= 29:
                    return False
            else:
                if not 1 <= day <= 28:
                    return False
        else:
            if not 1 <= day <= 31:
                return False

        return True
    except:
        return False
