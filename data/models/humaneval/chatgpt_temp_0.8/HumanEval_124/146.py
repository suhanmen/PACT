def valid_date(date):
    """You have to write a function which validates a given date string and
    returns True if the date is valid otherwise False.
    The date is valid if all of the following rules are satisfied:
    1. The date string is not empty.
    2. The number of days is not less than 1 or higher than 31 days for months 1,3,5,7,8,10,12. And the number of days is not less than 1 or higher than 30 days for months 4,6,9,11. And, the number of days is not less than 1 or higher than 29 for the month 2.
    3. The months should not be less than 1 or higher than 12.
    4. The date should be in the format: mm-dd-yyyy

    for example: 
    valid_date('03-11-2000') => True

    valid_date('15-01-2012') => False

    valid_date('04-0-2040') => False

    valid_date('06-04-2020') => True

    valid_date('06/04/2020') => False
    """
    # Check if date string is not empty
    if len(date) == 0:
        return False

    # Check if date is in the format: mm-dd-yyyy
    date_parts = date.split("-")
    if len(date_parts) != 3:
        return False

    # Check if month is between 1 and 12
    try:
        month = int(date_parts[0])
        if month < 1 or month > 12:
            return False
    except ValueError:
        return False

    # Check if day is valid for the given month
    try:
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
    except ValueError:
        return False

    # Check if year is valid (we assume any year is valid for this exercise)
    try:
        year = int(date_parts[2])
    except ValueError:
        re
