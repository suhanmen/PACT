def valid_date(date):
    # rule 1: check if the date string is not empty
    if not date:
        return False

    # rule 4: check if the date is in the format mm-dd-yyyy
    if not re.match(r'^\d{2}-\d{2}-\d{4}$', date):
        return False

    # extract month, day and year from the date string
    month, day, year = map(int, date.split('-'))

    # rule 3: check if the month is between 1 and 12
    if month < 1 or month > 12:
        return False

    # rule 2: check the number of days for the given month and year
    if month in [1, 3, 5, 7, 8, 10, 12]:
        max_days = 31
    elif month in [4, 6, 9, 11]:
        max_days = 30
    else:
        # check if it's a leap year
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            max_days = 29
        else:
            max_days = 28

    if day < 1 or day > max_days:
        return False

    # if all rules are satisfied, return True
    return True
