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
    try:
        # Check if the date string is not empty
        if len(date) == 10:
            # Split the date into month, day, and year
            month, day, year = date.split('-')
            # Convert the month, day, and year to integers
            month = int(month)
            day = int(day)
            year = int(year)
            # Check if the month is between 1 and 12
            if month >= 1 and month <= 12:
                # Check if the number of days is valid for the given month
                if (month in [1, 3, 5, 7, 8, 10, 12] and day >= 1 and day <= 31) or (month in [4, 6, 9, 11] and day >= 1 and day <= 30) or (month == 2 and day >= 1 and day <= 29):
                    # Check if the year is a valid year
                    if year >= 1 and year <= 9999:
                        return True
        return False
    except:
        return False
