def valid_date(date):
    months_with_31_days = [1, 3, 5, 7, 8, 10, 12]
    months_with_30_days = [4, 6, 9, 11]

    # Check if the date is not empty and in the correct format
    if not date or len(date) != 10 or date[2] != '-' or date[5] != '-':
        return False

    # Extract the month, day and year from the date string
    month = int(date[:2])
    day = int(date[3:5])
    year = int(date[6:])

    # Check if the month is between 1 and 12
    if month < 1 or month > 12:
        return False

    # Check if the number of days is valid according to the month
    if month in months_with_31_days:
        if day < 1 or day > 31:
            return False
    elif month in months_with_30_days:
        if day < 1 or day > 30:
            return False
    else:
        # February has 29 days on leap years and 28 on non-leap years
        leap_year = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
        if day < 1 or day > 29 if leap_year else 28:
            return False

    # If all checks passed
