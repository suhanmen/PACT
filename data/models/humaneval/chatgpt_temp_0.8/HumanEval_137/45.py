def compare_one(a, b):
    # convert strings representing real numbers to floats
    if isinstance(a, str) and ("," in a or "." in a):
        a = float(a.replace(",", "."))
    if isinstance(b, str) and ("," in b or "." in b):
        b = float(b.replace(",", "."))

    # compare values and return the larger one in its given type
    if type(a) == type(b):
        if a > b:
            return a
        elif b > a:
            return b
        else:
            return None
    else:
        return None
