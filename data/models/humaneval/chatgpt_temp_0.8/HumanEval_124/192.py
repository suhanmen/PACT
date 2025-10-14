def valid_date(date):
    if not date: # checking if the date string is not empty
        return False
    
    # extracting month, day, and year from the date string
    month, day, year = date.split('-')
    
    # checking if the month is not less than 1 or higher than 12
    if not 1 <= int(month) <= 12:
        return False
    
    # checking the number of days for each month
    if month in ['01', '03', '05', '07', '08', '10', '12'] and not 1 <= int(day) <= 31:
        return False
    elif month in ['04', '06', '09', '11'] and not 1 <= int(day) <= 30:
        return False
    elif month == '02':
        if int(year) % 4 == 0 and not (1 <= int(day) <= 29):
            return False
        elif not (1 <= int(day) <= 28):
            return False
    
    # checking if the date is in the format mm-dd-yyyy
    if len(year) != 4 or len(month) != 2 or len(day) != 2:
        return False
    
    # if all the above conditions are passed, then the date is valid
    return True
