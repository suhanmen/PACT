def search(lst):
    highest = -1
    for num in set(lst):
        if num == lst.count(num) and num > highest:
            highest = num
    return highest
