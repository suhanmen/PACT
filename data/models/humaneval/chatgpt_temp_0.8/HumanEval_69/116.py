def search(lst):
    max_value = -1
    for num in set(lst):
        if num > 0 and lst.count(num) >= num:
            max_value = max(max_value, num)
    return max_value
