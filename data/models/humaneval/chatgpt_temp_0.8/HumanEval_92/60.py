python
def any_int(x, y, z):
    # Check if all inputs are integers
    if all(isinstance(i, int) for i in [x, y, z]):
        # Check if x is equal to sum of y and z
        if x == y + z:
            return True
        # Check if y is equal to sum of x and z
        elif y == x + z:
            return True
        # Check if z is equal to sum of x and y
        elif z == x + y:
            return True
        else:
            return False
    else:
        return False
