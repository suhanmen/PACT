def valid_date(date):
    # Check if date string is not empty
    if not date:
        return False

    # Split the date string into month, day, and year components
    month, day, year = date.split("-")

    # Convert the month, day, and year components to integers
    try:
        month = int(month)
        day = int(day)
        year = int(year)
    except ValueError:
        return False

    # Check if month is between 1 and 12
    if month < 1 or month > 12:
        return False

    # Check the number of days based on the month
    if month in [1, 3, 5, 7, 8, 10, 12]:
        max_days = 31
    elif month in [4, 6, 9, 11]:
        max_days = 30
    else:
        # Check for leap year
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            max_days = 29
        else:
            max_days = 28
    if day < 1 or day > max_days:
        return False

    # Check if date is in the format: mm-dd-yyyy
    if f"{month:02d}-{day:02d}-{year}" != date:
        return False

    # If all 
