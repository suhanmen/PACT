def strange_sort_list(lst):
    odd = sorted(lst)[::-2]
    even = sorted(lst)[1::2][::-1]
    return odd + even
