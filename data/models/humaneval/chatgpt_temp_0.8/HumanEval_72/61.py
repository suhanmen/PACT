# CANNOT PARSE CODE SNIPPET
def will_it_fly(q, w):
    """
    Returns True if the object q will fly, and False otherwise.
    The object q will fly if it's balanced (it is a palindromic list) and the sum of its elements is less than or equal the maximum possible weight w.
    """
    if q != q[::-1]:
        # if the list is not a palindrome, it's unbalanced
        return False
    elif sum(q) > w:
        # if the sum of elements is greater than the maximum weight, it's too heavy
        return False
    else:
        # otherwise, it's balanced and light enough to fly
        return True
