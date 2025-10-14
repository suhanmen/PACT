def valid_date(date):
    # Check if the date string is empty
    if not date:
        return False

    # Split the date into month, day, and year
    try:
        month, day, year = map(int, date.split('-'))
    except ValueError:
        return False

    # Check if the month is between 1 and 12
    if not 1 <= month <= 12:
        return False

    # Check the number of days based on the month and year
    if month in [1, 3, 5, 7, 8, 10, 12]:
        if not 1 <= day <= 31:
            return False
    elif month in [4, 6, 9, 11]:
        if not 1 <= day <= 30:
            return False
    elif month == 2:
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            if not 1 <= day <= 29:
                return False
        else:
            if not 1 <= day <= 28:
                return False

    # Check if the date is in the format: mm-dd-yyyy
    if not date[2] == date[5] == '-':
        return False

    return True
