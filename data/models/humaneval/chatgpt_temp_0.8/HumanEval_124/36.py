def valid_date(date):
    """Validates a given date string and returns True if the date is valid, otherwise False."""
    months_with_31_days = [1, 3, 5, 7, 8, 10, 12]
    months_with_30_days = [4, 6, 9, 11]

    # Check if the date string is empty
    if not date:
        return False

    # Check if the date is in the format mm-dd-yyyy
    if len(date) != 10 or date[2] != '-' or date[5] != '-':
        return False

    # Check if the month is valid
    month = int(date[:2])
    if month < 1 or month > 12:
        return False

    # Check if the day is valid
    day = int(date[3:5])
    if month in months_with_31_days:
        if day < 1 or day > 31:
            return False
    elif month in months_with_30_days:
        if day < 1 or day > 30:
            return False
    else:
        # February
        if day < 1 or day > 29:
            return False

    return True
