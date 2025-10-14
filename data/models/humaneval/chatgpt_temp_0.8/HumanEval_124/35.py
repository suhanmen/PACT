def valid_date(date):
    """Validates a given date string and returns True if the date is valid, otherwise False."""
    months_with_31_days = [1, 3, 5, 7, 8, 10, 12]
    months_with_30_days = [4, 6, 9, 11]

    # Rule 1: The date string is not empty
    if not date:
        return False

    # Rule 4: The date should be in the format: mm-dd-yyyy
    if not re.match(r'^\d{2}-\d{2}-\d{4}$', date):
        return False

    month, day, year = map(int, date.split('-'))

    # Rule 2: Check number of days based on month
    if month in months_with_31_days:
        if day < 1 or day > 31:
            return False
    elif month in months_with_30_days:
        if day < 1 or day > 30:
            return False
    else:  # month is February
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):  # leap year
            if day < 1 or day > 29:
                return False
        else:
            if day < 1 or day > 28:
                return False

    # Rule 3: The months should not be less than 1 o
