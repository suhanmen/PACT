def strange_sort_list(lst):
    sorted_list = []
    sorted_lst = sorted(lst)
    
    while len(sorted_lst) > 0:
        sorted_list.append(sorted_lst.pop(0))
        if len(sorted_lst) > 0:
            sorted_list.append(sorted_lst.pop())
    
    return sorted_list
