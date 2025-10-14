def search(lst):
    for num in range(1, max(lst)+1):
        if lst.count(num) >= num:
            return num
    return -1
