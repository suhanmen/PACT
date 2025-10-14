# CANNOT PARSE CODE SNIPPET
def will_it_fly(q, w):
    # Check if the object is a palindromic list
    if q == q[::-1]:
        # Check if the sum of the elements is less than or equal the maximum possible weight
        if sum(q) <= w:
            return True
    return False
