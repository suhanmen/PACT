def search(lst):
    for num in sorted(set(lst), reverse=True):
        if num <= lst.count(num):
            return num
    return -1
