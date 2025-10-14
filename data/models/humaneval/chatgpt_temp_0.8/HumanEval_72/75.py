# CANNOT PARSE CODE SNIPPET
def will_it_fly(q, w):
    # check if the list is palindromic
    if q == q[::-1]:
        # check if the sum of elements is less than or equal to maximum possible weight
        if sum(q) <= w:
            return True
        else:
            return False
    else:
        return False
