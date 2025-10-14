import re

def valid_date(date):
    if not date:
        return False
    
    date_pattern = re.compile(r"^(0?[1-9]|1[0-2])-(0?[1-9]|[12]\d|3[01])-(\d{4})$")
    match = date_pattern.match(date)
    
    if not match:
        return False
    
    month = int(match.group(1))
    day = int(match.group(2))
    year = int(match.group(3))
    
    if month == 2:
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            max_days = 29
        else:
            max_days = 28
    elif month in [4, 6, 9, 11]:
        max_days = 30
    else:
        max_days = 31
    
    if day < 1 or day > max_days:
        return False
    
    return True
