def valid_date(date):
    if not date:
        return False

    month, day, year = date.split("-")

    # Check if month is valid
    if not 1 <= int(month) <= 12:
        return False

    # Check if day is valid
    if int(month) in [4, 6, 9, 11]:
        if not 1 <= int(day) <= 30:
            return False
    elif int(month) == 2:
        if int(year) % 4 == 0:
            if not 1 <= int(day) <= 29:
                return False
        else:
            if not 1 <= int(day) <= 28:
                return False
    else:
        if not 1 <= int(day) <= 31:
            return False

    # Check if year is valid
    if int(year) < 1:
        return False

    # Check if date is in the format mm-dd-yyyy
    if len(month) != 2 or len(day) != 2 or len(year) != 4:
        return False
    if not month.isdigit() or not day.isdigit() or not year.isdigit():
        return False
    if date.count("-") != 2:
        return False

    return True
