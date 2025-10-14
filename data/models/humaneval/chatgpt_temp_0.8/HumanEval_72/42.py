# CANNOT PARSE CODE SNIPPET
def will_it_fly(q, w):
    if q != q[::-1]:  # check if the list is not palindromic
        return False

    if sum(q) <= w:  # check if the sum of the elements is less than or equal to the maximum possible weight
        return True

    return False
