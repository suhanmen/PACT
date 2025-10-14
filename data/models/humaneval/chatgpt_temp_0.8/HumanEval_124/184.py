def valid_date(date):
    if len(date) != 10:
        return False
    mm, dd, yyyy = date.split("-")
    try:
        mm = int(mm)
        dd = int(dd)
        yyyy = int(yyyy)
    except ValueError:
        return False
    if mm < 1 or mm > 12:
        return False
    if mm == 2:
        if yyyy % 4 == 0 and (yyyy % 100 != 0 or yyyy % 400 == 0):
            if dd < 1 or dd > 29:
                return False
        else:
            if dd < 1 or dd > 28:
                return False
    elif mm in [4, 6, 9, 11]:
        if dd < 1 or dd > 30:
            return False
    else:
        if dd < 1 or dd > 31:
            return False
    return True
