def will_it_fly(q,w):
    # Check if q is palindromic
    if q == q[::-1]:
        # Calculate the sum of the elements in q
        q_sum = sum(q)
        # Check if the sum of elements is less than or equal to w
        if q_sum <= w:
            return True
        else:
            return False
    else:
        return False
