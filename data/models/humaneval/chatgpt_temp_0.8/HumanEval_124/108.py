def valid_date(date):
    # Rule 1: The date string is not empty.
    if not date:
        return False

    # Rule 4: The date should be in the format: mm-dd-yyyy
    if len(date) != 10 or date[2] != '-' or date[5] != '-':
        return False

    # Extract month, day, year
    month, day, year = date[:2], date[3:5], date[6:]

    # Rule 3: The months should not be less than 1 or higher than 12.
    if not month.isdigit() or not 1 <= int(month) <= 12:
        return False

    # Rule 2: Check number of days based on month
    if month in ['01', '03', '05', '07', '08', '10', '12']:
        if not day.isdigit() or not 1 <= int(day) <= 31:
            return False
    elif month in ['04', '06', '09', '11']:
        if not day.isdigit() or not 1 <= int(day) <= 30:
            return False
    elif month == '02':
        if not day.isdigit() or not 1 <= int(day) <= 29:
            return False

    # All rules satisfied
    return True
