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
    if date == "":
        return False

    # Check if date is in the correct format
    if not re.match(r"\d{2}-\d{2}-\d{4}", date):
        return False

    # Convert date string to a date object
    try:
        month, day, year = map(int, date.split("-"))
        date_obj = datetime.date(year, month, day)
    except ValueError:
        return False

    # Check if number of days is valid for given month
    if date_obj.month in [1, 3, 5, 7, 8, 10, 12]:
        if date_obj.day < 1 or date_obj.day > 31:
            return False
    elif date_obj.month in [4, 6, 9, 11]:
        if date_obj.day < 1 or date_obj.day > 30:
            return False
    elif date_obj.month == 2:
        if date_obj.day < 1 or date_obj.day > 29:
            return False

    # Check if month is valid
    if date_obj.month < 1 or date_obj.month > 12:
        return False

    # If all checks passed, date is valid
    return True
