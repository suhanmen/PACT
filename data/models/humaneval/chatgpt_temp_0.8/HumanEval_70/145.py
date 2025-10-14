def strange_sort_list(lst):
    '''
    Given list of integers, return list in strange order.
    Strange sorting, is when you start with the minimum value,
    then maximum of the remaining integers, then minimum and so on.

    Examples:
    strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
    strange_sort_list([]) == []
    '''

    sorted_lst = []

    # sort the list in ascending order
    sorted_lst = sorted(lst)

    # create two sublists by slicing the sorted list
    sublist1 = sorted_lst[::2]  # contains items at even indices
    sublist2 = sorted_lst[1::2]  # contains items at odd indices

    # reverse sublist2 so that it's sorted in descending order
    sublist2 = sublist2[::-1]

    # combine the two sublists
    sorted_lst = []
    for i in range(min(len(sublist1), len(sublist2))):
        sorted_lst.append(sublist1[i])
        sorted_lst.append(sublist2[i])

    # add any remaining items from the longer sublist
    if len(sublist1) > len(sublist2):
        sorted_lst.extend(sublist1[len(sublist2):])
    elif len(sublist2) > len(sublist1):
        sorted_lst.extend(sublist2[len(sublist1):])

    return sorted_lst
