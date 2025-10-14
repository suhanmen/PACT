def valid_date(date):
    if len(date) != 10:
        return False
    elif date[2] != "-" or date[5] != "-":
        return False
    else:
        month = int(date[0:2])
        day = int(date[3:5])
        year = int(date[6:10])
        if month < 1 or month > 12:
            return False
        elif month == 2:
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
        else:
            return True
