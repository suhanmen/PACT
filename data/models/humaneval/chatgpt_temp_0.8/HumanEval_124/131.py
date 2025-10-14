def valid_date(date):
    # Check if the date string is empty
    if not date:
        return False
    
    # Split the date string into month, day, and year
    month, day, year = date.split('-')
    
    # Check if the month is valid
    if int(month) < 1 or int(month) > 12:
        return False
    
    # Check if the day is valid for the given month
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
    if int(day) < 1 or int(day) > days_in_month[int(month)]:
        return False
    
    # Check if the year is valid
    if int(year) < 1:
        return False
    
    # Check if the date is in the correct format
    if len(date) != 10:
        return False
    if date[2] != '-' or date[5] != '-':
        return False
    
    # If all checks pass, return True
    re
