def valid_date(date):
    if len(date) != 10: # rule 1
        return False
    month, day, year = date.split('-')
    if not month.isdigit() or not day.isdigit() or not year.isdigit(): # check all parts of date are digits
        return False
    month, day, year = int(month), int(day), int(year)
    if month < 1 or month > 12: # rule 3
        return False
    if month in [1, 3, 5, 7, 8, 10, 12] and (day < 1 or day > 31): # rule 2
        return False
    elif month in [4, 6, 9, 11] and (day < 1 or day > 30):
        return False
    elif month == 2:
        if year % 4 != 0 and (day < 1 or day > 28): # not a leap year 
            return False
        elif year % 4 == 0 and (day < 1 or day > 29): # leap year 
            return False
    else:
        return True
