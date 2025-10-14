def valid_date(date):
    # Rule 1: Check if date string is not empty
    if not date:
        return False
    
    # Rule 4: Check if date is in the format mm-dd-yyyy
    parts = date.split("-")
    if len(parts) != 3:
        return False
    try:
        month, day, year = int(parts[0]), int(parts[1]), int(parts[2])
    except ValueError:
        return False
    
    # Rule 2: Check if the number of days is valid for the given month
    if month == 2:
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            max_days = 29
        else:
            max_days = 28
    elif month in {4, 6, 9, 11}:
        max_days = 30
    else:
        max_days = 31
    if not (1 <= day <= max_days):
        return False
    
    # Rule 3: Check if month is valid
    if not (1 <= month <= 12):
        return False
    
    # All rules are satisfied
    return True
