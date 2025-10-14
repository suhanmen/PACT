python
def pairs_sum_to_zero(l):
    seen = set()
    for x in l:
        if -x in seen:
            return True
        seen.add(x)
    return False
