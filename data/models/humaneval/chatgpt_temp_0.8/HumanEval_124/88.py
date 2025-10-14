def valid_date(date):
    # Rule 1
    if not date:
        return False
    
    # Split the date string into month, day and year components
    month, day, year = date.split('-')
    
    # Rule 2
    if int(month) in [1, 3, 5, 7, 8, 10, 12] and not 1 <= int(day) <= 31:
        return False
    elif int(month) in [4, 6, 9, 11] and not 1 <= int(day) <= 30:
        return False
    elif int(month) == 2 and not 1 <= int(day) <= 29:
        return False
    
    # Rule 3
    if not 1 <= int(month) <= 12:
        return False
    
    # Rule 4
    try:
        datetime.datetime.strptime(date, '%m-%d-%Y')
    except ValueError:
        return False
    
    return True
