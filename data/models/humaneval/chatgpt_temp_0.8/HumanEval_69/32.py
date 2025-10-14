python
def search(lst):
    for num in sorted(set(lst), reverse=True):
        if lst.count(num) >= num and num > 0:
            return num
    return -1
