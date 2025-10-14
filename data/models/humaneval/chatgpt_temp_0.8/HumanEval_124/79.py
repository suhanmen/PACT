def valid_date(date):
    if not date:
        return False

    # Split the date into month, day, and year
    try:
        month, day, year = date.split('-')
    except ValueError:
        return False

    # Check if month, day, and year are valid integers
    try:
        month = int(month)
        day = int(day)
        year = int(year)
    except ValueError:
        return False

    # Check if month is between 1 and 12
    if not 1 <= month <= 12:
        return False

    # Check number of days based on month and year
    if month in [1, 3, 5, 7, 8, 10, 12]:
        max_days = 31
    elif month in [4, 6, 9, 11]:
        max_days = 30
    else:  # February
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            max_days = 29
        else:
            max_days = 28

    if not 1 <= day <= max_days:
        return False

    # Check if date is in the format mm-dd-yyyy
    if date.count('-') != 2:
        return False

    return True
