# CANNOT PARSE CODE SNIPPET
def will_it_fly(q, w):
    # Check if the object is balanced
    if q == q[::-1]:
        # Calculate the sum of the elements
        total_weight = sum(q)
        # Check if the total weight is less than or equal to the maximum possible weight
        if total_weight <= w:
            return True
        else:
            return False
    else:
        return False
