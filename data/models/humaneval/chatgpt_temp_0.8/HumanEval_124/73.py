def valid_date(date):
    # Rule 1: Date string should not be empty
    if not date:
        return False
    
    # Rule 4: Date should be in the format mm-dd-yyyy
    try:
        month, day, year = date.split('-')
    except ValueError:
        return False
    
    # Rule 2: Validating days based on month
    month_days = {
        '01': 31, '02': 29, '03': 31, '04': 30, 
        '05': 31, '06': 30, '07': 31, '08': 31, 
        '09': 30, '10': 31, '11': 30, '12': 31
    }
    if month not in month_days.keys():
        return False
    if not (1 <= int(day) <= month_days[month]):
        return False
    
    # Rule 3: Month should be between 1 and 12
    if not (1 <= int(month) <= 12):
        return False
    
    # All rules passed
    return True
