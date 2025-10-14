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
    if not date:
        return False
    
    # Split the date string into month, day and year components
    try:
        month, day, year = date.split('-')
    except ValueError:
        return False

    # Convert the string components to integers
    try:
        month = int(month)
        day = int(day)
        year = int(year)
    except ValueError:
        return False

    # Check if the month is valid
    if month < 1 or month > 12:
        return False

    # Check if the day is valid for the given month
    if month == 2:
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            max_days = 29
        else:
            max_days = 28
    elif month in [4, 6, 9, 11]:
        max_days = 30
    else:
        max_days = 31
    if day < 1 or day > max_days:
        return False

    # Check if the year is valid (optional)
    if year < 1:
        return False

    # If all checks pass, the date is valid
    return True
