# CANNOT PARSE CODE SNIPPET
def will_it_fly(q, w):
    """
    Returns True if the object q will fly, and False otherwise.
    The object q will fly if it's balanced (it is a palindromic list) and the sum of its elements 
    is less than or equal the maximum possible weight w.
    """
    if q != q[::-1]:  # Check if it's not palindromic
        return False
    if sum(q) > w:  # Check if the sum of elements is greater than the maximum possible weight
        return False
    return True
