def search(lst):
    max_num = max(lst)
    for num in range(1, max_num+1):
        if lst.count(num) >= num:
            return max(filter(lambda x: x > 0 and lst.count(x) >= x, set(lst)))
    return -1
