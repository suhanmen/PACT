def valid_date(date):
    try:
        # Check the format of the date
        date_list = date.split('-')
        if len(date_list) != 3:
            return False
        month, day, year = int(date_list[0]), int(date_list[1]), int(date_list[2])
        
        # Check if month is valid
        if month < 1 or month > 12:
            return False
        
        # Check if day is valid
        if month in [1, 3, 5, 7, 8, 10, 12]:
            if day < 1 or day > 31:
                return False
        elif month in [4, 6, 9, 11]:
            if day < 1 or day > 30:
                return False
        elif month == 2:
            if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
                if day < 1 or day > 29:
                    return False
            else:
                if day < 1 or day > 28:
                    return False
        
        return True
    
    except:
        return False
