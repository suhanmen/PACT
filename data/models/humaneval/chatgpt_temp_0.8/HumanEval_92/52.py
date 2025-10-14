def any_int(x, y, z):
    if all(isinstance(n, int) for n in [x, y, z]):
        if x == y + z or y == x + z or z == x + y:
            return True
        else:
            return False
    else:
        return False
