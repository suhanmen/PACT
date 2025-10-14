def by_length(arr):
    names = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    arr = [x for x in arr if 1 <= x <= 9]
    arr.sort()
    arr.reverse()
    result = [names[x-1] for x in arr]
    return result
