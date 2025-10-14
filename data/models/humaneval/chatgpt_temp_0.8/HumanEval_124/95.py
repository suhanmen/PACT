def valid_date(date):
    if not date:
        return False

    # Split the date string into month, day, and year
    month, day, year = date.split('-')

    try:
        # Convert month, day, and year to integers
        month_int = int(month)
        day_int = int(day)
        year_int = int(year)
    except ValueError:
        return False

    # Check that the month is between 1 and 12
    if month_int < 1 or month_int > 12:
        return False

    # Check the number of days based on the month
    if month_int in [1, 3, 5, 7, 8, 10, 12]:
        if day_int < 1 or day_int > 31:
            return False
    elif month_int in [4, 6, 9, 11]:
        if day_int < 1 or day_int > 30:
            return False
    elif month_int == 2:
        if year_int % 4 == 0 and (year_int % 100 != 0 or year_int % 400 == 0):
            # Leap year
            if day_int < 1 or day_int > 29:
                return False
        else:
            # Not a leap year
            if day_int < 1 or day_int > 28:
              
