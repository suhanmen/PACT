def valid_date(date):
    if not date or not isinstance(date, str):
        return False

    parts = date.split("-")
    if len(parts) != 3:
        return False

    month, day, year = parts
    if not (month.isdigit() and day.isdigit() and year.isdigit()):
        return False

    month, day, year = int(month), int(day), int(year)

    if not (1 <= month <= 12):
        return False

    if month == 2:
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            max_day = 29
        else:
            max_day = 28
    elif month in [4, 6, 9, 11]:
        max_day = 30
    else:
        max_day = 31

    if not (1 <= day <= max_day):
        return False

    return True
