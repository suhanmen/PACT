def any_int(x, y, z):
    if type(x) == type(y) == type(z) == int:
        if x == y + z or y == x + z or z == x + y:
            return True
        else:
            return False
    else:
        return False
