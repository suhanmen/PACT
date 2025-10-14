def valid_date(date):
    # Check if date string is not empty
    if not date:
        return False
    
    # Split the date string into month, day, and year
    try:
        month, day, year = date.split('-')
    except ValueError:
        return False
    
    # Check if month is between 1 and 12
    if not 1 <= int(month) <= 12:
        return False
    
    # Check if day is between 1 and 31 for Jan, Mar, May, Jul, Aug, Oct, and Dec
    if int(month) in [1, 3, 5, 7, 8, 10, 12]:
        if not 1 <= int(day) <= 31:
            return False
    # Check if day is between 1 and 30 for Apr, Jun, Sep, and Nov
    elif int(month) in [4, 6, 9, 11]:
        if not 1 <= int(day) <= 30:
            return False
    # Check if day is between 1 and 29 for Feb on leap year (divisible by 4) and between 1 and 28 for non-leap year 
    elif int(month) == 2:
        leap_year = (int(year) % 4 == 0)
        if leap_year and not 1 <= int(day) <= 29:
            return False
        elif not leap_year and not 1 <= int(day)
