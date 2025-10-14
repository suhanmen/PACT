def valid_date(date):
    # Check if the date string is not empty
    if date == "":
        return False

    # Split the date string into month, day, and year
    month, day, year = date.split("-")

    # Convert the month, day, and year strings to integers
    try:
        month = int(month)
        day = int(day)
        year = int(year)
    except ValueError:
        return False

    # Check if the month is in the valid range (1-12)
    if month < 1 or month > 12:
        return False

    # Check if the day is in the valid range for the given month
    if month in [1, 3, 5, 7, 8, 10, 12] and (day < 1 or day > 31):
        return False

    if month in [4, 6, 9, 11] and (day < 1 or day > 30):
        return False

    if month == 2:
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            # Leap year
            if day < 1 or day > 29:
                return False
        else:
            # Not a leap year
            if day < 1 or day > 28:
                return False

    # 
