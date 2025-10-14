def any_int(x, y, z):
    # Check if all numbers are integers
    if isinstance(x, int) and isinstance(y, int) and isinstance(z, int):
        # Check if any number is equal to the sum of the other two
        if x == y + z or y == x + z or z == x + y:
            return True
        else:
            return False
    else:
        return False
