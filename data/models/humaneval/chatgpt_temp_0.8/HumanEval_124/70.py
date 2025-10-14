def valid_date(date):
    # Check if the date string is empty
    if not date:
        return False

    # Split the date string into month, day, and year
    month, day, year = date.split('-')

    # Check if the month is valid
    if not 1 <= int(month) <= 12:
        return False

    # Check if the day is valid
    if month in ['01', '03', '05', '07', '08', '10', '12']:
        if not 1 <= int(day) <= 31:
            return False
    elif month in ['04', '06', '09', '11']:
        if not 1 <= int(day) <= 30:
            return False
    elif month == '02':
        if not 1 <= int(day) <= 29:
            return False

    # Check if the year is valid
    if not len(year) == 4:
        return False

    # Check if the date string is in the correct format
    if not date.count('-') == 2:
        return False

    return True
