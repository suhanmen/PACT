def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,
    """
    if type(a) == str:
        a = a.replace(",", ".") # Replace comma with dot for string representation of real numbers
    if type(b) == str:
        b = b.replace(",", ".") # Replace comma with dot for string representation of real numbers
    if type(a) != type(b):
        return None # Return None if the variable types are different
    if a == b:
        return None # Return None if the values are equal
    if type(a) == int or type(a) == float:
        return max(a, b) # Return the larger variable if both are integers or floats
    else:
        return max(a, b, key=float) # Return the larger variable if both are strings representing real numbers
