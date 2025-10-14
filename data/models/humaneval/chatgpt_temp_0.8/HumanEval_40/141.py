def triples_sum_to_zero(l: list):
    """
    triples_sum_to_zero takes a list of integers as an input.
    it returns True if there are three distinct elements in the list that
    sum to zero, and False otherwise.
    """
    if len(l) < 3:
        return False
    
    l.sort() # sort the list in ascending order
    
    for i in range(len(l)-2):
        # fix the first number and use two pointers to find the other two
        left = i+1
        right = len(l)-1
        while left < right:
            total = l[i] + l[left] + l[right]
            if total == 0:
                return True
            elif total < 0:
                left += 1
            else: # total > 0
                right -= 1
    
    return False
