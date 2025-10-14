python
def strange_sort_list(lst):
    result = []
    lst.sort()  # sort the input list in ascending order
    while lst:
        result.append(lst.pop(0))  # add the smallest value to the result list
        if lst:
            result.append(lst.pop())  # add the largest value to the result list (if there are any remaining)
    return result
