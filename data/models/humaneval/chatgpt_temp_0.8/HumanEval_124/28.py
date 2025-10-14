def valid_date(date):
    # Checking if the date string is not empty
    if not date:
        return False

    # Splitting the date string into month, day and year
    month, day, year = date.split('-')

    # Converting month, day and year to integers
    month = int(month)
    day = int(day)
    year = int(year)

    # Checking if the month is between 1 and 12
    if month < 1 or month > 12:
        return False

    # Checking the number of days based on the month and year
    if month in [1, 3, 5, 7, 8, 10, 12]:
        if day < 1 or day > 31:
            return False
    elif month in [4, 6, 9, 11]:
        if day < 1 or day > 30:
            return False
    elif month == 2:
        if year % 4 == 0:
            if day < 1 or day > 29:
                return False
        else:
            if day < 1 or day > 28:
                return False

    # Checking if the date is in the format: mm-dd-yyyy
    if len(date) != 10 or date[2] != '-' or date[5] != '-':
        return False

    # If all the chec
