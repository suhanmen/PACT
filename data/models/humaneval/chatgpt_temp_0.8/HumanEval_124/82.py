def valid_date(date):
    # Rule 1: The date string is not empty.
    if not date:
        return False

    # Rule 4: The date should be in the format: mm-dd-yyyy
    if not re.match(r'^\d{2}-\d{2}-\d{4}$', date):
        return False

    # Extract the month, day, and year from the date string
    month, day, year = map(int, date.split('-'))

    # Rule 3: The months should not be less than 1 or higher than 12.
    if month < 1 or month > 12:
        return False

    # Rule 2: Validate the number of days for the given month and year
    days_in_month = {
        1: 31,
        2: 29 if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0 else 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }

    if day < 1 or day > days_in_month[month]:
        return False

    return True
