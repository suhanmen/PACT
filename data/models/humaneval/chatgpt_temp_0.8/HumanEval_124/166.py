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

    # Check if the date string is empty
    if not date:
        return False

    # Split the date string into its component parts
    parts = date.split("-")

    # Check if there are three parts
    if len(parts) != 3:
        return False

    # Check if the parts are all numeric
    if not all(part.isdigit() for part in parts):
        return False

    # Convert the parts to integers
    month, day, year = map(int, parts)

    # Check if the month is valid
    if month < 1 or month > 12:
        return False

    # Check if the day is valid for the given month
    if month in [1, 3, 5, 7, 8, 10, 12]:
        if day < 1 or day > 31:
            return False
    elif month in [4, 6, 9, 11]:
        if day < 1 or day > 30:
            return False
    elif month == 2:
        if day < 1 or day > 29:
            return False

    # Check if the year is valid
    if year < 1 or year > 9999:
        return False

    # Check if the date string is in the correct format
    if len(part
