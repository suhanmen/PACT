# CANNOT PARSE CODE SNIPPET
def will_it_fly(q, w):
    # check if q is balanced (it's a palindrome)
    if q == q[::-1]:
        # check if the sum of elements is less than or equal to w
        if sum(q) <= w:
            return True
        else:
            return False
    else:
        return False
