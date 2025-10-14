def valid_date(date):
    if len(date) != 10:  # check if the length of date string is 10
        return False

    try:
        month, day, year = map(int, date.split('-'))  # split the date string into month, day and year
    except ValueError:
        return False

    if month < 1 or month > 12:  # check if month is within the range 1 to 12
        return False

    if month in [1, 3, 5, 7, 8, 10, 12]:
        max_days = 31
    elif month in [4, 6, 9, 11]:
        max_days = 30
    else:
        max_days = 29 if (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)) else 28  # check for leap year

    if day < 1 or day > max_days:  # check if day is within the range 1 to max_days
        return False

    return True
