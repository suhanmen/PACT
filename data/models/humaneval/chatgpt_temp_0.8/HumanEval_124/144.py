def valid_date(date):
    """
    Validates the given date string in format mm-dd-yyyy.

    Returns True if the date is valid, otherwise False.
    """
    # Check that the input is not empty
    if not date:
        return False

    # Split the date string into month, day, and year
    try:
        month, day, year = date.split('-')
    except ValueError:
        # The date string is not in the correct format
        return False

    # Convert month, day, and year to integers
    try:
        month = int(month)
        day = int(day)
        year = int(year)
    except ValueError:
        # The month, day, or year is not a valid integer
        return False

    # Check that the month is between 1 and 12
    if month < 1 or month > 12:
        return False

    # Check that the day is valid for the given month and year
    if month in [1, 3, 5, 7, 8, 10, 12]:
        if day < 1 or day > 31:
            return False
    elif month in [4, 6, 9, 11]:
        if day < 1 or day > 30:
            return Fals
