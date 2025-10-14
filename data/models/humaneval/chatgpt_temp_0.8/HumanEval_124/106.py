def valid_date(date):
    if len(date) != 10 or date[2] != '-' or date[5] != '-':
        return False

    month, day, year = date[:2], date[3:5], date[6:]

    if not month.isdigit() or not day.isdigit() or not year.isdigit():
        return False

    month, day, year = int(month), int(day), int(year)

    if month < 1 or month > 12:
        return False

    if month in (4, 6, 9, 11) and day > 30:
        return False

    if month == 2:
        max_days = 29 if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0 else 28
        if day > max_days:
            return False
    elif day > 31:
        return False

    return True
