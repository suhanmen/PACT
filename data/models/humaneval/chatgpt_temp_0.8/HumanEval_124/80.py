def valid_date(date):
    # Check if the date string is not empty
    if not date:
        return False

    # Split the date string into month, day, and year
    month, day, year = date.split('-')

    # Convert month, day, and year to integers
    try:
        month = int(month)
        day = int(day)
        year = int(year)
    except ValueError:
        return False

    # Check if the month is between 1 and 12
    if month < 1 or month > 12:
        return False

    # Check if the day is within the valid range for the given month
    if month in [1, 3, 5, 7, 8, 10, 12]:
        if day < 1 or day > 31:
            return False
    elif month in [4, 6, 9, 11]:
        if day < 1 or day > 30:
            return False
    elif month == 2:
        if day < 1 or day > 29:
            return False

    # Check if the date string is in the format: mm-dd-yyyy
    if not (len(str(month)) == 2 and len(str(day)) == 2 and len(str(year)) == 4):
        return False

    return True
