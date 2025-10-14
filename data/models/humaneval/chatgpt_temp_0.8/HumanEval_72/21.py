# CANNOT PARSE CODE SNIPPET
def will_it_fly(q, w):
    """
    Returns True if the object q will fly, and False otherwise.
    The object q will fly if it's balanced (it is a palindromic list) and the sum of its elements is less than or equal the maximum possible weight w.

    :param q: list of integers
    :param w: integer representing the maximum possible weight
    :return: boolean
    """

    # Check if the list is palindromic
    if q == q[::-1]:
        # Check if the sum of the list is less than or equal to the maximum possible weight
        if sum(q) <= w:
            return True
        else:
            return False
    else:
        return False
