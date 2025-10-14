def compare_one(a, b):
    if type(a) == type(b):
        if type(a) == int or type(a) == float:
            if a > b:
                return a
            elif b > a:
                return b
            else:
                return None
        elif type(a) == str:
            if float(a.replace(',', '.')) > float(b.replace(',', '.')):
                return a
            elif float(b.replace(',', '.')) > float(a.replace(',', '.')):
                return b
            else:
                return None
    else:
        return None
