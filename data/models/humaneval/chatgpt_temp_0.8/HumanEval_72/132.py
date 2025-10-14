# CANNOT PARSE CODE SNIPPET
def will_it_fly(q, w):
    # Check if q is balanced and the sum of its elements is less than or equal to w
    if q == q[::-1] and sum(q) <= w:
        return True
    else:
        return False
