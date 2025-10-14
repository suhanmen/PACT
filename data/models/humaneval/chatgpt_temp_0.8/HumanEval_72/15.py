# CANNOT PARSE CODE SNIPPET
def will_it_fly(q, w):
    # Check if q is balanced (i.e. palindromic)
    if q == q[::-1]:
        # Check if the sum of q's elements is less than or equal to w
        if sum(q) <= w:
            return True
        else:
            return False
    else:
        return False
