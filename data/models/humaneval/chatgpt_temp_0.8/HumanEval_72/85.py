# CANNOT PARSE CODE SNIPPET
def will_it_fly(q, w):
    # Check if q is balanced (palindromic list) and sum of its elements is less than or equal to the maximum weight w.
    return q == q[::-1] and sum(q) <= w
