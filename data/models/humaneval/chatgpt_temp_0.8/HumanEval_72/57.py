# CANNOT PARSE CODE SNIPPET
def will_it_fly(q, w):
    # Check if the list is a palindrome
    if q == q[::-1]:
        # Calculate the sum of the list
        q_sum = sum(q)
        # Check if the sum is less than or equal to the maximum weight
        if q_sum <= w:
            return True
    return False
