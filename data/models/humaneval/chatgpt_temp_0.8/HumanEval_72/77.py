# CANNOT PARSE CODE SNIPPET
def will_it_fly(q, w):
    # Check if the list is palindromic
    if q == q[::-1]:
        # Check if the sum of elements is less than or equal to maximum weight
        if sum(q) <= w:
            return True
        else:
            return False
    else:
        return False
