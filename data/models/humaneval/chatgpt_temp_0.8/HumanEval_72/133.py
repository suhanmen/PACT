# CANNOT PARSE CODE SNIPPET
def will_it_fly(q, w):
    # check if list is palindrome
    if q == q[::-1]:
        # check if sum of elements is less than or equal to maximum weight
        if sum(q) <= w:
            return True
    return False
