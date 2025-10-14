def valid_date(date):
    # Check if the date string is not empty.
    if not date:
        return False

    # Split the date string into month, day and year.
    try:
        month, day, year = date.split('-')
    except ValueError:
        return False

    # Check if month, day and year are integers.
    try:
        month, day, year = int(month), int(day), int(year)
    except ValueError:
        return False

    # Check if the month is valid.
    if month < 1 or month > 12:
        return False

    # Check if the day is valid.
    if month in [1, 3, 5, 7, 8, 10, 12]:
        if day < 1 or day > 31:
            return False
    elif month in [4, 6, 9, 11]:
        if day < 1 or day > 30:
            return False
    elif month == 2:
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            if day < 1 or day > 29:
                return False
        else:
            if day < 1 or day > 28:
                return False

    # Check if the date is in the format mm-dd-yyyy.
    if
