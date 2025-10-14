# CANNOT PARSE CODE SNIPPET
def triples_sum_to_zero(l: list) -> bool:
    """
    triples_sum_to_zero takes a list of integers as an input.
    it returns True if there are three distinct elements in the list that
    sum to zero, and False otherwise.
    """
    if len(l) < 3:
        return False
    l.sort()
    for i in range(len(l)-2):
        if i > 0 and l[i] == l[i-1]:
            continue
        j, k = i+1, len(l)-1
        while j < k:
            s = l[i] + l[j] + l[k]
            if s > 0:
                k -= 1
            elif s < 0:
                j += 1
            else:
                return True
    return False
