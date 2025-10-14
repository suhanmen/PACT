def valid_date(date):
    if len(date) != 10:
        return False
    
    try:
        mm, dd, yyyy = [int(x) for x in date.split("-")]
        if not (1 <= mm <= 12):
            return False
        if mm in [1, 3, 5, 7, 8, 10, 12]:
            if not (1 <= dd <= 31):
                return False
        elif mm in [4, 6, 9, 11]:
            if not (1 <= dd <= 30):
                return False
        elif mm == 2:
            if not (1 <= dd <= 29):
                return False
            if dd == 29 and (yyyy % 4 != 0 or (yyyy % 100 == 0 and yyyy % 400 != 0)):
                return False
        else:
            return False
        return True
    except:
        return False
