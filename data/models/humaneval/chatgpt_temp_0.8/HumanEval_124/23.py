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
    # rule 1: check if the date string is not empty
    if not date:
        return False
    
    # rule 4: check if the date is in the format mm-dd-yyyy
    if len(date) != 10 or date[2] != '-' or date[5] != '-':
        return False
    
    # separate day, month and year values
    month, day, year = int(date[:2]), int(date[3:5]), int(date[6:])
    
    # rule 2: check the number of days based on the month
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
    
    # rule 3: check if the month is between 1 and 12
    if month < 1 or month > 12:
        return False
    
    return True
