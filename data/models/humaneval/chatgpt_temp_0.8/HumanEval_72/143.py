# CANNOT PARSE CODE SNIPPET
def will_it_fly(q, w):
    if q == q[::-1] and sum(q) <= w:  # check if q is balanced and its sum is less than or equal to w
        return True
    else:
        return False
