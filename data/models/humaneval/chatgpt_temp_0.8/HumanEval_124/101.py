def valid_date(date):
    # Check if the date string is not empty
    if len(date) == 0:
        return False

    # Check if the date is in the format mm-dd-yyyy
    if not date[2] == date[5] == "-":
        return False

    # Extract month, day, and year from the date string
    month, day, year = date[:2], date[3:5], date[6:]

    # Check if month is between 1 and 12
    if not 1 <= int(month) <= 12:
        return False

    # Check if day is between 1 and 31 for months 1, 3, 5, 7, 8, 10, 12
    if int(month) in [1, 3, 5, 7, 8, 10, 12]:
        if not 1 <= int(day) <= 31:
            return False

    # Check if day is between 1 and 30 for months 4, 6, 9, 11
    elif int(month) in [4, 6, 9, 11]:
        if not 1 <= int(day) <= 30:
            return False

    # Check if day is between 1 and 29 for month 2 in a leap year
    elif int(month) == 2:
        if int(year) % 4 == 0:
            if not 1 <= int(day) <= 29:
                return False
        else:
            if not 1 <= int(day) <= 28:
   
