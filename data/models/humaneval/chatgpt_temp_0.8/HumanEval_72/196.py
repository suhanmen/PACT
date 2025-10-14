# CANNOT PARSE CODE SNIPPET
def will_it_fly(q, w):
    if q == q[::-1]:  # check if q is balanced (palindromic)
        if sum(q) <= w:  # check if sum of elements in q is less than or equal to w
            return True
        else:
            return False
    else:
        return False
