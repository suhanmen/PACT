def valid_date(date):
    # Check if the string is empty
    if not date:
        return False

    # Split the date into month, day, year
    date_list = date.split("-")
    if len(date_list) != 3:
        return False
    month, day, year = date_list

    # Check if the month is valid
    if not (1 <= int(month) <= 12):
        return False

    # Check if the day is valid
    days_in_month = {
        1: 31,
        2: 29 if int(year) % 4 == 0 and (int(year) % 100 != 0 or int(year) % 400 == 0) else 28,
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
    if not (1 <= int(day) <= days_in_month[int(month)]):
        return False

    # Check if the year is valid
    if len(year) != 4:
        return False

    # Check if the date is in the right format
    if not (len(month) == 2 and len(day) == 2 and len(year) == 4):
        return False

    return True
