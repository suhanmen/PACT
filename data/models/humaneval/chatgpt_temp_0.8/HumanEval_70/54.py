def strange_sort_list(lst):
    result = []
    lst.sort()  # sort the original list in ascending order
    while lst:
        # remove and append the first (minimum) element of the remaining list
        result.append(lst.pop(0))
        if lst:
            # remove and append the last (maximum) element of the remaining list
            result.append(lst.pop())
    return result
