def valid_date(date):
    # check if the date string is not empty
    if not date:
        return False
    
    # split the date string into month, day and year
    month, day, year = date.split('-')
    
    # check if the month is between 1 and 12
    if not 1 <= int(month) <= 12:
        return False
    
    # check if the number of days is valid for the given month
    if month in ['01', '03', '05', '07', '08', '10', '12']:
        if not 1 <= int(day) <= 31:
            return False
    elif month in ['04', '06', '09', '11']:
        if not 1 <= int(day) <= 30:
            return False
    elif month == '02':
        # check for leap year
        if int(year) % 4 == 0 and (int(year) % 100 != 0 or int(year) % 400 == 0):
            if not 1 <= int(day) <= 29:
                return False
        else:
            if not 1 <= int(day) <= 28:
                return False
    
    # check if the date is in the format mm-dd-yyyy
    if not date[2] == '-' and date[5] == '-':
        return False
    
    
