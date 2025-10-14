def valid_date(date):
    if date.count('-') != 2:  # Check if date is in correct format
        return False

    month, day, year = date.split('-')  # Extract month, day, and year from date
    try:
        month = int(month)
        day = int(day)
        year = int(year)
    except ValueError:
        return False

    if not (1 <= month <= 12):  # Check if month is valid
        return False

    if month == 2:  # Check number of days in February
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):  # Leap year
            if not (1 <= day <= 29):
                return False
        else:  # Not a leap year
            if not (1 <= day <= 28):
                return False

    elif month in [4, 6, 9, 11]:  # Check number of days in months with 30 days
        if not (1 <= day <= 30):
            return False

    else:  # Check number of days in months with 31 days
        if not (1 <= day <= 31):
            return False

    return True
