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
    # check if date string is empty
    if not date:
        return False

    # check if date is in correct format
    if not re.match(r'\d{2}-\d{2}-\d{4}', date):
        return False

    # split date into month, day and year
    month, day, year = map(int, date.split('-'))

    # check if month is between 1 and 12
    if not 1 <= month <= 12:
        return False

    # check if number of days is valid for the given month
    if month in [1, 3, 5, 7, 8, 10, 12] and not 1 <= day <= 31:
        return False
    elif month in [4, 6, 9, 11] and not 1 <= day <= 30:
        return False
    elif month == 2:
        # check for leap year
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            if not 1 <= day <= 29:
                return False
        else:
            if not 1 <= day <= 28:
                return False

    return True
