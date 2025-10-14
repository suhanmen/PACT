def search(lst):
    max_num = max(lst)
    frequency = [0] * (max_num + 1)
    for num in lst:
        frequency[num] += 1
    for i in range(1, max_num+1):
        if i <= frequency[i]:
            return i
    return -1
