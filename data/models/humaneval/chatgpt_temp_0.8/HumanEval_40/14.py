def triples_sum_to_zero(l: list):
    """
    triples_sum_to_zero takes a list of integers as an input.
    it returns True if there are three distinct elements in the list that
    sum to zero, and False otherwise.
    """
    # First, let's handle the base case where the list has less than 3 elements
    if len(l) < 3:
        return False
    
    # Now we need to iterate over all possible triplets of distinct elements in the list
    for i in range(len(l)):
        for j in range(i+1, len(l)):
            for k in range(j+1, len(l)):
                if l[i] + l[j] + l[k] == 0:
                    return True
    
    # If we haven't found any triplet that sum to zero, return False
    return False
