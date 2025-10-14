def valid_date(date):
    # check if the date string is not empty
    if not date:
        return False
    
    # split the date string into month, day, and year
    try:
        month, day, year = date.split('-')
    except ValueError:
        return False
    
    # check if the month is between 1 and 12
    if not 1 <= int(month) <= 12:
        return False
    
    # check the number of days based on the month and year
    if month in ['01', '03', '05', '07', '08', '10', '12']:
        max_day = 31
    elif month in ['04', '06', '09', '11']:
        max_day = 30
    elif month == '02':
        if int(year) % 4 == 0 and (int(year) % 100 != 0 or int(year) % 400 == 0):
            max_day = 29
        else:
            max_day = 28
    else:
        return False
    
    # check if the day is between 1 and max_day for the month
    if not 1 <= int(day) <= max_day:
        return False
    
    # check if the year is a valid four-digit number
    if not year.isdigit() or len(year) != 4:
        return Fal
